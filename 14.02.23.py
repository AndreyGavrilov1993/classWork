# import random
# # list1= [random.randint(1,9) for i in range (10)]
# # print(list1)
#
# def isertion_sort(list):
#     for i in range(1,len(list)):
#         for j in range(i, 0 ,-1):
#             if (list1[j]<list1[j-1]):
#                 list1[j],list1[j-1]=list1[j-1],list1[j]
#             else: break
#
# def lineary_search(list,n):
#     count=0
#     for i in list:
#         if i==n: return count
#         count+=1
#     return -1
#
# list= [1, 3, 5, 7, 10, 15, 40, 50, 68]
#
# def binary_search(list, n, min=0, max=0, flag=True):
#     if flag: max=len(list)
#     sr=(min+max)//2
#     if (min>max): return -1
#     if (n>list[sr]):
#         binary_search(list, n, sr+1, max, False)
#     elif (n<list[sr]):
#         binary_search(list, n, min, sr-1, False)
#     else:
#         return sr
#
# list1=[random.randint(1,9) for i in range (10)]
# print(list1)
# isertion_sort(list1)
# print(list1)
# print(list)
# print(lineary_search(list,7))
# print(binary_search(list1,4))

#Кортежи

# list1=[1,2,3,4]
# list2=[1,2,3,4]
# print(list1)
# print(list2)
# list1[0]=34
# print(list2[0])
# print(list1)
# print(list2)

# list1=['a']
# list2=('a',)
# print(list1)
# print(list2)

# list2=tuple("hello word")
#
# print(list2)

# list1='Alex','Sydnie','Tom','Ivan'
# name1, name2, name3, name4 = list1
# print(list1)
# print(name1)
# name1+="a"
# print(name1)
# print(list1)
# print(list1[1])
# print(list1[-1])

# list1='banana', 'apple', 'bananamango', 'mango', 'strawberry-banana', 'apple', 'banana', 'orange'
# def count(list1, word):
#     count=0
#     for i in list1:
#         if i.find(word)!=-1:
#             count+=1
#     return count
#
# print(count(list1,"apple"))

# list1= 'Kevin', 'Alex', 'Miranda'
# list2= 'Pol'
# list3= [1,2,3,4,5]
# list4=*list3,
# print(*list1)
# print(list2)
# print(list3)
# print(list4)

#Срез
# list1=[1,2,3,4,5,6,7]
# list1=list1[0:-2]
# print(list1[0:3])
# print(list1)

list1='merc','ford', 'reno', 'toyota', 'ford', 'mazda', 'bmw', 'toyota'

w1='merc'
w2='marc'

list2=[]
for i in range(len(list1)):
    if list1[i]!=w1:
        list2.append(list1[i])
    else:
        list2.append(w2)
list1=*list2,

print(list1)