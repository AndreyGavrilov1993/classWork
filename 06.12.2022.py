'''a=int(input("введите число"))

>
<
>=
<=
=='''
'''
if a>0:
    print("число положительное")
else:
    print("число отрицательное")'''
'''
a=int(input("введите число"))
if a==0:
    print("0")
elif a%2==0:
    print("чётное число")
else:
    print("нечётное число")'''
'''
if a=="a":
    print("a")
elif a=="b":
    print("b")
else:
    print("else")'''
'''
a=int(input("введите число: "))
b=int(input("введите число: "))
if a>b:
    print(a,">",b)
elif a<b:
    print(a,"<",b)
else:
    print(a,"=",b)'''
'''
city=input("введите столицу России: ")
if city=="Москва":
    print("верно")
    if city=="москва":
    print("верно")    
else:
    print("неверно")'''
'''
a=int(input("введите 1-е число: "))
b=int(input("введите 2-е число: "))
summ=int(input("введите сумму: "+str(a)+"+"+str(b)+"="))
if summ==a+b:
    print("верно")
else:
    print("не верно")'''
'''
a=int(input("введите 1-е число: "))
b=int(input("введите 2-е число: "))
op=input("введите операцию: ")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="sr":
    print((a+b)/2)
else:
    print("такой команды нет")'''
'''
begin=int(input("введите начало диапазона: "))
end=int(input("введите конец диапазона: "))
n=int(input("введите число: "))
   if begin<=n<=end: print("yes")
   else:
       print("no")'''
sec=int(input("введите время в секундах: "))
reg=input("введите h/m/s")
if reg=="h":
    print(((60*60*12)-sec)//3600)
elif reg=="m":
    print(((60*60*12)-sec)//60)
elif reg =="s":
    print(((60 * 60 * 12) - sec))