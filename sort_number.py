user=int(input("enter a number:"))
a1=str(user)
index=0
new=[]
while index<len(a1):
    new.append(a1[index])
    index=index+1
new.sort()
var=("".join(new))
print(var)


