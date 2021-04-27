list=[[1,2,3,44,5,6],[7,11,4,6,7],[6,2,99,22,55]]
index=0
while index<len(list):
    jar=0
    max=0
    while jar<len(list[index]):
        if list[index][jar]>max:
            max=list[index][jar]
        jar=jar+1
    index=index+1
    print(max)
 
