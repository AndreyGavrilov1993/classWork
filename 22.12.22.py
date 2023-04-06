'''size=int(input())
for j in range(size):
    for i in range(size):
      print("*", end=" ")
    print()'''
'''a=int(input())
size=int(input("size"))
for i in range(size):
    for j in range(size):
        print(a, end="\t")
        a+=1
    print()'''
'''size=int(input())
num=int(input())
buf=num
for i in range(size):
    for j in range(size):
        print(num, end="\t")
        num+=1
    print()
    buf*=10
    num=buf'''
'''size=int(input("size: "))
num=int(input("first number: "))
for i in range(size):
    for j in range(size):
        print(num, end="\t")
        num+=1
    print()
    num=(num-1)*10'''
'''size=int(input("size: "))
for i in range(size):
    for j in range(size):
        if(i==0 or i==size-1 or j==0 or j==size-1):
         print("*", end=" ")
        else: print(" ", end=" ")
    print()'''
'''size=int(input("size: "))
for i in range(size):
    print("*", end=" ")
    for j in range(size-2):
        print("*" if(i==0 or i==size-1) else " ",end=" ")
    print("*")'''
'''size=int(input())
for i in range(size):
    print("*", end=" ")
print()
for i in range(size-2):
    print("*", end=" ")
    for j in range(size-2):
        print(" ", end=" ")
    print("*")

for i in range(size):
    print("*", end=" ")
print()'''
'''Вывести диагональную линию звёздочками в соответствии с стороной квадрата'''
'''size=int(input("size: "))
for i in range(size):
    for j in range(i):
        print(" ", end="")
    print("*")'''
'''size=int(input("size: "))
for i in range(size):
    for j in range(i+1):
        print("*", end=" ")
    print()'''
'''size=int(input())
for i in range(size):
    for j in range(size-i):
        print("*", end=" ")
    print()'''
'''size=int(input())
for i in range(size):
    for j in range(size-i-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print(" ")'''
'''size=int(input("size: "))
count=1
a=True
for i in range(size):
    if (a):
       for j in range(size):
        print(count, end="\t")
        count+=1
       count+=size-1
    else:
        for j in range(size):
            print(count, end="\t")
            count-=1
        count+=size+1
    a=not(a)
    print(a)'''
'''size=int(input("size: "))
count=1
a=True
for i in range(size):
       for j in range(size):
           print(count, end="\t")
           count=count+a
       count+=size+a*-1
       a*=-1
       print()'''
'''Пользователь вводит начало и конец диапазона,
 а затем стороны квадрата, вывести квадрат заполненный случайными значениями'''
import random
size=int(input("сторона квадрата: "))
min=int(input("начало диапазона: "))
max=int(input("конец диапазона: "))
minimum=max
maximum=min
if (min>max): min,max=max,min
for i in range(size):
    for j in range(size):
        num=random.randint
        if num<minimum: minimum=num
        if num>maximum: maximum=num
        print(random.randint(min,max), end="\t")
    print()
print("min:", minimum, "max:", maximum)



