starNum = int(input("Enter Number of Stars : "))
for i in range(1,starNum+1): # rows
    for j in range(1,starNum+1): # columns
        print("*",end="  ")
    print()