# class Student:
#     __name = "Pol"
#
#     def getName(self):
#         return self.__name;
#
# st = Student()
# print(st.getName())


# import random
# class Stack:
#
#     def __init__(self,size):
#      self.__size=size
#      self.__counter=0
#      self.__list=['' for i in range(size)]
#
#     def size(self):
#         return self.__counter
#
#     def show(self):
#         # print("[",end=" ")
#         # for i in range(self.__counter-1):
#         #     print(self.__list[i],end=", ")
#         # print(self.__list[self.__counter],"]")
#         print(self.__list[:self.__counter:])
#
#     def push(self, n):
#         if self.__counter==self.__size:
#             raise IndexError('list index out of range')
#         else:
#             self.__list[self.__counter] = n
#             self.__counter+=1
#     def pop(self):
#          if self.__counter==0:
#              raise IndexError('list is empty')
#          else:
#              self.__counter-=1
#
#
#
# if __name__=="__main__":
#  try:
#   stack1 = Stack(4)
#   stack1.show()
#   print(stack1.size())
#   for i in range(7):
#       stack1.push(random.randint(1,9))
#   stack1.show()
#   print(stack1.size())
#   for i in range(2):
#       stack1.pop()
#   stack1.show()
#   print(stack1.size())
#   for i in range(2):
#       stack1.pop()
#   stack1.show()
#  except Exception as er:
#     print(er)

import random
class Queue:
    def __init__(self,size):
        self.__size=size
        self.__counter=0
        self.__list=['' for i in range(9)]

    def size(self):
        return self.__counter
    def show(self):
        # print("[",end=" ")
        # for i in range(self.__counter-1):
        #     print(self.__list[i],end=", ")
        # print(self.__list[self.__counter],"]")
        print(self.__list[:self.__counter:])
    def push(self, n):
        if self.__counter==self.__size:
            raise IndexError('List index out of range')
        else:
            self.__list[self.__counter] = n
            self.__counter+=1
    def __pop__(self):
        if self.__counter==0:
            raise IndexError('List is empty')
        else:
            for i in range(self.__counter-1):
                self.__list[i]=self.__list[i+1]
            self.__counter-=1

if __name__=="__main__":
    try:
        queue1 = Queue(9)
        queue1.show()
        print(queue1.size())
        for i in range(7):
            queue1.push(random.randint(1,9))
        queue1.show()
        print(queue1.size())
        for i in range(2):
            queue1.__pop__()
        queue1.show()
        print(queue1.size())
        for i in range(2):
            queue1.__pop__()
        queue1.show()
    except Exception as er:
        print(er)

