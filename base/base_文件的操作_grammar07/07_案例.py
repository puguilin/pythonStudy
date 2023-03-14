# 定义输入的值
code = input("请选择功能【1:注册】【2:登录】")
if code == "1":
    NewUser = input("请输入注册名")
    NewPassword = input("请输入密码")
    f = open('user_info', mode='a', encoding='utf8')
    f.write(f'{NewUser}|{NewPassword}\n')
    f.close()
elif code == "2":
    User = input('请输入用户名')
    Password = input('请输入密码')
    f = open('user_info', mode='r', encoding='utf8')
    ifo = f.readlines()
    for i in ifo:
        user = i.strip().split('|')
        if user[0] == User and user[1] == Password:
            print("登陆成功")
            break
    else:
        print("登陆失败")
