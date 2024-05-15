from tkinter import *

outputText = ""

def addOutputNumber(number):
  global outputText

  try:
    str(number)
  except :
    print("error")

  outputText += number

  output.configure(text=outputText)

def addOutputOperator(operator):
  global outputText

  try:
    str(operator)
  except :
    print("error")

  outputText += operator

  output.configure(text=outputText)

def backspace():
  global outputText

  outputText = outputText[:-1]

  output.configure(text=outputText)

def clear():
  global outputText

  outputText = ""

  output.configure(text=outputText)

def calculate():
  global outputText

  try:
    expression = outputText.replace("x", "*").replace("÷", "/")
    result = eval(expression)
    outputText = str(result)
  except:
    print('error')
  
  output.configure(text=outputText)


root = Tk()
root.title("Calculator")
root.geometry("600x700")
root.configure(background="lightyellow")

title = Label(root, text="Calculator", font=("Arial", 24))
title.pack(pady=35)

output = Label(root, width="60", text="", background="lightgray", font=("Arial", 35))
output.pack(pady=10)

buttonFrame = Frame(root)
buttonFrame.pack(pady=45)

numpadOne = Button(buttonFrame, text="1", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("1"))
numpadOne.grid(column=0, row=0)
numpadTwo = Button(buttonFrame, text="2", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("2"))
numpadTwo.grid(column=1, row=0)
numpadThree = Button(buttonFrame, text="3", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("3"))
numpadThree.grid(column=2, row=0)
plusButton = Button(buttonFrame, text="+", width="5", height="2", font=("Arial", 18), command=lambda: addOutputOperator(" + "))
plusButton.grid(column=3, row=0)

numpadFour = Button(buttonFrame, text="4", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("4"))
numpadFour.grid(column=0, row=1)
numpadFive = Button(buttonFrame, text="5", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("5"))
numpadFive.grid(column=1, row=1)
numpadSix = Button(buttonFrame, text="6", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("6"))
numpadSix.grid(column=2, row=1)
minusButton = Button(buttonFrame, text="-", width="5", height="2", font=("Arial", 18), command=lambda: addOutputOperator(" - "))
minusButton.grid(column=3, row=1)

numpadSeven = Button(buttonFrame, text="7", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("7"))
numpadSeven.grid(column=0, row=2)
numpadEight = Button(buttonFrame, text="8", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("8"))
numpadEight.grid(column=1, row=2)
numpadNine = Button(buttonFrame, text="9", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("9"))
numpadNine.grid(column=2, row=2)
multiplyButton = Button(buttonFrame, text="x", width="5", height="2", font=("Arial", 18), command=lambda: addOutputOperator(" x "))
multiplyButton.grid(column=3, row=2)

backspaceButton = Button(buttonFrame, text="<", width="5", height="2", font=("Arial", 18), command=backspace)
backspaceButton.grid(column=0, row=3)
numpadZero = Button(buttonFrame, text="0", width="5", height="2", font=("Arial", 18), command=lambda: addOutputNumber("0"))
numpadZero.grid(column=1, row=3)
clearButton = Button(buttonFrame, text="C", width="5", height="2", font=("Arial", 18), command=clear)
clearButton.grid(column=2, row=3)
devideButton = Button(buttonFrame, text="÷", width="5", height="2", font=("Arial", 18), command=lambda: addOutputOperator(" ÷ "))
devideButton.grid(column=3, row=3)

equalButton = Button(buttonFrame, text="=", width="5", height="2", font=("Arial", 18), command=calculate)
equalButton.grid(column=0, row=4, columnspan=4, sticky="nsew")

for i in range(4):
    buttonFrame.grid_columnconfigure(i, weight=1)
for i in range(5):
    buttonFrame.grid_rowconfigure(i, weight=1)


root.mainloop()