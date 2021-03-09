#Write a program to print the sum of numbers from 1 to N, where N is given as an input from the user.
#Sample input:
#5  
#Sample output:
#15 (1+2+3+4+5)



user=int(input("enter a number"))
index=1
sum=0
while index<=user:
    user1=int(input("enter a number"))
    sum=sum+user1
    index=index+1
print(sum)

