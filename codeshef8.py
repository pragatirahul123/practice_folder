# Write a program to print numbers from N to 1, where N is given as an input from the user.
# Sample Input:
# 5
# Sample Output:
# 5
# 4
# 3
# 2
# 1

user=int(input("enter a number"))
var=user
while var>=1:
    print(var)
    var=var-1
