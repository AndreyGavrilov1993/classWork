#1
'''
n=int(input())
i=1
while (i<=n/2):
 k=2
 if(n%i==0):
    flag=True
    while (k<i):
     if n%k==0:
       flag=False
       break
       k+=1
      if (flag): print(i, end=" ")
    i+=1
 k=2
 flag=True
 while (k<n):
         if n%k==0:
                 flag=False
                 break
                 k+=1
         if (flag): print(n, end=" ")'''

#2 Пользователь вводит число, посчитать сумму всех чисел, которые кратны этому числу в диапазоне от 0 до 100
'''n=int(input())
summa=0
i=2
while (i<=100):
        if i%n==0:
                summa+=i
                i+=1
        print(summa)'''
'''for i in range(0,10,1):
    print(i, end=" ")

i=0
while(i<10):
    print(i)
    i+=1'''
'''n=int(input())
for n in range(0,n,1):
    print(n, end=" ")'''
'''n=int(input())
for n in range(n,-1,-1):
    print(n, end=" ")'''
'''n=int(input())
summa=0
for i in range(0,n,1):
    summa+=i
    print(summa)'''
'''n=int(input())
summa=0
for i in range(2,n+1,2):
        print(i, end=" ")'''
'''n=int(input())
summa=0

k=2 if (n>0) else -2

if n>0: k=2
else: k=-2

for i in range(k,n+k,k):
    print(i, end=" ")'''
'''
symbol=input()
n=int(input())
for i in range(n):
    print(symbol, end=" ")'''
'''a=int(input())
b=int(input())
for i in range(a,b):
    print(i, end=" ")'''
'''Вводим число, пока не введём число 0'''
'''a=int(input())
summa=0
while True:
    a=int(input())
    if a==0: break
    summa+=a
print(summa)'''
'''count=0
summ=0
while True:
    mark==int(input())
    if mark==0: break
    if 2<=mark<=5:
       count+=1
       summ+=mark
    else: print("некорректная оценка")
print(summ/count)'''
'''import random
for i in range(10):
print(random.randint(1,9), end=" ")'''
import random
a=random.randint(1,99)
while True:
     n=int(input())
     if n==0: break
     if (n==a):
         print("good")
         break
     elif(n<a):
         print("n<загаданного")
     elif(n>a):
         print("n<загаданного")




