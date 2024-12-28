import tkinter as tk # tk is a short name for tkinter
# root is a variable for the main window
root = tk.Tk()

# this line to insert title to GUI, title().
root.title("First GUI")

# geometry("500x400") to specify the the width = 500 and height = 400 of GUI
root.geometry("500x400")

# firstLabel is a variable to store a label
# text : to store the text in the label "Hello World"
# font : to apply bold to text and make the text larger 30
# place( x=150 , y=150 ) is a method to place the label on GUI using x,y points
firstLabel = tk.Label(text="Hello World" , font=('bold',30))
firstLabel.place(x=150 , y=150)

#starts the Tkinter event loop to keep the GUI running and responsive.
root.mainloop()