class Brid():
    def fly(self):
        print('小鸟正在飞')

class Airport:
    def fly(self):
        print('飞机正在飞行')


class Xtq:
    def fly(self):
        print('哮天犬正在飞行')


def fly(obj):
    obj.fly()


fly(Xtq())
fly(Airport())
fly(Brid())