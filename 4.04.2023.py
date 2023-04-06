# class Human():
#     def __init__(self, name):
#         self._name=name
#     def get_name(self):
#         return self._name
# class Student(Human):
#     def __init__(self, name, group, avg):
#         super().__init__(name)
#         self.__group=group
#         self.__avg=avg
#
# class ExcellentStudent(Student):
#     def __init__(self, name, group, avg, stipend):
#         super().__init__(name, group, avg)
#         self.stipend=stipend
#
# class Sportsmen(Student):
#     def training(self):
#         print(self._name, " training")
#
# class Worker(Human):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self._salary=salary
#
# class Director(Worker):
#     def manage(self):
#         print(self._name, "manage")
#
# class Curator(Worker):
#     def __int__(self, name, salary, group):
#         super().__init__(name, salary)
#         self._group=group
#     def checkHW(self):
#         print(self._name, "check HW")
#
# if __name__=="__main__":
#
#  student1 = Student("Ivan","5A", 4.3)
#  print(student1.get_name())
#  student3 = Sportsmen("Tom","60",4.4)
#  student3.training()
#  print(student3._name)


import random

class Student():
    def __init__(self, name, group):
        self.__name=name
        self.__group=group
    def info(self):
        print(self.__name , " : ", self.__group)
class Group(Student):
    def __init__(self, group_name):
        self._group_name=group_name
        __students_list=[]
    def add_students(self, list):
        self.__students_list=list
    def show_info(self):
        print(self.__group_name," : ")
        for i in self.__students_list:
            i.info()


if __name__=="__main__":
    students_list=[]
    names = ('Павел','Мария','Катя','Лиля','Ярик')
    groups = ('5А', '3В', '4А')
    count=int(input("input count of students: "))
    for i in range(count):
     students_list.append(Student(random.choice(list(names)),random.choice(list(groups))))

    for i in students_list:
        i.info()
        # print(i.get_name())
        # print(i.get._group)

   group1=Group(random.choice(list(groups)))
   group1.add_students(students_list)
   group1.info()
