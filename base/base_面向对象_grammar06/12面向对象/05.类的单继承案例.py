# 定义父类 Animal
class Animal:
    # 初始化属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义父类的方法1：eat
    def eat(self):
        print(f'{self.name}正在吃东西。。。。。。')

    # 定义父类的方法2:drink
    def drink(self):
        print(f'{self.name}正在喝水。。。。。。')


# 定义子类 Dog继承Animal
class Dog(Animal):
    # # 定义子类的自己的属性
    # def __init__(self,name,age,color):
    #     self.color = color
    # 定义子类的自己的方法
    def Gatekeeper(self):
        print(f'的{self.name}正在看门。。。。。')


# 定义子类 Cat继承父类Animal
class Cat(Animal):
    # 定义自己的方法
    def Catch_mouse(self):
        print(f'{self.name}正在抓老鼠。。。。。')


# 对象的实例化
dog = Dog('大黄', 10)
print(dog.name)
dog.eat()
dog.drink()
dog.Gatekeeper()
# print(dog.color)
# 对象的实例化
cat = Cat('咪咪', 3)
cat.eat()
cat.drink()
cat.Catch_mouse()
