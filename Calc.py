# from tkinter import StringVar
import customtkinter
from customtkinter import StringVar, CTkSwitch

##TODO: Dark/Light Mode


# Methods/Definitions/Functions

labelValue = "0"


def changeLabelValue(value):
    global labelValue
    # print (labelValue)
    """ labelValue = value """
    label.configure(text=value)
    """ if labelValue ==  "0":
        label.configure(text = value) """
    """ else:
        label.configure(text=+ value) """


""" def switchState():
    if switch.select:
        customtkinter.set_appearance_mode("dark")
    if switch.deselect:
        customtkinter.set_appearance_mode("light") """


""" def saveSecondNumber(secondNumber):
    if firstNumber != None and saveOperator != None:
        print(secondNumber)
        return secondNumber """


saveOperator = None
firstNumber = None
secondNumber = None


def saveOperators(operator):
    print(operator)
    global saveOperator
    saveOperator = operator


def saveNumber(number):
    global firstNumber
    global secondNumber

    if firstNumber is None and saveOperator is None:
        firstNumber = number
        print(firstNumber)

    """ and not (button0._clicked or button1._clicked or button2._clicked or button3._clicked or button4._clicked or button5._clicked or button6._clicked or button7._clicked or button8._clicked or button9._clicked) """
    """ if firstNumber != None and saveOperator is None:
        firstNumber = str(firstNumber) + str(number)
        print(firstNumber + "lol") """

    if firstNumber != None and saveOperator != None:
        secondNumber = number
        print(secondNumber)

    number = None


def equals():
    """firstNumber, secondNumber, saveOperator"""
    global firstNumber
    global secondNumber
    global saveOperator
    print(firstNumber)
    print(secondNumber)
    if saveOperator == "+" and firstNumber != None and secondNumber != None:
        add(firstNumber, secondNumber)

    if saveOperator == "-" and firstNumber is not None and secondNumber is not None:
        sub(firstNumber, secondNumber)

    if saveOperator == "*" and firstNumber is not None and secondNumber is not None:
        mult(firstNumber, secondNumber)

    if saveOperator == "/" and firstNumber is not None and secondNumber is not None:
        div(firstNumber, secondNumber)

    firstNumber = None
    secondNumber = None
    saveOperator = None


def add(firstNumber, secondNumber):
    result = firstNumber + secondNumber
    print(result)
    changeLabelValue(result)


def sub(firstNumber, secondNumber):
    result = firstNumber - secondNumber
    print(result)
    changeLabelValue(result)


def mult(firstNumber, secondNumber):
    result = firstNumber * secondNumber
    print(result)
    changeLabelValue(result)


def div(firstNumber, secondNumber):
    result = firstNumber / secondNumber
    print(result)
    changeLabelValue(result)


def clear():
    changeLabelValue("0")
    global firstNumber
    global secondNumber
    global saveOperator
    saveOperator = None
    firstNumber = None
    secondNumber = None


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("400x700")


frameInput = customtkinter.CTkFrame(master=root)
frameInput.pack(padx=5, pady=5, side="top", fill="both")

# textInput = StringVar(value="0")

label = customtkinter.CTkLabel(master=frameInput, text="0", anchor="w", compound="left")
label.pack(side="left", padx=10)

frameNumbers = customtkinter.CTkFrame(master=root, width=500, height=500)
frameNumbers.pack(padx=5, pady=5, side="left", anchor="nw")

button1 = customtkinter.CTkButton(
    master=frameNumbers,
    text="1",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("1"), saveNumber(1)),
)
button1.grid(column=0, row=0, pady=10, padx=10)

button2 = customtkinter.CTkButton(
    master=frameNumbers,
    text="2",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("2"), saveNumber(2)),
)
button2.grid(column=1, row=0, pady=10, padx=10)

button3 = customtkinter.CTkButton(
    master=frameNumbers,
    text="3",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("3"), saveNumber(3)),
)
button3.grid(column=2, row=0, pady=10, padx=10)

button4 = customtkinter.CTkButton(
    master=frameNumbers,
    text="4",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("4"), saveNumber(4)),
)
button4.grid(column=0, row=1, pady=10, padx=10)

button5 = customtkinter.CTkButton(
    master=frameNumbers,
    text="5",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("5"), saveNumber(5)),
)
button5.grid(column=1, row=1, pady=10, padx=10)

button6 = customtkinter.CTkButton(
    master=frameNumbers,
    text="6",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("6"), saveNumber(6)),
)
button6.grid(column=2, row=1, pady=10, padx=10)

button7 = customtkinter.CTkButton(
    master=frameNumbers,
    text="7",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("7"), saveNumber(7)),
)
button7.grid(column=0, row=2, pady=10, padx=10)

button8 = customtkinter.CTkButton(
    master=frameNumbers,
    text="8",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("8"), saveNumber(8)),
)
button8.grid(column=1, row=2, pady=10, padx=10)

button9 = customtkinter.CTkButton(
    master=frameNumbers,
    text="9",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("9"), saveNumber(9)),
)
button9.grid(column=2, row=2, pady=10, padx=10)

button0 = customtkinter.CTkButton(
    master=frameNumbers,
    text="0",
    width=40,
    height=40,
    command=lambda: (changeLabelValue("0"), saveNumber(0)),
)
button0.grid(column=0, row=3, pady=10, padx=10)

frameOperators = customtkinter.CTkFrame(master=root)
frameOperators.pack(padx=5, pady=5, side="right", anchor="ne")

buttonRemove = customtkinter.CTkButton(
    master=frameOperators, text="CE", width=40, height=40, command=lambda: clear()
)
buttonRemove.grid(column=0, row=0, pady=10, padx=10)

# TODO: Edit button command
buttonPlus = customtkinter.CTkButton(
    master=frameOperators,
    text="+",
    width=40,
    height=40,
    command=lambda: saveOperators("+"),
)
buttonPlus.grid(column=0, row=1, pady=10, padx=10)

buttonMinus = customtkinter.CTkButton(
    master=frameOperators,
    text="-",
    width=40,
    height=40,
    command=lambda: saveOperators("-"),
)
buttonMinus.grid(column=1, row=1, pady=10, padx=10)

buttonMult = customtkinter.CTkButton(
    master=frameOperators,
    text="*",
    width=40,
    height=40,
    command=lambda: saveOperators("*"),
)
buttonMult.grid(column=2, row=1, pady=10, padx=10)

buttonDivide = customtkinter.CTkButton(
    master=frameOperators,
    text="/",
    width=40,
    height=40,
    command=lambda: saveOperators("/"),
)
buttonDivide.grid(column=0, row=2, pady=10, padx=10)

buttonEquals = customtkinter.CTkButton(
    master=frameOperators,
    text="=",
    width=40,
    height=40,
    command=lambda: equals(),
)
""" firstNumber, secondNumber, saveOperator  -> in equals"""
buttonEquals.grid(column=1, row=0, pady=10, padx=10)


""" switch = customtkinter.CTkSwitch(master=root, text="Dark Mode", command=switchState)
switch.pack(side="left", anchor="w") """


root.mainloop()
