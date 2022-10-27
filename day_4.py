# print(a[::-1])
# print(a[4][2])

# c = a.count(12)
# print(c)
# a = ['hello', 12, 1.9, 'hello', True, [1, 2, 4, 5], 12]
# print(a)
# a.append(1)

# print(a)
# a.remove('hello')
# a.remove('hello')
# print(a)

# a = ['hello', 12, 1.9, 'hello', True, [1, 2, 4, 5], 12]

# s = a.index(1.9)
# a.pop(s)
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# b = [7, 8, 9, 10, 11, 12]

# a.extend(b)
# print(a + b)

# a = [1, 7, 8, 9, 1, 0, 11, 1, 2, 2, 3, 4, 5, 6]
# a.sort(reverse=True)
# print(a)



#Exe1
# a =[]
# a.append(['lucky']) 
# a.append (2)
# a.append (3)
# a.append (4)
# a.append (5)
# print (a)

#Exe2
# a = ('Dinara',3, 4,)
# print(a[0])
# print(a[1])
# print(a[2])

#exe3
# a = ['hello', 12, 1.9,True, 12]

#Exe4
# a = ['hello','aslan','sultan','bratan','ali']
# c = ' '.join(a)
# print (c)

#Exe5
# a = ['hello','aslan']
# c = ['adok','ali']
# print (a+c)

#Exe6
# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
# print (names.count('Jack'))

#Exe7
# names = ['Jack', 'Jimmy', 'Oskar', 'Jhon', 'Jackson', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
# names.remove('Oskar')
# print(names)

# Exe8
# a = []
# a.append(['Ali',2004,'Backend'])
# print(a)

#Exe9
# a = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# b = a.index('loop')
# a.pop(6)
# print(b)
# print(a)

#Exe10
# a = [123, 321, 2, 543] 
# print(a[0] * a[1] * a[2] * a[3])

#Exe11
# list_1 = []
# list_2 = []

# a = int(input('>> '))
# b = int(input('>> '))
# c = int(input('>> '))
# d = int(input('>> '))
# e = int(input('>> '))
# if a % 2 == 0:
#     list_1.append(a)
# else:
#     list_2.append(a)
# if b % 2 == 0:
#     list_1.append(b)
# else:
#     list_2.append(b)
# if c % 2 == 0:
#     list_1.append(c)
# else:
#     list_2.append(c)
# if d % 2 == 0:
#     list_1.append(d)
# else:
#     list_2.append(d)
# if e % 2 == 0:
#     list_1.append(e)
# else:
#     list_2.append(e)
# print (list_1)
# print (list_2)

#Exe12
# list = []
# a = int(input('>>'))
# b = int(input('>>'))
# c = int(input('>>'))
# d = int(input('>>'))
# e = int(input('>>'))
# list.append(a)
# list.append(b)
# list.append(c)
# list.append(d)
# list.append(e)
# f = max(list)
# g = sum(list)
# h = min(list)
# srednee = g / len(list)
# print (f"max: {f}, min: {h}, sredne: {g}")

#Exe13
# products = ['яблоко', 'груша', 'арбуз','банан', 'мандарин']
# a = products.index('яблоко')
# b = products.index('груша') 
# c = products.index('арбуз')
# d = products.index('банан')
# e = products.index('мандарин')
# print (a)
# print(b)
# print(c)
# print(d)
# print(e)
# a1 = int(input('выбери товар:'))
# print(a1)
# products.pop(a1)
# print (products)
# if a1 == 0:
#     print ('яблоки закончились выберите другой продукт')
# elif a1 == 1:
#     print ('груша закончились выберите другой продукт')
# elif a1 == 2:
#     print ('арбуз закончились выберите другой продукт')
# elif a1 == 3:
#     print ('банан закончились выберите другой продукт')
# elif a1 == 4:
#     print ('мандарин закончились выберите другой продукт')
# b1 = int(input('выберите продукт:' ))
# print (b1) 


# products = ['яблоко', 'груша', 'арбуз','банан', 'мандарин']
# a = products.index('яблоко')
# b = products.index('груша') 
# c = products.index('арбуз')
# d = products.index('банан')
# e = products.index('мандарин')
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# f = int(input('выберите другой товар: '))
# if f >= 0 and f<=4:
#     products.pop(f)
# else:
#     print ('lol')
# print(products)