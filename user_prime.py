num=int(input("enter a number"))
var=0
i=1
p=0
while True:
    c=0
    jar=2
    while jar<=i:
        if i%jar==0:
            c=c+1
        jar=jar+1
    if c==1:
        p=p+1
        print(i) 
        var=var+1
    if var==num:
        break
    i=i+1
