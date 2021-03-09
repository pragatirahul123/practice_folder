num=int(input("enetr a number"))
var=1
c1=0
while var<num:
    if num%var==0:
        c1=c1+2
    var=var+1
if (c1==2):
    print("prime number",num)
else:
    print("not prime number",num)
