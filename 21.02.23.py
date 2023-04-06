import random

#list2 = [random.randint(1,9) for i in range(5)]
list2=[2,4,6,8,6,4,2]
print(list2)
k=0
while(k<len(list2)):
    if (list2[k]%2==0):
        list2.remove(list2[k])
        k-=1
    k+=1
print(list2)