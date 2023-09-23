# from tkinter import StringVar
import customtkinter
from customtkinter import StringVar

##TODO: Dark/Light Mode

# Methods/Definitions
def changeLabelValue(value):
    label.configure(text=value)


def equals():
    print("0")

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


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
    command=lambda: changeLabelValue("1"),
)
button1.grid(column=0, row=0, pady=10, padx=10)

button2 = customtkinter.CTkButton(
    master=frameNumbers,
    text="2",
    width=40,
    height=40,
    command=lambda: changeLabelValue("2"),
)
button2.grid(column=1, row=0, pady=10, padx=10)

button3 = customtkinter.CTkButton(
    master=frameNumbers,
    text="3",
    width=40,
    height=40,
    command=lambda: changeLabelValue("3"),
)
button3.grid(column=2, row=0, pady=10, padx=10)

button4 = customtkinter.CTkButton(
    master=frameNumbers,
    text="4",
    width=40,
    height=40,
    command=lambda: changeLabelValue("4"),
)
button4.grid(column=0, row=1, pady=10, padx=10)

button5 = customtkinter.CTkButton(
    master=frameNumbers,
    text="5",
    width=40,
    height=40,
    command=lambda: changeLabelValue("5"),
)
button5.grid(column=1, row=1, pady=10, padx=10)

button6 = customtkinter.CTkButton(
    master=frameNumbers,
    text="6",
    width=40,
    height=40,
    command=lambda: changeLabelValue("6"),
)
button6.grid(column=2, row=1, pady=10, padx=10)

button7 = customtkinter.CTkButton(
    master=frameNumbers,
    text="7",
    width=40,
    height=40,
    command=lambda: changeLabelValue("7"),
)
button7.grid(column=0, row=2, pady=10, padx=10)

button8 = customtkinter.CTkButton(
    master=frameNumbers,
    text="8",
    width=40,
    height=40,
    command=lambda: changeLabelValue("8"),
)
button8.grid(column=1, row=2, pady=10, padx=10)

button9 = customtkinter.CTkButton(
    master=frameNumbers,
    text="9",
    width=40,
    height=40,
    command=lambda: changeLabelValue("9"),
)
button9.grid(column=2, row=2, pady=10, padx=10)

button0 = customtkinter.CTkButton(
    master=frameNumbers,
    text="0",
    width=40,
    height=40,
    command=lambda: changeLabelValue("0"),
)
button0.grid(column=0, row=3, pady=10, padx=10)

frameOperators = customtkinter.CTkFrame(master=root)
frameOperators.pack(padx=5, pady=5, side="right", anchor="ne")

button1 = customtkinter.CTkButton(
    master=frameOperators, text="<----", width=40, height=40
)
button1.grid(column=0, row=0, pady=10, padx=10)

button1 = customtkinter.CTkButton(
    master=frameOperators,
    text="+",
    width=40,
    height=40,
    command=lambda: add(changeLabelValue),
)
button1.grid(column=0, row=1, pady=10, padx=10)

button1 = customtkinter.CTkButton(master=frameOperators, text="-", width=40, height=40)
button1.grid(column=1, row=1, pady=10, padx=10)

button1 = customtkinter.CTkButton(master=frameOperators, text="*", width=40, height=40)
button1.grid(column=2, row=1, pady=10, padx=10)

button1 = customtkinter.CTkButton(master=frameOperators, text="/", width=40, height=40)
button1.grid(column=0, row=2, pady=10, padx=10)

button1 = customtkinter.CTkButton(master=frameOperators, text="=", width=40, height=40, command= lambda: equals)
button1.grid(column=0, row=0, pady=10, padx=10)


root.mainloop()

numbers = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
operators = "+", "-", "*", "/"
