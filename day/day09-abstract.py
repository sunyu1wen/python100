# encoding: utf-8
from abc import ABCMeta, abstractmethod


class Pet(object):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        "发出声音"
        pass


class dog(Pet):
    def make_voice(self):
        print('%s:汪汪汪。。。' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [dog("旺财"), Cat("招财猫"), dog("大黄")]
    for Pet in pets:
        Pet.make_voice()


if __name__ == '__main__':
    main()
