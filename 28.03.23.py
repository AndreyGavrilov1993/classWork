# class Cat:
#     def __init__(self,name):
#         self.name=name
#         print(f'create {self.name} : {self}')
#
#     def __del__(self):
#         print(f'remove {self.name} : {self}')
#
#     def show(self):
#         print(self.name)
#
# if __name__=="__main__":
#     cat1 = Cat("Tom")
#     cat2 = Cat("Kuzma")
#
#     cat1.show()
#     cat2.show()
#     del(cat2)




#     name = "Noname"
#     weight = '6'
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#      # print(f'name {self.name} | weight {self.weight}')
#     def sleep(self):
#         print(f'cat2 {self.name}')
# cat1=Cat()
# cat1.name='cat1'
# cat1.weight='7'
# cat2=Cat("cat2",'3')
# cat2.sleep='7'


# class Drob:
#     def __init__(self, unit, num, denum):
#         self.unit = unit + num//denum
#         self.num = num%denum
#         self.denum = denum
#
#     def summ(self,drob2):
#         num1=self.num+self.denum*self.unit
#         num2=drob2.num+drob2.denum*drob2.unit
#         result_num = num1*drob2.denum+num2*self.denum
#         result_denum = self.denum*drob2.denum
#         result_unit = result_num//result_denum
#         result_num %= result_denum
#         return (f'{result_unit} {result_num} / {result_denum}')
#
#     def show(self):
#         print(f'{self.unit} {self.num} / {self.denum}')
#
# drob1 = Drob(2,3,5)
# drob2 = Drob(1,8,3)
# drob1.show()
# drob2.show()
# print(drob1.summ(drob2))

class Tovar:
    def __init__(self, price, type):
        self.price=price
        self.type=type
class Magazine:
    list=[]
    pribil=0
    def __init__(self, budget):
        self.budget=budget

    def buy(self,tovar):
        if (self.budget>=tovar.price):
            self.list.append(tovar)
            self.budget-=tovar.price
        else: print("no money no money")

    def sell(self,type):
        for i in self.list:
            if type == i.type:
                self.pribil+=(i.price*2.2).__round__()
                self.list.remove(i)

mag1 = Magazine(2000)
tovar1 = Tovar(100, "chips")
tovar2 = Tovar(30, "potato")
tovar3 = Tovar(100, "tomato")

for i in range (3): mag1.buy(tovar1)
mag1.sell(tovar2)
mag1.buy(tovar3)

mag1.sell("ships")
mag1.sell("potato")
mag1.sell("ships")

print(mag1.budget)
print(mag1.pribil)