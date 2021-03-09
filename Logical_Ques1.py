list=[[2,3,1],[3,4,1],[6,3,1],[3,5,1]]
index=0
while index<len(list):
    jar=0
    sum=0
    while jar<len(list[index]):
        sum=sum+list[index][jar]
        jar=jar+1
    print(sum)
    index=index+1
    
