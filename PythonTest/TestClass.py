#!/usr/bin/env python
# coding=utf-8


class Person:

    personCount = 0

    def __init__(self, name):
        Person.personCount += 1
        # self.__class__.personCount += 1
        self.name = name
        self.__age = 22     #private member

    def die(self):
        print ('{} is being destroyed!'.format(self.name))
        Person.personCount -= 1
        self.__age = -1
        if Person.personCount == 0:
            print ('This is last one.')
        else:
            print ('There still ', Person.personCount)

    def say_hi(self):
        print ('Hello {}, how are you?'.format(self.name))

    @classmethod
    def how_maney(cls):
        print ('We have {:d} person'.format(Person.personCount))


class Teacher(Person):

    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.salary = salary

    def say_hi(self):
        Person.say_hi(self)
        print ('salary', self.salary)


class Student(Person):

    def __init__(self, name, score):
        Person.__init__(self, name)
        self.score = score

    def say_hi(self):
        Person.say_hi(self)
        print ('score', self.score)


p = Person('KaiKai')
p.say_hi()
print (p)

p2 = Person('Yang')
p2.say_hi()

print ('p2.name', p2.name)
# print ('p2.__age', p2.__age)

teacher = Teacher('Teacher', 18888)
teacher.say_hi()

student = Student('Student', 100)
student.say_hi()

Person.how_maney()

p.die()
p2.die()
Person.how_maney()






