#!/usr/bin/python
# coding=utf-8


# list

shoplist = ['apple', 'kai', 'mango', 'carrot', 'banana']

print ('I have', len(shoplist), 'items to purchase.')

print ('These items are:')
for item in shoplist:
    print (item)

print ('\nI also have to buy rice.')
shoplist.append('rice')
print ('My shopping list is now', shoplist)

print ('\nI will sort my list now')
shoplist.sort()
print ('My shopping list is now', shoplist)

print ('')
print ('The first item I will buy is', shoplist[0])
oldItem = shoplist[0]
del shoplist[0]

print ('I bought the', oldItem)

shoplist.insert(1, 'yang')

print ('My shopping list is now', shoplist)




# tuple

zoo = ('python', 'elephant', 'kaikai')

print ("\n\n\n")
print ('Number of animals in the zoo is', len(zoo), zoo)

new_zoo = 'monkey', 'camel', zoo
print ('Number of cages in the new zoo is', len(new_zoo), new_zoo)

print ('Animals brought from old zoo are', new_zoo[2])

print ('Last animal brought fromold zoo is', new_zoo[2][2])

print ('Number of animals in the new zoo is', len(new_zoo) - 1 + len(new_zoo[2]))


