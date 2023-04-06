# file1=open("text1.txt", 'r', encoding='utf-8')
# count=0
# num=0
# for line in file1:
#     if (line!=""): count+=len(line.split(" "))
# file1.seek(0,0)
#
# for number in file1:
#   for i in line:
#     if (i.isdigit()): num+=1
# file1.seek(0,0)
#
# print(file1.read())
# print(f'количество слов', count)
# print(f'количество цифр', num)
#
# file1.close();

# with open("text1.txt", 'r', encoding='utf-8') as file1:
#    dict={}
#    for line in file1:
#       list1 = line.split(" ")
#       dict[list1[0]]=list1[1]
#    for key, val in dict:
#       print(f"{key} : {val}")

# def copy(path):
#  with open(path, "r", encoding="utf-8") as f:
#       text=f.read()
#  path=path[:-4:]+"(copy).txt"
#  with open(path, "w", encoding="utf-8") as f:
#       f.write(text)
# copy("text1.txt")

# def copy(path):
#     with open(path, "r", encoding="utf-8") as f:
#         list=[]
#         for i in f:
#           list+=i.split(" ")
#         text=""
#         for i in list:
#             if len(i)>=7:
#                 if len(i)==7 and i[-1]!="\n":
#                  text+=i+" "
#                 elif len(i)>7:
#                   text+=i+" "
#     path = path[:-4:] + "(copy).txt"
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(text)
# copy("text1.txt")

def copy(path):
    with open(path, "r", encoding="utf-8") as f:
        list=f.read().split("\n")
        list.reverse()
        path = path[:-4:] + "(copy).txt"
    with open(path, "w", encoding="utf-8") as f:
       for i in list:
           f.write(i+"\n")
copy("text1.txt")