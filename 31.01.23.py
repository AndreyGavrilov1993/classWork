'''def show_line():
    print("-------------")

show_line()
print("hdkjhdhj")
for i in range(5):
    print(i)
show_line()
print("hdkjhkuyyuhj")
for i in range(25):
    print(i)
show_line()
print("hgfjhkjhkh")
for i in range(15):
    print(i)
show_line()
print("k,jkghkhjhj")
for i in range(5):
    print(i)'''

'''def show_cube():
    for i in range(5):
        print("* "*5)

num=int(input())

for i in range(num):
    print(i)
    show_cube()'''

'''def show_cube(n):
    for i in range(n):
        print("* "*n)

num=int(input())

for i in range(num):
    print(i)
    show_cube(3)'''

'''def maximum(a,b,c,d):
    max=a
    if max<b: max=b
    if max<c: max<c
    if max<d: max<d
    print(max)'''

#2

'''def num(a,b):
    a=int(input())
    b=int(input())
    if a%2==0: a+=1
    for i in range(a,b+1, 2):
            print(i)

num(1,9)'''

#3
'''def show_line(lenght, side, symbol):
    if side:
        print(symbol*lenght)
    else:
        for i in range(lenght):
            print("\t"+symbol)

show_line(4, False, "*")'''

#4
def show_rectangle(row, column):
    print("* "*column)
    for o in range(row-2):
        print("* "+" "*(column-2)+"*")
    print("* "*column)

'''    for i in range(row):
        for j in range(column):
            if i==0 or i==row-1 or j==0 or j==column-1:
                print("* ",end=" ")
            else: print("  ",end=" ")
        print()'''

show_rectangle(3,9)