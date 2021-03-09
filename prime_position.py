num=int(input("enter a number"))
var=1
position=0
while var<=num:
    jar=2
    c=0
    while jar<=num:
        if var%jar==0:
            c=c+1
        jar=jar+1
    if c==1:
        position=position+1
        print(var,"position",position) 
    var=var+1
