list=[22,3,41,11,5,2]
min=list[0]
i=0
while i<len(list):
    if list[i]<min:
        min=list[i]
    i=i+1
print(min)
