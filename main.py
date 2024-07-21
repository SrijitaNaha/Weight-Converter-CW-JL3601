from tkinter import *

# Creating GUI window
root = Tk()


# Function to convert weight
def convert():
    # converting kg to gram
    gram = float(row2_val.get()) * 1000
    # converting  kg to pound
    pound = float(row2_val.get()) * 2.20462
    # convert kg to ounce
    ounce = float(row2_val.get()) * 35.274

    # Entering the converted weights to the text widgets
    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, ounce)


# Creating the Label widgets
lbl_weight = Label(root, text="Enter the weight in Kg")
row2_val = StringVar()
row2 = Entry(root, textvariable=row2_val)
col1 = Label(root, text="Gram")
col2 = Label(root, text="Pounds")
col3 = Label(root, text="Ounce")

# Creating the Text Widgets
t1 = Text(root, height=1, width=20)

t2 = Text(root, height=1, width=20)

t3 = Text(root, height=1, width=20)

# Creating the Button Widget
btn = Button(root, text="Convert", command=convert)

# Grid method used for creating table structure
lbl_weight.grid(row=0, column=0)
row2.grid(row=0, column=1)
col1.grid(row=1, column=0)
col2.grid(row=1, column=1)
col3.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
btn.grid(row=0, column=2)

root.mainloop()
