from tkinter import *

root = Tk()
root.title("BMI Calculator")
root.geometry("500x500")

kg = IntVar()
cm = IntVar()

def calculator():
    givenKG = kg.get()
    givenCM = cm.get()

    square = givenCM*givenCM
    number = givenKG/square
    final = number*10000

    display = Label(root , text=f"Your BMI is {final}" , width=50 , bg="blue" , fg="white")
    display.place(x=25 , y=200)

    if final < 18:
        result = "underweight"
        colour = "light blue"

    elif final > 18 and final < 25:
        result = "healthy"
        colour = "green"

    elif final > 25 and final < 30:
        result = "overweight"
        colour = "orange"

    elif final > 30:
        result="obese"
        colour = "red"

    massIndex = Label(root , text=f"You are {result} due to your BMI" , width=50 , bg=f"{colour}")
    massIndex.place(x=25 , y=250)

displayKG = Label(root , text="Weight in KG:")
displayKG.place(x=10 , y=70)
weight = Entry(textvariable=kg , width=20)
weight.place(x=10 , y=100)

displayCM = Label(root , text="Height in CM:")
displayCM.place(x=200 , y=70)
height = Entry(textvariable=cm , width=20)
height.place(x=200 , y=100)

calculateButton = Button(root , text="Calculate BMI" , command=calculator)
calculateButton.place(x=95 , y=5)

root.mainloop()