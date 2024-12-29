correct_pass = "aaa"
my_pass = ""
count = 1
while correct_pass!=my_pass :
    if count<=3:
        print("			Try ( ",count," ) :")
        my_pass = input("Enter Your Password : ") # my_pass = aaa
        count+=1 # count = 3
    else :
        print("No more Times ..!")
        break
else :
    print("You Login Succefully ...")