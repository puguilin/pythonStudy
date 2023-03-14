# 父类
class Phone:
    def __init__(self):
        self.name = '苹果手机'

    def fn(self):
        print('当前是苹果手机')

    def __str__(self):
        return f'当前是{self.name}'


# 子类继承Phone
class iPhone13(Phone):
    # def __init__(self):
    #     self.name = '苹果13ProMax'

    def fn(self):
        print("当前是苹果13ProMax")

    def __str__(self):
        return f'当前是{self.name}'



phone = iPhone13()
phone.fn()
print(phone.name)
print(phone)
