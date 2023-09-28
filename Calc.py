# from tkinter import StringVar
import customtkinter
from customtkinter import StringVar, CTkSwitch

##TODO: Dark/Light Mode


###TODO: Zeichen neben der Zahl entfernen DONE, wenn neue Rechnung eingegeben wird->vorherige wegmachen


# Methods/Definitions/Functions

labelValueList = []
resultForLabel = None

firstNumberList = []
secondNumberList = []


def changeLabelResult(value):
    # global labelResult
    global resultForLabel
    resultForLabel = value
    labelResult.configure(text=resultForLabel)


def changeLabelValue(value):
    global labelValueList
    # global
    # print (labelValue)
    """ labelValue = value """
    labelValueList.append(value)
    label.configure(text=labelValueList)
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
    global firstNumberList
    global secondNumberList

    if firstNumberList and saveOperator is None:
        firstNumberList.append(number)

    if not firstNumberList and saveOperator is None:
        firstNumberList = [number]

        # print(firstNumber)

    """ if saveOperator is not None and firstNumberList:
        firstNumberList.append(number) 

    if saveOperator is not None and not firstNumberList:
        firstNumberList = [number] """

    if firstNumberList and saveOperator != None and secondNumberList:
        secondNumberList.append(number)

    if firstNumberList and saveOperator != None and not secondNumberList:
        secondNumberList = [number]
        # print(secondNumber)

    print(number)
    number = None


def equals():
    """firstNumber, secondNumber, saveOperator"""

    ## TODO: try-catch, e.g. only operator entered
    global firstNumberList
    global secondNumberList
    global saveOperator
    global labelValueList

    firstNumber = int("".join(map(str, firstNumberList)))
    secondNumber = int("".join(map(str, secondNumberList)))

    """ print(firstNumber)
    print(secondNumber) """

    """ print(firstNumber)
    print(secondNumber) """
    if saveOperator == "+" and firstNumberList != [] and secondNumberList != []:
        add(firstNumber, secondNumber)

    if (
        saveOperator == "-"
        and firstNumberList is not [None]
        and secondNumberList is not [None]
    ):
        sub(firstNumber, secondNumber)

    if (
        saveOperator == "*"
        and firstNumberList is not [None]
        and secondNumberList is not [None]
    ):
        mult(firstNumber, secondNumber)

    if (
        saveOperator == "/"
        and firstNumberList is not [None]
        and secondNumberList is not [None]
    ):
        div(firstNumber, secondNumber)

    firstNumberList = []
    secondNumberList = []
    saveOperator = None
    labelValueList = []


def add(firstNumber, secondNumber):
    global saveOperator
    number = None
    global labelValueList

    # firstNumber = None
    """ if labelValueList.count:
        result = result + number
        print(result) """

    result = firstNumber + secondNumber

    print(result)
    changeLabelResult(result)


def sub(firstNumberList, secondNumberList):
    result = firstNumberList - secondNumberList
    print(result)
    changeLabelResult(result)


def mult(firstNumberList, secondNumberList):
    result = firstNumberList * secondNumberList
    print(result)
    changeLabelResult(result)


def div(firstNumberList, secondNumberList):
    result = firstNumberList / secondNumberList
    print(result)
    changeLabelResult(result)


def clear():
    label.configure(text="0")
    labelResult.configure(text="0")
    global firstNumberList
    global secondNumberList
    global saveOperator
    global labelValueList
    global result
    saveOperator = None
    firstNumberList = []
    secondNumberList = []
    labelValueList = []
    result = None


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("400x700")


frameInputOutput = customtkinter.CTkFrame(master=root)
frameInputOutput.pack(padx=5, pady=5, side="top", fill="both")

# textInput = StringVar(value="0")

""" frameOutput = customtkinter.CTkFrame(master=root)
frameOutput.pack """

label = customtkinter.CTkLabel(master=frameInputOutput, text="0")
label.grid(padx=10, pady=5, row=0, column=0)

labelResult = customtkinter.CTkLabel(master=frameInputOutput, text="0")
labelResult.grid(padx=10, pady=5, row=1, column=0)

frameNumbers = customtkinter.CTkFrame(master=root, width=500, height=500)
frameNumbers.pack(padx=5, pady=5, side="left", anchor="nw")

button1 = customtkinter.CTkButton(
    master=frameNumbers,
    text="1",
    width=40,
    height=40,
    command=lambda: (changeLabelValue(1), saveNumber(1)),
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
button0.grid(column=0, columnspan=3, row=3, pady=10, padx=10, sticky="ew")

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
    command=lambda: (saveOperators("+"), changeLabelValue("+")),
)
buttonPlus.grid(column=0, row=1, pady=10, padx=10)

buttonMinus = customtkinter.CTkButton(
    master=frameOperators,
    text="-",
    width=40,
    height=40,
    command=lambda: ((saveOperators("-"), changeLabelValue("-"))),
)
buttonMinus.grid(column=1, row=1, pady=10, padx=10)

buttonMult = customtkinter.CTkButton(
    master=frameOperators,
    text="*",
    width=40,
    height=40,
    command=lambda: (saveOperators("*"), changeLabelValue("*")),
)
buttonMult.grid(column=1, row=2, pady=10, padx=10)

buttonDivide = customtkinter.CTkButton(
    master=frameOperators,
    text="/",
    width=40,
    height=40,
    command=lambda: (saveOperators("/"), changeLabelValue("/")),
)
buttonDivide.grid(column=0, row=2, pady=10, padx=10)

buttonEquals = customtkinter.CTkButton(
    master=frameOperators,
    text="=",
    width=40,
    height=40,
    command=lambda: (equals()),
)
""" firstNumber, secondNumber, saveOperator  -> in equals"""
buttonEquals.grid(column=1, row=0, pady=10, padx=10)


""" switch = customtkinter.CTkSwitch(master=root, text="Dark Mode", command=switchState)
switch.pack(side="left", anchor="w") """


root.mainloop()
