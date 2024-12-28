avg = float(input("Enter The Average : "))
if 100 >= avg >= 90 : # is like avg <=100 and avg >=90
    print("A")
elif 89 >= avg >= 80 :
    print("B")
elif avg <=79 and avg >=70 : # is like 79 >= avg >= 70
    print("C")
elif avg<70 :
    print("Try Again")