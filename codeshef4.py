# Write a program to print the first 14 odd numbers starting from 3
# Output:
# 3 5 7 9 11 13 15 17 19 21 23 25 27 29


var=3
while var<=30:
    if var%2!=0:
        print(var," ",end="")
    var=var+1
