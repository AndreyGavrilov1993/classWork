'''str="ghjklfd"
str2="ghbuj"
line2=""
for i in range (len(str)-1, -1, -1):
    line2+=str[i]
if(line2==str2): print("yes")
else: print("no")'''
#Есть список с именами, будем считать, что имена заканчивающиеся на букву "а" или "я" - женские имена, а остальные мужские. Посчитать количество имён.
names=("Андрей","Анастасия","Виталий","Мария","Ира","Равиль","Ася")

man=0
women=0
for i in names:
    if i[len(i)-1]=="а" or i[len(i)-1]=="я": woman+=1
    else: man+1
    print(man)
    print(woman)