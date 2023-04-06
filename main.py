# chislo1 = int(input("Введите целое число: "))
# if chislo1 > 0:
#     print(chislo1, "больше 0")
# elif chislo1 < 0:
#     print(chislo1, "меньше 0")
# else:
#     print(chislo1, "= 0")



# chislo2 = int(input("Введите целое число: "))
# if chislo2 % 2 == 1:
#     print(chislo2, "нечетное")
# else:
#     print(chislo2, "четное")



# chislo3 = int(input("Введите целое число: "))
# chislo4 = int(input("Введите целое число: "))
# if (chislo3 > 2) and (chislo4 <= 3):
#     print("Истина")
# else:
#     print("Ложь")



# chislo5 = int(input("Введите целое число: "))
# chislo6 = int(input("Введите целое число: "))
# chislo7 = int(input("Введите целое число: "))
# if (chislo5 < chislo6) and (chislo6 < chislo7):
#     print("Истина")
# else:
#     print("Ложь")



# chislo8 = int(input("Введите целое число: "))
# chislo9 = int(input("Введите целое число: "))
# if (chislo8 % 2 == 1) and (chislo9 % 2 == 1):
#     print("Истина")
# else:
#     print("Ложь")



# chislo8 = int(input("Введите целое число: "))
# chislo9 = int(input("Введите целое число: "))
# if (chislo8 % 2 == 1) or (chislo9 % 2 == 1):
#     print("Истина")
# else:
#     print("Ложь")



# chislo10 = int(input("Введите целое число: "))
# if (chislo10 % 2 == 0) and (len(str(chislo10)) == 2):
#     print("Истина")
# else:
#     print("Ложь")



# chislo11 = float(input("Введите число: "))
# chislo12 = float(input("Введите число: "))
# chislo13 = float(input("Введите число: "))
# if (chislo11 < chislo12) and (chislo12 < chislo13):
#     print(3*chislo11, 3*chislo12, 3*chislo13)
# else:
#     if chislo11 < 0:
#         chislo11 = -1 * chislo11
#     if chislo12 < 0:
#         chislo12 = -1 * chislo12
#     if chislo13 < 0:
#         chislo13 = -1 * chislo13
#     print(chislo11,chislo12,chislo13)









chislo14 = float(input("Введите X: "))
chislo15 = float(input("Введите Y: "))
if chislo14 > chislo15:
    print(2 * chislo14 - 3 * chislo15)
else:
    print(3 * chislo14 - 2 * chislo15)



chislo16 = float(input("Введите число: "))
chislo17 = float(input("Введите число: "))
if chislo16 < chislo17:
    print(chislo16)
else:
    print(chislo16*chislo17)



chislo18 = float(input("Введите число: "))
chislo19 = float(input("Введите число: "))
if chislo18 < chislo19:
    chislo20 = chislo18
    chislo18 = (chislo18 + chislo19)/2
    chislo19 = 2*chislo19*chislo20
elif chislo18 > chislo19:
    chislo20 = chislo19
    chislo19 = (chislo19+chislo18)/2
    chislo18 = 2*chislo18*chislo20
print(chislo18, chislo19)