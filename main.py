# def ploshad_kruga(radius):
#     return 3.14*radius**2
# radius = float(input("Введите радиус круга: "))
# print(ploshad_kruga(radius))
#
#
# def chislo_v_stepeni(chislo, stepen):
#     return chislo**stepen
# chislo = float(input("Введите число: "))
# stepen = float(input("Введите степень числа: "))
# print(chislo_v_stepeni(chislo, stepen))
#
#
from random import randint
# spisok = []
# for q in range(5):
#     spisok.append(randint(1,100))
# print(spisok)
# def spisok_v_elementi(spisok):
#     for w in spisok:
#         print(w)
# spisok_v_elementi(spisok)


spisok2 = []
for a in range(5):
    spisok2.append(randint(-1000, 1000))
print(spisok2)
def max_spisok(spisok2):
    chislo1 =spisok2[0]
    for s in spisok2:
        if s > chislo1:
            chislo1 = s
    return chislo1
print(max_spisok(spisok2))