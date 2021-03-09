list=[1,2,6,4,7,8,4,5]
num=8
new=[]
index=0
while index<len(list):
    jar=index+1
    while jar<len(list):
        if list[index]+ list[jar]== num:
            print(list[index],list[jar] , "==", num)
        jar=jar+1
    index=index+1

