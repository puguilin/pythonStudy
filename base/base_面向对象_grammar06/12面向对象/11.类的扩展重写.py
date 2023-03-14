# 定义父类
class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# 子类
class Phone(Goods):
    def __init__(self, name, price, capacity, size):
        super().__init__(name, price)
        self.capacity = capacity
        self.size = size


phone = Phone('华为', '5999', '1T', '7寸')

print(phone.name, phone.price, phone.capacity, phone.size)
# print(Phone.mro())
# # 查看继承关系
# print(dir(phone))
# # 查看对象属性
