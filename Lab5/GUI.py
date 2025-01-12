import tkinter as tk
root = tk.Tk()
root.title("Login")
root.geometry("500x500")

loginLabel = tk.Label(root , text="تسجيل" , font=("bold",30))
loginLabel.place(x=200 , y=80)

userNameLab = tk.Label(root , text="username")
userNameLab.place(x=300 , y=200)
userName = tk.Entry(root)
userName.place(x=170 , y=200)

password = tk.Label(root , text="password")
password.place(x=300 , y=250)
password = tk.Entry(root)
password.place(x=170 , y=250)

loginBtn = tk.Button(root , text = "login")
loginBtn.place(x=200 , y=400)
root.mainloop()