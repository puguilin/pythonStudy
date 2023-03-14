# 父类
class Animal:
    # 初始化属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义方法
    def eat(self):
        print(f'{self.name}正在干饭。。。。。。。。。')

    def drink(self):
        print(f'{self.name}正在喝水。。。。。。。。。')


# Animal的子类Dog
class Dog(Animal):
    # 定义自己的方法
    def look_house(self):
        print(f'{self.name}正在看家。。。。。。。。。。')


# Dog的子类FlyDog
class FlyDog(Dog):
    def fly(self):
        print(f'{self.name}正在飞行。。。。。。。。。')


# 对象的实体化
xtq = FlyDog('哮天犬', 2300)
print(xtq.name)
# 调用父类Dog的方法
xtq.look_house()
# 调用Animal的方法
xtq.eat()
xtq.drink()
# 调用自己的方法
xtq.fly()
