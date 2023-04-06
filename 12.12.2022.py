#Пользователь вводит доход фирмы за первые 3 месяца, янв. февраль, март и вводит годовой доход. Необходимо определить доход за квартал меньше или больше.
'''jan=int(input("введите доход за январь: "))
feb=int(input("введите доход за февраль: "))
mar=int(input("введите доход за март: "))
year=int(input("введите годовой доход:"))
if year/4>(jan+feb+mar): print("доход за первый квартал меньше среднего дохода")
elif year/4<(jan+feb+mar): print("доход за первый квартал больше среднего дохода")
else: print("доход за первый квартал равен среднему доходу")'''
'''
name=input("введите своё имя:")
n=int(input("введите количество повторений имени: "))
print(name*n)'''
'''
name=input("введите своё имя:")
n=int(input("введите количество повторений имени: "))
counter=0
while(counter<n):
    print(name, end=" ")
    counter+=1'''
'''
n=int(input("введите число:"))
counter=0
while counter<n:
    print(counter, end="")
    counter+=1'''
'''
a=int(input("введите первое число: "))
b=int(input("введите второе число: "))
if a>b: a,b=b,a
while a<=b:
    print(a)
    a+=1'''
'''a=int(input("введите число"))
while a<0:
    print(a)
    a+=1
    while a>=0:
        print(a)
        a-=1'''
'''
n=int(input("введите число"))
counter=2
while counter<=n:
    print(counter)
    counter+=2'''
'''
n=int(input("введите число"))
counter=2
if n<0:
    counter=-2
while counter<=n:
    print(counter)
    n+=2
else:
    counter = 2
while counter <= n:
    print(counter)
    counter += 2'''
'''
a=int(input("введите число"))
if a<0:
    counter=-2
    k=-2
else:
    counter=2
    k=2
while abs(counter)<=abs(a):
    print(counter)
    counter+=k'''
'''
a=int(input("введите число: "))
summa=0
while a>0:
    summa+=a
    a-=1
    print(summa)'''
'''
a=int(input("введите начало диапазона: "))
b=int(input("введите конец диапазона: "))
if a>b: a,b=b,a
if a%2: a+=1
while a<=b:
    print(a)
    a+=2'''
'''a1=int(input("введите начало 1-го диапазона: "))
b1=int(input("введите конец 1-го диапазона: "))
a2=int(input("введите начало 2-го диапазона: "))
b2=int(input("введите конец 2-го диапазона: "))
if a1>b1: a1,b1=b1,a1
if a2>b2: a2,b2=b2,a2
if a1<a2: min=a1
else: min=a2
if b1>b2: max=b1
else: max=b2
while min<=max:
  if a1<=min<=b1 and a2<=min<=b2:
    print(min)
    min+=1'''
n=int(input("введите число: "))
result=1
k=2
while (k<=n):
    result*=k
    k+=1
    print(result)



