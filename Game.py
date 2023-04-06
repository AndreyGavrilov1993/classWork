import random
#заставка
print('''
--------------------
----- NEW YEAR -----
------- game -------
--------------------
''')
#знакомство
name=input("Введите своё имя: ")
s=name[len(name)-1]
if s=="а" or s=="я":
    print("Добрый день уважаемая,",name)
else: print("Добрый день уважаемый,",name)
#определение кол-ва жизней
input("Нажмите ввод чтобы бросить кубик")
lives=random.randint(1,6)
if 1<=lives<=2:
    print("Выживает сильнейший.")
elif 3<=lives<=4:
    print("Не много ни мало.")
else:
    print("Сегодня ваш день.")
print("У вас",lives,end=" ")
if lives==1: print("жизнь")
elif 5<=lives<=6: print("жизней")
else: print("жизни")

#новогодняя викторина
print("Ответьте на вопросы")
counter=0
q=input("2023 год - год кого по китайскому календарю?").upper()
if q=="КРОЛИКА" or q=="КРОЛИК" or q=="ЗАЯЦ" or q=="ЗАЙЦА":
    print("верно")
    counter+=1
else: print("не верно")
q=int(input("Какого числа наступит китайский новый год?")).upper()
if q=="22 ЯНВАРЯ" or q=="22" or q=="22ЯНВАРЯ":
    print("верно")
    counter+=1
else:
    print("не верно")
q=input("Какой цвет нельзя одевать на нг 2023 (белый, серый, красный?").upper()
if q=="КРАСНЫЙ":
    print("верно")
    counter+=1
else:
    print("не верно")
q=(input("Как будет по английски новый год?")).upper()
if q=="NEW YEAR":
    print("верно")
    counter+=1
else:
    print("не верно")
q=input("Существует ли Дед Мороз?").upper()
if q=="ДА":
    print("верно")
    counter+=1
else:
    print("не верно")
#результаты викторины
if counter<3:
    print("викторина провалена. Вы дали менее трёх правильных ответов. У вас минус одна жизнь.")
    lives-=1
elif counter==5:
    print("вы знаете всё про этот новый год. У вас плюс одна жизнь")
    lives+=1

if lives==0:
    print("вы проиграли")
    input()
    exit()
#Mortal Combat with Snowmans
hp=lives
defence=0
power=0
for i in range (10):
    v=input(f"У вас {10-i} очков хараткеристик.\nВведите 1-hp 2-power 3-defence")
    if v=="1": hp+=1
    elif v=="2": power+=1
    elif v=="3": defence+=1
    else:
        print("ошибка ввода")
        i-=1
print(f"ваши хароактеристики:\nжизней: {hp}, сила: {power}, защита: {defence}")
# холод>вода, вода>огонь, огонь<холод
hp_mob=3
power_mob=3
defence_mob=3

for i in range(3):
    while hp_mob>0:
        mob=random.randint(1,3)
        player=input("1-вода 2-огонь 3-лёд")
        if mob==1 and player=="2" or mob==2 and player=="3" or mob==3 and player=="1":
            print("Вас атакуют:")
            difr=(power_mob)-defence;
            if (difr>1):
                hp-=difr
                print(f"у вас отняли {difr} здоровья")
            else:
                 hp-=1
                 print(f"у вас отняли 1 здоровье")
            if lives == 0:
                print("вы проиграли")
                input()
                exit()
        if player=="1" and mob==2 or player=="2" and mob==3 or player=="3" and mob==1:
            print("Вы атакуете:")
            difr=(power)-defence_mob;
            if (difr>1):
                hp_mob-=difr
                print(f"вы отняли {difr} здоровья")
            else:
                hp_mob-=1
                print(f"вы отняли 1 здоровье")
        else:
            print("одинаковая атака. Ничья")
print(f"вы победили {i+1} противника. Следующий противник будет сложнее")
hp_mob+=1
power_mob+=1
defence_mob+=1

hp=lives
defence=0
power=0
for j in range (10):
    v=input(f"У вас {10-j} очков хараткеристик.\nВведите 1-hp 2-power 3-defence")
    if v=="1": hp+=1
    elif v=="2": power+=1
    elif v=="3": defence+=1
    else:
        print("ошибка ввода")
        j-=1
print(f"ваши хароактеристики:\nжизней: {hp}, сила: {power}, защита: {defence}")

print("Вы победили!!! УРА!!! С Новым Годом!!!")