'''b1=int(input("input start: "))
e1=int(input("input end: "))
if e1>b1: e1,b1=b1,e1
while b1>=e1:
    print(b1)
    b1-=1'''
'''a=int(input("input: "))
count=1
while count<=a:
    print(count, end=" ")
    count+=1'''
'''b1=int(input("input: "))
n=int(input("count str: "))
while (n>0):
    count=b1
    while 1<=count:
        print(count, end=" ")
        count-=1
    n-=1
    print()'''
'''column=int(input("input column: "))
row=int(input("count row: "))
n=1
while (row>0):
    count=column
    while count>0:
        print(n, end="\t")
        count-=1
        n+=1
    row-=1
    print()'''
'''size=int(input())
s=input()
n=size
while (n>0):
    k=size
    while(k>0):
        print(s, end=" ")
        k-=1
    n-=1
    print()'''
'''size=int(input())
s=input()
n=1
while(n>0):
    k=size
    while(k>0):
        if (k=0 or k==size or n=1 or n=size)
            print(s, end=" ")
        else:
            print(" ",end=" ")
        k-=1
    n-=1
    print()'''
'''n1=int(input())
n2=input()
a=1
while (a<10):
    print(1,"*",a,"=",1*a)
    a+=1'''
n1=int(input())
n2=input()
a=1
while (a<10):
    b=1
    while(b<10):
        print(b,"*",a,"=",b*a, end="\t")
        b+=1
    a+=1
    print()
