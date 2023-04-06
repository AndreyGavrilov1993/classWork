# import random
#
# def create_list(n):
#     list=[]
#     for i in range(n):
#         list.append(random.randint(10,99))
#     return list
#
# list2=[random.randint(10,99) for i in range (10)]
# print(list2)
#
# list=create_list(10)
# print(list)

import random

def bubble_sort(list):
    counter=0
    for j in range(len(list)-1):
      flag=True
      for i in range(len(list)-1-j):
        counter+=1
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
            flag=False
      if flag:break


list=[random.randint(10,99) for i in range (10)]
print(list)
bubble_sort(list)
print(list)

def bubble_sort_bad(list):
    counter=0
    for j in range(len(list)-1):
     flag=True
     for i in range(len(list)-1-j):
        counter+=1
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
            flag=False
     if flag:break
    return counter

def shaker_sort(list):
    counter=0
    min=0
    max=len(list)-1
    while min<max:
     flag=True
     for i in range(max):
         counter+=1
         if (list[i]>list[i+1]):
            list[i],list[i+1]=list[i+1],list[i]
            flag=False
     if (not flag):
       max-=1
       flag=True
       for i in range(max, min, -1):
           counter+=1
           if (list[i]<list[i-1]):
            list[i],list[i-1]=list[i-1],list[i]
            Flag=False
       min+=1
       if flag: break
     return counter

def isertion_sort(list):
    counter=0
    for i in range(1,len(list)):
        for j in range(i, 0, -1):
         counter+=1
         if (list[j]<list[j-1]):
          list[j],list[j-1]=list[j-1],list[j]
        else:
         break
    return counter

def selection_sort(list):
    counter=0
    for i in range(len(list)-1):
        min=list[i]
        minIndex=i
        for j in range(i, len(list)):
            counter+=1
            if (min>list[j]):
                min=list[j]
                minIndex=j
        list[i], list[minIndex]=list[minIndex], list[i]
    return counter


list=[random.randint(10,99) for i in range (10)]
print(list)
list2=list.copy()
list3=list.copy()
list4=list.copy()
list5=list.copy()
list6=list.copy()
print("bubble_sort")
print(bubble_sort(list2))
print(list2)
print("bubble_sort_bad")
print(bubble_sort_bad(list3))
print(list3)
print("shaker_sort")
print(shaker_sort(list4))
print(list4)
print("isertion_sort")
print(isertion_sort(list5))
print(list5)
print("selection_sort")
print(selection_sort(list6))
print(list6)