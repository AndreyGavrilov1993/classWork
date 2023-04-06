# a=8
#
# def foo():
#     global a
#     a+=1
#     print(a)
#
# foo()
# print(a)

# a=6
# b=8
#
# def foo(a,b):
#     print(a)
#     if a<b:
#      foo(a+1,b)
#     print(a)
#
# foo(a,b)
# a=6
# b=8
#
# def foo(a,b):
#     print(a)
#     if a<b:
#      foo(a+1,b)
#     print(a)
#
# foo(a,b)
#
# def foo2(a):
#     if (a>=0):
#         print(a)
#         foo2(a-1)

# a=6
# b=8
#
# def summ(a,b):
#     if(a==b): return b
#     return (summ(a,b-1)+b)
#
# print(summ(a,b))

# a=4
#
# def factorial(a):
#     if (a<0): return 0
#     if (a==1): return 1
#     else: return factorial (a-1)*a
#
# print(factorial(5))

# def show_list(list, i=0):
#     if (i<len(list)):
#         print(list[i], end=" ")
#         show_list(list, i+1)
# list=[14,234,67,3,9]
# show_list(list)

# def show_list(list, i=0):
#     if (i<len(list)):
#         show_list(list, i+1)
#         print(list[i], end=" ")
# list=[14,234,67,3,9]
# show_list(list)

# def show_list(list, i=0):
#     if (i<len(list)):
#         print(list[len(list)-1-i], end=" ")
#         show_list(list, i+1)
# list=[14,234,67,3,9]
# show_list(list)

#Бинарный поиск

# def binary_search(list, n, min=0, max=0, flag=False):
#                 if (flag): max=len(list)-1
#                 index=(min+max)//2
#                 if(min>max): return -1
#                 elif (n>list[index]):
#                     return binary_search(list, n, index+1, max, False)
#                 elif (n<list[index]):
#                     return binary_search(list, n, min, index-1, False)
#                 else:
#                     return index
#
# # list=generate_list(12, 1, 100)
# # list.sort()
# # print(list)
# list=[1,3,6,9,24,36,57,78,86,99]
# print(list)
#
# print(binary_search(list,86))

def recursive_list(list, n, summ, min, max, flag=False):
    if summ=0: max=len(list)-1
        index=0
    if(min>max): return -1
    elif (n)
    list=[4,1,3,4,2,1,0,9,6]
    print(list)