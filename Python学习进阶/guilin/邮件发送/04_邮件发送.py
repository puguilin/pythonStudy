# !/usr/bin/python3
# _*_ coding:utf-8 _*_
#
# Copyright (C) 2023 - 2023 pgl, Inc. All Rights Reserved 
#
# @Time    : 2023/2/gyx 10:05
# @Author  : pgl
# @File    : 04_邮件发送.py
# @IDE     : PyCharm


import smtplib
from email.contentmanager import subtype
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
import smtplib


def send_simple():
    # 登陆邮箱
    smtp_obj = smtplib.SMTP('smtp.qq.com')  # 定义的语言规则
    smtp_obj.login('1929592393@qq.com', 'xdqdybuuqovbhech')
    # 编写内容
    msg = '你要的邮件来了  The mail you asked for has arrived'
    msg_body = MIMEText(msg, 'plain', 'utf-8')  # 包装主题内容  plain 类型(普通)
    msg_body['Subject'] = Header('测试邮件', 'utf-8')  # 文件标题
    msg_body['From'] = Header('测试部门', 'utf-8')  #
    # 发送
    smtp_obj.sendmail('1929592393@qq.com', ['2469671909@qq.com'], msg_body.as_string())
    #                       发送的邮箱           发送给谁               .as_string() 转成字符串文件


def send_html():
    # 登陆邮箱
    smtp_obj = smtplib.SMTP('smtp.qq.com')  # 定义的语言规则
    smtp_obj.login('1929592393@qq.com', 'xdqdybuuqovbhech')
    # 编写内容
    msg = '''
        <h1>你要的邮件来了  The mail you asked for has arrived</h1>
        <p>测试一个邮件内容，内容是一个html编写的</p>
        <p><a href="http://www.baidu.com">官网</p>
    '''
    msg_body = MIMEText(msg, 'html', 'utf-8')  # 包装主题内容  html 类型(html邮件)
    msg_body['Subject'] = Header('测试邮件', 'utf-8')  # 文件标题
    msg_body['From'] = Header('测试部门', 'utf-8')  #
    # 发送
    smtp_obj.sendmail('1929592393@qq.com', ['2469671909@qq.com'], msg_body.as_string())
    #                       发送的邮箱           发送给谁               .as_string() 转成字符串文件


# 发送带有附件的 (有问题)
def send_fujian():
    # 登陆邮箱
    smtp_obj = smtplib.SMTP('smtp.qq.com', 25)  # 定义的语言规则
    smtp_obj.login('1929592393@qq.com', 'xdqdybuuqovbhech')

    # 设置收发件邮箱
    mail_suer = "1929592393@qq.com"
    mail_receivces = ["2469671909@qq.com"]

    # 设置邮件主体
    mail_msg = MIMEMultipart()  # 表示邮件由多部分组成
    mail_msg["From"] = Header("Alex", "utf-8")
    mail_msg["To"] = Header("Handsome Boy", "utf-8")
    mail_msg["Subject"] = Header("Python 邮件测试", "utf-8")

    # 创建一个带附件的实例
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header("subject邮件主题", 'utf-8')

    # 正文添加文字
    content = '发送带有附件的正文说明'
    txt1 = MIMEText(content, _subtype='html', _charset='utf-8')
    msg.attach(txt1)

    # 正文添加图片  正文-图片 只能通过html格式来放图片
    file1 = "./res/1.jpg"
    fp = open(r"res/1.jpg", 'rb')
    message_msg = """
           <p>Python 邮件发送测试...</p>
           <p><a href="https://www.baidu.com">这是一个链接</a></p>
           <p>图片示例：</p>
           <p><img src="cid:image1"></p>"""
    msg.attach(MIMEText(message_msg, 'html', 'utf-8'))
    image = MIMEImage(fp.read())
    fp.close()
    # 定义图片 ID，在 HTML 文本中引用
    image.add_header('Content-ID', '<image1>')
    msg.attach(image)

    # 构造附件1，txt文件
    att1 = MIMEText(open("res/中文.txt", "rb").read(), "base64", 'utf-8')
    att1[
        # 二进制流数据（如常见的文件下载）此处可省略这一行 MIMEText 因为MIMEApplication默认子类型是application/octet-stream
        "Content-Type"] = "application/octet-stream"
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # 附件名称为中文时的写法
    # 注意：此处basename要转换为gb2312编码，否则中文会有乱码。
    #      特别，此处的basename为unicode编码，所以可以用basename.encode('gb2312')
    #            如果basename为utf-8编码，要用basename.decode('utf-8').encode('gb2312')
    """basename = 'res / 中文.txt'
    att1["Content-Disposition"] = 'attachment; filename=%s' % basename.encode('gb2312')
    """
    # 附件名称为英文时的写法
    att1["Content-Disposition"] = 'attachment; filename="1.txt"'
    msg.attach(att1)

    # 构造附件2，xlsx文件
    att2 = MIMEText(open('res/test.xlsx', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="test.xlsx"'
    msg.attach(att2)

    # 构造附件3-图片
    image = MIMEImage(open(r'res/1.jpg', 'rb').read(), _subtype=subtype)
    image.add_header('Content-Disposition', 'attachment', filename='img.jpg')  # filename 名称可以随便写
    msg.attach(image)

    # 可以添加多个附件
    # msg.attach(att4)

    # 发送邮件
    smtp_obj.sendmail(mail_suer, mail_receivces, msg.as_string())


if __name__ == '__main__':
    # send_simple()
    # send_html()
    send_fujian()
