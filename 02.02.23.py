'''def show_line(n):
    print("*"*n)

def show_sr(a,b,c):
    return("Среднее арифметическое: ",(a+b+c)/3)

show_line(4)

print(2,3,4)'''

'''list1=[1,2,3,4,5,6]
n=8
def show_list():
    for i in range (len(list1)):
        print(list1[i],end=" ")

show_list()'''

'''n=int(input())

def foo1():
    global n
    while(n>0):
        print(n)
        n-=1

def foo2():
    global n
    while(n>0):
        print(n)
        n-=1

foo1()
print(n)
foo2()'''

'''list1=[1,2,3,4,5]

def change_list():
    for i in range(len(list1)):
        list1[i]*=2
    print(list1)

change_list()

print(list1)

def foo2(a):
    a=5
    print(a)

def foo3(list):
    list[0]=7
    print(list[0])

a=3
foo2(a)
print(a)

list=[1,2,3]
foo3(list)
print(list[0])'''

#5
'''def summa(min,max):
    if min>max: min,max=max,min
    summ=0
    for i in range(min,max+1):
        summ+=i
    return summ

print(summa(2,6))'''

#6
'''def simple(n):
    for i in range(2,int((n**0.5))+2):
        if(n%i==0): return False
    return True

print(simple(9))'''

#7
'''def magic(num):
    return int(num[0])+int(num[1])+int(num[2])==int(num[3])+int(num[4])+int(num[5])

print(magic("123456"))'''

#8
# def simple_in_range(a,b):
#     for i in range(a,b+1):
#      flag=True
#      for j in range(2,int((i**0.5))+2):
#          if(i%j==0):
#              flag=False
#              break
#     if (flag):print(i,end=" ")
#
# print(simple_in_range(1,9))

'''def simple(n):
    for i in range(2, int((n**0.5))+2):
        if (n%i==0): return False
    return True

def simple_in_range(a,b):
    for i in range(a,b+1):
      if simple(i): print(i,end=" ")

print(simple_in_range(1,9))'''

def create_list():
    list=[]
    count=0
    while(True):
        str=input()
        if str.lower()=="стоп":
            break
        list.append(str)
    return list
def selection_list(list, alp):
    list2=[]
    for i in list:
        if i[0].upper==alp:
            list2.append(i)
    return list2

def show_list(list):
    for i in list:
        print(i, end=" ")

list=create_list()
list2=selection_list(list,'А')

show_list(list)
show_list(list2)

