#Вложенные списки
'''students=[[3,4,3,3],[4,4,3,4],[4,5,4,5]]
print(students)
print(students[0])
print(students[0][0])'''
#Матрица
'''students=[[3,4,3,3],[4,4,3,4],[4,5,4,5]]
print("\t\t\t\t|рус\t\t|англ\t\t\t|мат\t\t\t|физ.")
for i in range (len(students)):
    print(f"студент {i+1}-й\t", end=" ")
    for j in range (len(students[i])):
        print(f"| {students[i][j]}\t\t", end=" ")
    print()

summ=0
count=0
for i in students:
    for j in i:
        count+=1
        summ+=j
        print(j, end=" ")
    print()
print(summ)
print(summ/count)'''
'''profit=[[5000,4500,3000,4200],
        [5000,4200,3700,6600],
        [7000,3200,6000,9000]]
print("\t\t\t|I\t\t|II\t\t|III\t|IV")
min_profit=profit[0][0]
max_profit=profit[0][0]

min_num=1
min_emp=1
max_num=1
max_emp=1

for i in range (len(profit)):
    summ=0
    print(f"{i+1} employee:\t", end="")
    for j in range (len(profit[i])):
        if min_profit>profit[i][j]:
            min_profit=profit[i][j]
            min_num=j+1
            min_emp=i+1
        if max_profit<profit[i][j]:
            max_profit=profit[i][j]
            max_num=i+1
            max_emp=j+1
        summ+=profit[i][j]
        print(f"| {profit[i][j]}\t", end="")
    print(f"|| {summ}")
print("\t\t\t", end="")
result=0
for j in range (len(profit[0])):
    summ=0
    for i in range (len(profit)):
        summ+=profit[i][j]
    print(f"| {summ}\t", end="")
    result+=summ
print(f"|| {result}")

print(f"max_profit: {max_profit} num:{max_num} | employee:{max_emp}")
print(f"min_profit: {min_profit} num:{min_num} | employee:{min_emp}")'''
'''import random
array=[]

size1=int(input("height: "))
size2=int(input("width: "))

for i in range(size1):
    array.append([])
    for j in range(size2):
        array[i].append(random.randint(10,99))
        print(array[i][j], end=" ")
    print()'''
import random
import math

size=16
list1=[]
for i in range(size):
    list1.append(random.randint(10,99))
print(list1)

size2=math.ceil(size**0.5)
array=[]

k=0
for i in range (size2):
    array.append([])
    for j in range (size2):
        try:
          array[i].append(list1[k])
          k+=1
        except:
            array[i].append(0)
        print(array[i][j], end="\t")
    print()
