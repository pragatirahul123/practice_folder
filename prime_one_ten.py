i=2
while(i<=10):
    j=2
    while (j<i):
        if(i%2==0):
            print(i,"not prime")
            break
        j=j+1
    else:
        print(i,"prime")
    i=i+1
    
