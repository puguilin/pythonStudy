# 定义类
class LoginPage:
    # 初始化
    def __init__(self, username, password, verify_code):
        # 传参
        self.username = username
        self.password = password
        self.verify_code = verify_code

    def admin(self):
        print(f'登陆成功，登录用户为{self.username},密码为{self.password},'
              f'验证码为{self.verify_code}')


# 对象的实例化
user1 = LoginPage('user1', 'user123456', '1234')
# 调用方法
user1.admin()
