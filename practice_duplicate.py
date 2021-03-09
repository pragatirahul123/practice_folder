list1=[1,34,67,8]
list2=[4,1,8,9,11,67]
index=0
new=[]
while index<len(list1):
    jar=0
    while jar<len(list2):
        if list1[index]==list2[jar]:
            new.append(list1[index])
        jar=jar+1
    index=index+1
print(new)
        
