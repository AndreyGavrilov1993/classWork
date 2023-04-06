from random import randint
otrizat = 0
polog = 0
nechet = 0
chet = 0
krat3 = 1
minmax = 1
spisok = []
chislo = int(input("Введите длину списка: "))
for q in range(chislo):
    spisok.append(randint(-100, 100))
print(spisok)
for w in range(0, chislo):
    if spisok[w] < 0:
        otrizat = otrizat+spisok[w]
    elif spisok[w] > 0:
        polog = polog+spisok[w]
    if spisok[w] % 2 == 1:
        nechet = nechet+spisok[w]
    if spisok[w] % 2 == 0:
        chet = chet+spisok[w]
    if w % 3 == 0:
        krat3 = krat3*spisok[w]
    if spisok.index(min(spisok))<spisok.index(max(spisok)):
        for e in range(spisok.index(min(spisok)),spisok.index(max(spisok))):
            minmax = minmax*spisok[e]
    else:
        for e in range(spisok.index(max(spisok)), spisok.index(min(spisok))):
            minmax = minmax * spisok[e]
print("Сумма отрицательных чисел =", otrizat)
print("Сумма положительных чисел =", polog)
print("Сумма нечетных чисел =", nechet)
print("Сумма четных чисел =", chet)
print("Сумма чисел с индексами кратными 3 =", krat3)
print("Произведение чисел между наибольшим и наименьшим =", minmax)