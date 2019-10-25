#encoding:utf-8
class Person(object):

    __slots__ = ('_name','_age','_gender')
    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex
    # 访问器 - getter方法
    @property
    def name(self):
        return self._name
    @property
    def sex(self):
        return self._sex
    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age
    @sex.setter
    def sex(self,sex):
        self._sex = sex


    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._age)


def main():
    person = Person('王大锤', 12,'man')
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
