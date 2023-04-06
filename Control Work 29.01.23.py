#Part 1
#1
'''a=int(input("Введите 1е число: "))
b=int(input("Введите 2е число: "))
c=int(input("Введите 3е число: "))
d=int(input("Введите 4е число: "))
if a>b and a>c and a>d:
    print("максимум=a")
elif  b>c and b>d:
    print("максимум=b")
elif  c>d:
    print("максимум=c")
else:
    print("максимум=d")

#2
'''a=int(input("Введите начало диапазона: "))
b=int(input("Введите конец диапазона: "))
for i in range (a,b+1):
        print(i, end=" ")
    print()'''
#3
'''size=int(input("input size side: "))
for j in range (size):
   print("* "*size)'''
#4
'''count=1
for i in range(40,85+1):
    count*=i
print(count)
'''
#5
'''import random
list=list(range(1,10))
for i in (list):
print(list)
'''
#6
'''import random
list=list(range(1,10+1))
for i in (list):
 print(list)
 print((sum(list))/2, end=" ")
print()'''

#Part 2
#1
text="Создать спосок из 10 элементов. Заполнить его случайными целыми числами в диапазоне."
count=0
list=list(text)
for i in list:
 if i==" ":
    count+=1
 elif i==text.isdigit():
   count-=1
 print(count,"слов")
#2
'''list=[]
list1=len(list[])
if list1=="стоп":
    break
    print(list)
print(summ(list))'''
#3
'''list1=["form", "apple", "orange", "icecream", "chocolate", "egg", "limon", "elephant", "potate", "monkey"]
list2=["form", "elephant", "monkey"]
print(list1.remove["form", "elephant", "monkey"])
print(list1)
print(list2)'''
'''