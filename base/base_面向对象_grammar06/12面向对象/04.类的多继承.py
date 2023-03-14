# 父类
class Donkey:
    def pake(self):
        print("它正在驮货物")

    def run(self):
        print("它正在走路")


# 父类
class Horse:
    def run(self):
        print("它正在奔跑")


# 子类，继承Donkey,Horse
class Mule(Horse, Donkey):
    pass


# 对象实例化
mule = Mule()
mule.run()
mule.pake()
# 方法的调用，继承靠近右边的替代之前的