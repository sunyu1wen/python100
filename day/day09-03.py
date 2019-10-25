# encoding:utf-8
class Person(object):
    "人"

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Person):
    "学生"

    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self._sex = sex

    @property
    def name(self):
        return self._name

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, sex):
        self._sex = sex

    def play(self):
        print('%s性别是%s正在愉快的玩耍打地鼠-子类.' % (self._name, self._sex))


class Teacher(Person):
    "laoshi"

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def teach(self, add):
        print("----name :%s  age: %s  grade : %s--add： %s-" % (self._name, self._age, self._grade, add))


def main():
    stu = Student("学生", "28", "man")
    stu.play()
    teacher = Teacher("老师B", 30, "大三")
    teacher.grade =  "grade"
    teacher.teach("添加的参数课程")


if __name__ == '__main__':
    main()
