user=int(input("your  number : "))
i=0
count=0
new=[]
while i<=100:
    user1=int(input("your guess number : "))
    if user==user1:
        print("your guess correct" ,user )
        break
        
    else:
        
        print("guess is wrong")
        count=count+1
        new.append(count)
    i=i+1
print("wrong guess", new)


    
