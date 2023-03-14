# 定义类
class Person:
    # 初始化
    def __init__(self, name, weight):
        # 传参赋值
        self.name = name
        self.weight = weight

    # 方法1，运动体重瘦0.5
    def run(self):
        self.weight -= 0.5
        print(f'{self.name}运动了，体重减轻了0.5公斤')

    # 方法2:吃东西增加1公斤
    def eat(self):
        self.weight += 1
        print(f'{self.name}吃了东西，体重增加了1公斤')

    # 方法3：调用实例化对象，打印当前的体重
    def __str__(self):
        return f'{self.name}的当前体重为{self.weight}'


# 对象的实例化
person = Person('小郑', 77)

print(person)
person.run()
print(person)
person.eat()
print(person)
