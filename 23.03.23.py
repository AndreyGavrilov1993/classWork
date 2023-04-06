# import first
# import second
#
# # print("main")
# # print(first.summ(2,3))
# if __name__=='__main__':
#     print(first.summ(2,3))
#     print(second.dif(2,3))
#     print(__name__)

# def summ(a,b):
#     return a+b
#
# print(summ(2,3))
# result=summ(3,4)
# print(result)

# result2=lambda x:x**2
#
# print(result2(2))

# result2=lambda a,b:a+b
#
# print(result2(2,3))

# maximum=lambda a,b: a if a>b else b
#
# print(maximum(2,3))

# list1=list(range(10))
# print(list1)
# print(list(filter(lambda x:x%2==0, list1)))
#
# a=3
# b=5
# c=8
# a.real()

# class Student:
#     name='noname'
#     group='0'
#
#     def show_info(self):
#         print(f'name {self.name} | group {self.group}')
#
# st1 = Student()
# st1.name="Alex"
# st1.group="3A"
# st1.show_info()

# class Car:
#
#     def __init__(self,color,model):
#         self.model = model
#         self.color = color
#
#     def show_info(self):
#         print(f'model {self.model} : color {self.color}')
#
#     def set_color(self,color):
#         self.color=color
#
# car1 = Car("red","Toyota")
# car1.show_info()
# car1.set_color("red")
# # car1.show_info()
# car1.show_info()

class Employee:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def show_info(self):
        print(f'name {self.name} : phone {self.phone}')

    def dif_info(self,name,phone):
        self.name=name
        self.phone=phone

emp1 = Employee("Alex","89198989438")
emp1.show_info()
emp1.dif_info("Wesker","88998786735")
emp1.show_info()