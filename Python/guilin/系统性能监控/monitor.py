import configparser
import logging
import time
from datetime import datetime

import psutil
import schedule
import yagmail

logging.basicConfig(filename='monitor.log',
                    filemode='a',
                    format='%(asctime)s %(filename)s --> %(funcName)s [line:%(lineno)d] [%(levelname)s]: %(message)s',
                    datefmt='%F %T',
                    level=logging.INFO)
logger = logging.getLogger()


class Mail:

    def __init__(self, host, port, user, password, receiver):
        """创建并连接登录邮箱服务器

        :param host: 发送邮箱服务器地址
        :param port: 发送邮箱服务器端口
        :param user: 寄件人邮箱账户
        :param password: 寄件人邮箱账户密码或授权码
        :param receiver: 收件人邮箱账户信息 （str or list or tuple）
        """
        self.receiver = receiver
        self.yag = yagmail.SMTP(host=host,
                                port=port,
                                user=user,
                                password=password)
        self.yag.set_logging(log_level=yagmail.logging.DEBUG,
                             file_path_name='monitor.log')

    def send_mail(self, subject, contents, attachments=None):
        """发送邮件

        :param subject: 邮件主题
        :param contents: 邮件正文内容
        :param attachments: 邮件的附件
        :return:
        """
        self.yag.send(to=self.receiver.split(', '),
                      subject=subject,
                      contents=contents,
                      attachments=attachments)


def monitor(mail_conf: dict):
    """系统性能监控

    :param mail_conf: 邮件发送所需配置信息
    :return:
    """
    # 获取信息
    # 1）物理cpu核心数
    cpu_count = psutil.cpu_count(logical=False)
    # 2）cpu使用率
    cpu_percent = psutil.cpu_percent(interval=1)
    # 3）内存信息
    mem_info = psutil.virtual_memory()
    # 4）磁盘信息
    disk_info = psutil.disk_usage('C:\\')
    # 5）网络信息
    net_info = psutil.net_io_counters()
    # 6）当前系统采集时间
    current_time = datetime.now().strftime('%F %T')

    # 1GB = 1024MB = 1024 * 1024KB = 1024 * 1024 * 1024B
    gunit = 1024 * 1024 * 1024

    # 日志记录信息
    log_str = "系统性能定时监控如下：\n"
    log_str += "|-------------------|------------|-----------------|------------------|----------------------------|\n"
    log_str += "|     监控时间      |  CPU使用率 |    内存使用率   |    硬盘使用率    |         网络收发量         |\n"
    log_str += "|                   | (共%d核CPU) | (总计%.2fG内存) | (总计%.2fG硬盘) |                            |\n" \
               % (cpu_count, mem_info.total / gunit, disk_info.total / gunit)
    log_str += "|-------------------|------------|-----------------|------------------|----------------------------|\n"
    log_str += "|%s|   %5.2f%%   |      %5.2f%%     |      %5.2f%%      |     收:%5.2fG/发:%5.2fG    |\n" \
               % (current_time, cpu_percent, mem_info.percent, disk_info.percent, net_info.bytes_recv / gunit,
                  net_info.bytes_sent / gunit)
    log_str += "|-------------------|------------|-----------------|------------------|----------------------------|\n"
    logger.info(log_str)

    contents = "前方高能预警，系统资源出现紧张。" + log_str
    # 判断系统资源占用率是否超过阈值
    if cpu_percent > 10 or mem_info.percent > 10 or disk_info.percent > 10:
        # Mail(**mail_conf).send_mail(邮件主题, 邮件正文, 邮件附件)
        Mail(**mail_conf).send_mail('【系统监控报告】', contents, ['monitor.logs'])


def main():
    # 获取config.ini配置文件信息
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')

    # 获取发送邮件的相关配置信息
    mail_conf = dict(config.items('mail'))

    # 每10分钟执行一次job
    schedule.every(0.1).minutes.do(monitor, mail_conf)

    # 循环检测周期调度是否已过期
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()


