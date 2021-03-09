a=int(input("enetr a number"))
b=int(input("enetr a number"))
c=int(input("enetr a number"))

if a>b:
    if a<c:
        sec_max=a
        print(sec_max)
    elif b>c:
        sec_max=b
        print(sec_max)
    else:
        sec_max=c
        print(sec_max)
else:
    if a>c:
        sec_max=a
    elif b<c:
        sec_max=b
    else:
        sec_max=c
print(sec_max)





