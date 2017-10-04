#!/usr/bin/python
# coding=utf-8


# list

print ('\n\n\nlist\n')

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

print ('\n\n\ntuple\n')

zoo = ('python', 'elephant', 'kaikai')

print ('Number of animals in the zoo is', len(zoo), zoo)

new_zoo = 'monkey', 'camel', zoo
print ('Number of cages in the new zoo is', len(new_zoo), new_zoo)

print ('Animals brought from old zoo are', new_zoo[2])

print ('Last animal brought fromold zoo is', new_zoo[2][2])

print ('Number of animals in the new zoo is', len(new_zoo) - 1 + len(new_zoo[2]))

singleton = (2, )
print ('only one zoo is', singleton)




# dictionary

print ('\n\n\ndictionary\n')

addressBook = {
    'kai': 'qhk83@qq.com'
    , 'kai2': 'qhk22@qq.com'
    , 'bbb': 'bbb@qq.com'
    , 'kai4': 'qhk44@qq.com'
}

print ('kai address is', addressBook['kai'], len(addressBook))

del addressBook['kai2']

print ('address map:', addressBook)

for name, email in addressBook.items():
    print (name, email)

addressBook['abc'] = 'abc@qq.com'

print ('address map:', addressBook)

if 'kai4' in addressBook:
    print ('kai4 is', addressBook['kai4'])

# keys = addressBook.keys() #python3  'dict_keys' object has no attribute 'sort'
# keys.sort()
keys = sorted(addressBook)
for key in keys:
    print ('key:', key, 'email:', addressBook[key])




# sequence

print ('\n\n\n sequence \n')

name = 'kaikai'

print ('sho list', shoplist)
print ('shop list -1', shoplist[-1]) #倒数第一个
print ('kaikai[1]', name[1])

print ('slice list 1:3', shoplist[1:3])
print ('slice list 3:', shoplist[3:])
print ('slice list 1:-1', shoplist[1:-1])

print ('string 1:3', name[1:3])
print ('string 2:', name[2:])
print ('string 1:-1', name[1:-1])

print ('slice list ::2', shoplist[::2]) #step
print ('slice list ::-1', shoplist[::-1]) #step



# set

print ('\n\n\n set \n')

bri = {'set1', 'set2', 'set3', 'set4'}

print ('set3' in bri)
print ('set5' in bri)

bric = bri.copy()
bric.add('set5')
print ('set5' in bric)
print ('bric.issuperset(bri)', bric.issuperset(bri))
print ('bri.issuperset(bric)', bri.issuperset(bric))
print ('bri.issubset(bric)', bri.issubset(bric))



delimiter = "_"
print (delimiter.join(shoplist))





