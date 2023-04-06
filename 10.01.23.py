#Строки
'''
line="Вася Петров"
for i in range(len(line)):
    print(line[i], end=" ")'''
'''line="В лингвистике: письменная или звучащая речь, которая внутренне организована и относительно закончена."
line2=""
counter=1 if(line!="") else 0

for i in range (len(line)):
    if (line[i]==" "): counter+=1
    elif line[i]=="-": counter-=1
if line[len(line)-1]==" ": counter-=1
print(counter)'''
#Программа которая преобразует число, введённое пользователем в текст.
'''num=input("Введите вдухзначное число: ")
if len(num)==2:
if num[0] == "1":
    if num[1] == "0": print("десять", end=" ")
    if num[1] == "1": print("одиннадцать")
    if num[1] == "2": print("двенадцать")
    if num[1] == "3": print("тренадцать")
    if num[1] == "4": print("четырнадцать")
    if num[1] == "5": print("пятнадцать")
    if num[1] == "6": print("шестнадцать")
    if num[1] == "7": print("семьнадцать")
    if num[1] == "8": print("восемьнадцать")
    if num[1] == "9": print("девятнадцать")
else:
    if num[0]  == "2": print("двадцать", end=" ")
    elif num[0]  == "3": print("тридцать", end=" ")
    elif num[0]  == "4": print("сорок", end=" ")
    elif num[0]  == "5": print("пятьдесят", end=" ")
    elif num[0]  == "6": print("шестьдесят", end=" ")
    elif num[0]  == "7": print("семьдесят", end=" ")
    elif num[0]  == "8": print("восемьдесят", end=" ")
    elif num[0]  == "9": print("девяносто", end=" ")

if num[1]=="1": print("один")
elif num[1]=="2": print("два")
elif num[1]=="3": print("три")
elif num[1]=="4": print("четыре")
elif num[1]=="5": print("пять")
elif num[1]=="6": print("шесть")
elif num[1]=="7": print("семь")
elif num[1]=="8": print("восемь")
elif num[1]=="9": print("девять")
else:
 if num[0]=="1": 
  print("один")
 elif num[0]=="2":
  print("два")
 elif num[0]=="3":
  print("три")
 elif num[0]=="4":
  print("четыре")
 elif num[0]=="5":
  print("пять")
 elif num[0]=="6": 
  print("шесть")
 elif num[0]=="7":
  print("семь")
 elif num[0]=="8":
  print("восемь")
 elif num[0]=="9":
  print("девять")'''
'''line=""
while True:
 name=input("Введите имя: ")
    if name.lower()=="конец": break
    line+=name+" "
 print(line)   '''
'''line= "Он родился в 1992 году."
counter=0
for i in range(len(line)):
 if line[i].isdigit():
    counter+=1
print(counter)'''
#Посчитайте кол-во строк
'''line='''
'''
Мпоапо апра пр  вр а
апрапв 
парар
пвоо
рараоаые
ыыекеу'''
'''
counter=0;
for i in range(len(line)):
    if line[i]=="\n": counter+=1
print(counter)'''
# Пользователь вводит строку и символ, посчитать сколько раз символ встречается в данной строке.
'''line=input("Введите строку: ")
symbol=input("Введите символ: ")
counter=0
for i in range (len(line)):
    if line[i]==symbol: counter+=1
print(counter)

counter2=0
for i in line:
    if i==symbol: counter2+=1
    print(counter2)'''
'''line="Папа папрапа парапар"
symbol="a"
for i in line:
    print(i, end=" ")'''
'''line="Папа папрапа парапар"
symbol="a"
counter=0
for i in line:
    if i.isalpha(): counter+=1
print(counter)'''
'''line="додо папа мама вася деда катя жена папа"
line2="мама"

print(line.find(line2,0,len(line)-1))'''
line=input("Введите строку: ")
line2=input("Введите слово: ")
if line.find(line2)==-1: print(0)
elif line.find(line2)==line.rfind(line2): print(1)
else: print(">1")
