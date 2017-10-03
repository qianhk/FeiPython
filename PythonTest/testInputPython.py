#!/usr/bin/python
# coding=utf-8

print('{0:.3f}'.format(1.0/3))
print('{0:_^11}'.format('kai'))
print(r'\'{name}\' wrote\n "{book}"'.format(name='kai', book='good book'))

# print('kai', end=' ') //python3
# print('is')
# print('good man')

s = '''This is Multi Line String
 Second Line
Third Line'''
print(s)


number = 23
guess = int(input('input a number: '))

if guess == number:
    print ('you guess it')
elif guess < number:
    print ('oh, small')
else:
    print ("ok great than {}".format(number))

print ('Done.')



running = True

while running:
    guess = int(input('input a number: '))

    if guess == number:
        print ('you guess it')
        running = False;
    else:
        print ("error, again.")
else:
    print ('while end')


for i in range(1, 9, 2):
    if i >= 7:
        print ('i >= 7')
        break   #有break 那么else不会执行了
    elif i == 5:
        print("i==5")
        continue
    else:
        print (i)
else:
    print('for end')


