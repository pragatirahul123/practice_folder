list=[10,11,12,13,14,17,19,18]
index=0
num=30
c1=[]
while index<len(list):
    jar=index+1
    a1=[]
    while jar<len(list):
        if list[index]+list[jar]==num:
            a1.append(list[index])
            a1.append(list[jar])
            c1.append(a1)
        jar=jar+1
    index=index+1
print(c1)
