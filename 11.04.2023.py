#!!!Декораторы!!!
# import random
# import time
# #@checkTime
# def checkTime(f):
#     def wrapper(list):
#         start = time.time()
#         f(list)
#         end = time.time() - start
#         print(end)
#     return wrapper
#
# @checkTime
# def headFoo(f):
#     def wrapper():
#         print("head for")
#         f()
#     return wrapper
#
# @checkTime
# def foo1(array):
#     start = time.time()
#     for i in array:
#         print(i, end=" ")
#     print()
#     end = time.time()-start
#     print(end)
#
# @checkTime
# def foo2(array):
#     start = time.time()
#     for i in range(0, len(array), 2):
#         print(array[i], end=" ")
#     print()
#     end = time.time() - start
#     print(end)
#
# if __name__=='__main__':
#
#     list=[random.randint(1,9) for i in range (10000)]
#     f1 = foo1(list)
#     f2 = foo2(list)
    # foo1(list)
    # foo2(list)
    #
    # f1_time = checkTime(foo1)
    # f2_time = checkTime(foo2)
    #
    # f1_time()
    # f2_time()


# def hashMode(f):
#     def wrapper(self):
#         print("hash:", self.__hash__())
#         f(self)
#     return wrapper
#
# class Student():
#     def __init__(self, name, group):
#         self.__name = name
#         self.__group = group
#
#     @hashMode
#     def show(self):
#         print(self.__name, self.__group)
#
# if __name__ == '__main__':
#     st1 = Student("Fred", "AMO12")
#     st2 = Student("Adel", "SXF22")
#     st1.show()
#     st2.show()


# import math
# from abc import ABC, abstractmethod
#
#     def counter():
# class Figure(ABC):

#     @abstractmethod
#     def getS(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
# class Circle(Figure):
#     def __init__(self, R):
#         self.__radius = R
#     def getS(self):
#         return math.pi*self.__radius**2
#     def draw(self):
#         print("circle")
#
# class Rectangle(Figure):
#     def __init__(self, w, h):
#         self.__width = w
#         self.__height = h
#
#     def getS(self):
#         return self.__height*self.__width
#     def draw(self):
#         print("rectangle")
#
# if __name__=='__main__':
#     fig1 = Rectangle(2,3)
#     fig2 = Circle(3)
#     fig1.draw()
#     print(fig1.getS())
#     fig2.draw()
#     print(fig2.getS())
#     # fig3=Figure]


# counter=0
# class Student:
#     def __init__(self, name):
#         self.name=name
#         Student.counter()
#     @staticmethod
#     def counter():
#         global counter
#         counter+=1
#
# if __name__=='__main__':
#     st1 = Student("Ivan")
#     st2 = Student("Ivan2")
#     st3 = Student("Ivan3")
#     Student.counter()
#     st1.counter()
#     st2.counter()
#     st3.counter()
#     print(counter)


# import math
# from abc import ABC, abstractmethod
# counter=0
#
# class Figure(ABC):
#     @staticmethod
#     @abstractmethod
#     def getS(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
# class Circle(Figure):
#     def __init__(self, R):
#         self.__radius = R
#     def getS(self):
#         return math.pi*self.__radius**2
#     def draw(self):
#         print("circle")
#
# class Rectangle(Figure):
#     def __init__(self, w, h):
#         self.__width = w
#         self.__height = h
#
#     def getS(self):
#         return self.__height*self.__width
#     def draw(self):
#         print("rectangle")
#
# if __name__=='__main__':
#     fig1 = Rectangle(2,3)
#     fig2 = Circle(3)
#     fig1.draw()
#     print(fig1.getS())
#     fig2.draw()
#     print(fig2.getS())
#     # fig3=Figure]

def hashMode(f):
     def wrapper(self):
         print("помыть:", self.__hash__())
         f(self)
     return wrapper

from abc import ABC
class Vegetable(ABC):
    @abstractmethod
    def __init__(self, wash, coock):
        self.__wash=wash
        self.__coock=coock
    @abstractmethod
    def get(self):
        pass


class Tomatoes(Vegetable):
    def __init__(self, weight):
        self.__weight = weight
        return self.__weight

class Cucumbers(Vegetable):
    def __init__(self, weight):
        self.__weight = weight
        return self.__weight

if __name__=='__main__':
    v1 = Tomatoes("gg")
