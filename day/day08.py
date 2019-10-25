# k = (raw_input('k = '))
# fm = 1
# print("k = " + k)
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self,course_name):
        print('%s learning %s.'%(self.name,course_name))


def main():
    stu1 = Student('sunyw','18');
    stu1.study('Python design')

    stu2 = Student('Bocai',88)
    stu2.study('PhotoShop')

if __name__=='__main__':
    main();