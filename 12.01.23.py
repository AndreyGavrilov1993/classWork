#Пользователь вводит предложение пи строку. Определить есть ли это слово в строке
'''line=input("Введите строку: ")
word=input("input word")
print("yes" if line.find(word) else "no")'''
#Необходимо определить сколько раз используется это слово в предложении
'''line=input("input line: ")
word=input("input word: ")
print(line.count(word))'''
'''line=input("input line: ")
word=input("input word: ")
counter=0
begin=0
while True:
    if(line.find(word,begin,len(line)))==-1: break
    else:
        begin=line.find(word,begin,len(line))+1
        counter+=1
print(counter)'''
#У вас есть строка. Пользователь вводит первое и второе слово. Заменить первые слова на вторые слова
'''line=input("input line:")
word1=input("input word: ")
word2=input("input world: ")
line=line.replace(word1,word2)
print(line)'''
#Есть предложения, полшьзователь вводит номер первого и второго слова. Нужно поменять эти слова местами
'''line=input("input line: ")
word1=input("input word: ")
word2=input("input word: ")
'''
'''Vasia=[5,4,5,5,4,3,4,5,5]
counter=0
for i in Vasia:
    if i==4: counter+=1
print(counter)'''
'''students=["Ольга","Виктор","Олег","Герасим"]
for i in students: print(i, end=" ")  '''
'''student1=["Ольга",23,4.5,"БВ222"]
student2=["Ольга",23,4.5,"БВ222"]
print((student1[2]+student2[2])/2)'''
'''name=input("input name: ")
surname=input("input surname: ")
age=input("input age: ")
height=int(input("input height: "))
weight=int(input("input weight: "))
list=["name","surname","age","height","weight"]
print(list)'''
'''student=[",",",",""]
student[0]=input("input name: ")
student[1]=input("input surname: ")
student[2]=input("input age: ")
student[3]=int(input("input height: "))
student[4]=int(input("input weight: "))
print(student)'''
'''st=["Алёна","Катя","Лена","Катя","Катя"]
word=input().upper()
counter=0
for i in st:
    if i.upper()==word: counter+=1
print(counter)'''
'''import random
list1=["","","","","","","","",""]
list2=["","","","","","","",""]
summ1=0
summ2=0
for i in range(len(list1)):
    list1[i]=random.randint(1,9)
    summ1+=list1[i]
for i in range(len(list2)):
    list2[i]=random.randint(1,9)
    summ2+=list2[i]
if summ1>summ2: print("list1>list2")
elif summ1<summ2: print("list1<list2")
else: print("list1=list2")

print(list1)
print(list2)

for i in range (len(list1)):
    for j in list2:
        if list1[i]==j:
            flag=True
            for k in range (i):
                if list1[i]==list1[k]:
                   flag=False
                   break
            if flag:
             print(list1[i],end=" ")
        break'''

list1=["0","0","0","0","0","0"]
for i in range (len(list1)):
    list1[i]=int(input("input data: "))
num=int(input("input num: "))
counter=-0
summ=0
for i in list1:
    if i==num: counter+=1
    summ+=i
print(counter)
print(summ)
print(summ/len(list1))