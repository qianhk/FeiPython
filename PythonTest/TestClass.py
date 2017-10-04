#!/usr/bin/env python
# coding=utf-8
# encoding=utf-8

import pickle
import io
import sys

print ('sys.getdefaultencoding()', sys.getdefaultencoding())
reload(sys)
sys.setdefaultencoding('utf-8')
print ('sys.getdefaultencoding()', sys.getdefaultencoding())

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

    def __del__(self):
        print ('{} is being __del__'.format(self.name))

    def __str__(self):
        return '__str__{}'.format(self.name)

    def say_hi(self):
        print ('Hello {}, how are you?'.format(self.name))

    def __len__(self):
        return len(self.name)

    def __getitem__(self, item):
        print ('type(item)', type(item))
        if item == 'two':
            return self.name[2]
        else:
            return self.name[item]

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

    def __str__(self):
        return '{} {}'.format(Person.__str__(self), self.score)

    def __lt__(self, other):
        return self.score < other.score


p = Person('KaiKai')
p.say_hi()
print (p)

p2 = Person('Yang')
p2.say_hi()

print ('p2.name', p2.name)
# print ('p2.__age', p2.__age)

teacher = Teacher('Teacher_Kai', 18888)
teacher.say_hi()

student = Student('Student_Kai', 105)
student.say_hi()

student2 = Student('Student_Kai', 102)
student2.say_hi()

print ('student < student2', student < student2)

print ('len(student)', len(student))

print ('student[2]', student[2], 'student[5]', student[5])

print ('student[\'two\']', student['two'])

Person.how_maney()

p.die()
p2.die()
Person.how_maney()


personFile = 'person.data'
f = open(personFile, 'wb')
pickle.dump(student, f)
f.close()

print ('new student {}'.format(student))

del student

f = open(personFile, 'rb')
student = pickle.load(f)
print ('new student2 {}'.format(student))
student.say_hi()

unicodeFile = 'unicodeText.data'
f = open(unicodeFile, 'wt')
f.write("好人一生平安,此乃中文chinese text")
f.close()

unicodeFile = 'unicodeText2.data'
with open(unicodeFile, 'wt') as f:
    f.write(u"好人一生平安,此乃中文chinese text")
# f.close()

# f = io.open(unicodeFile, 'rt')
# f.read



