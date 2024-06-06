import tkinter as tk
from tkinter import *

math= "0"
res = "0"

root = tk.Tk()

root.resizable(width=False, height=False)
root.geometry("400x320")
root.title("Calculator")
root.config(bg="#008080")


def button_click(number):
    global res
    if res == "1":
        e.delete(0, tk.END)
        e.insert(tk.END, str(number))
        res = 0
    else:
        e.insert(tk.END, str(number))

  
def calc(symbol):
    global math
    global current1
    if math == "0": 
        math = symbol
        current1 = e.get()
        e.delete(0, tk.END)
    else:
        result()  
        current1 = e.get()
        e.delete(0, tk.END)
        math = symbol


def delete():
    e.delete(0, tk.END)


def percentage():
    new = float(e.get())
    e.delete(0, tk.END)
    e.insert(tk.END, str(new*0.01))


def result():
    global math
    global res
    if math == "+":
        current2 = e.get()
        e.delete(0, tk.END)
        current = float(current1)+float(current2)
        e.insert(0,str(current))
        math= "0"
        res = "1"
    elif math == "-":
        current2 = e.get()
        e.delete(0, tk.END)
        current = float(current1)-float(current2)
        e.insert(0,str(current))
        math="0"
        res= "1"
    elif math == "*":
        current2 = e.get()
        e.delete(0, tk.END)
        current = float(current1)*float(current2)
        e.insert(0,str(current))
        math="0"
        res = "1"
    elif math == "/":
        current2 = e.get()
        e.delete(0, tk.END)
        current = float(current1)/float(current2)
        e.insert(0,str(current))
        math="0"
        res = "1"


#Design Calculator

e = Entry(root, font = ('Arial', 16), width=30)
e.pack(padx=1, pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)


button_delete = tk.Button(buttonframe, text = "C", font= ("Arial", 18), command= lambda:delete())
button_delete.grid(row=0, column=0, sticky = tk.W+tk.E)

button_division = tk.Button(buttonframe, text = "/", font= ("Arial", 18), command= lambda: calc("/"))
button_division.grid(row=0, column=1, sticky = tk.W+tk.E)

button_percentage = tk.Button(buttonframe, text = "%", font= ("Arial", 18), command= lambda: percentage())
button_percentage.grid(row=0, column=2, sticky = tk.W+tk.E)

button_multiplication = tk.Button(buttonframe, text = "*", font= ("Arial", 18), command= lambda: calc("*"))
button_multiplication.grid(row=0, column=3, sticky = tk.W+tk.E)

btn7 = tk.Button(buttonframe, text = "7", font= ("Arial", 18), command= lambda: button_click(7))
btn7.grid(row=1, column=0, sticky = tk.W+tk.E)

btn8 = tk.Button(buttonframe, text = "8", font= ("Arial", 18), command= lambda: button_click(8))
btn8.grid(row=1, column=1, sticky = tk.W+tk.E)

btn9 = tk.Button(buttonframe, text = "9", font= ("Arial", 18), command= lambda: button_click(9))
btn9.grid(row=1, column=2, sticky = tk.W+tk.E)

button_subtraction = tk.Button(buttonframe, text = "-", font= ("Arial", 18), command= lambda: calc("-"))
button_subtraction.grid(row=1, column=3, sticky = tk.W+tk.E)

btn4 = tk.Button(buttonframe, text = "4", font= ("Arial", 18), command= lambda: button_click(4))
btn4.grid(row=2, column=0, sticky = tk.W+tk.E)

btn5 = tk.Button(buttonframe, text = "5", font= ("Arial", 18), command= lambda: button_click(5))
btn5.grid(row=2, column=1, sticky = tk.W+tk.E)

btn6 = tk.Button(buttonframe, text = "6", font= ("Arial", 18), command= lambda: button_click(6))
btn6.grid(row=2, column=2, sticky = tk.W+tk.E)

button_add = tk.Button(buttonframe, text = "+", font= ("Arial", 18), command= lambda: calc("+"))
button_add.grid(row=2, column=3, sticky = tk.W+tk.E)

btn1 = tk.Button(buttonframe, text = "1", font= ("Arial", 18), command= lambda: button_click(1))
btn1.grid(row=3, column=0, sticky = tk.W+tk.E)

btn2 = tk.Button(buttonframe, text = "2", font= ("Arial", 18), command= lambda: button_click(2))
btn2.grid(row=3, column=1, sticky = tk.W+tk.E)

btn3 = tk.Button(buttonframe, text = "3", font= ("Arial", 18), command= lambda: button_click(3))
btn3.grid(row=3, column=2, sticky = tk.W+tk.E)

button_result = tk.Button(buttonframe, text = "=", font= ("Arial", 18), bg="black", fg="white", command= lambda: result())
button_result.grid(row=3, column=3, sticky = tk.W+tk.E+tk.N+tk.S, rowspan=2)

btn0 = tk.Button(buttonframe, text = "0", font= ("Arial", 18), command= lambda: button_click(0))
btn0.grid(row=4, column=0, sticky = tk.W+tk.E, columnspan=2)

button_point = tk.Button(buttonframe, text = ".", font= ("Arial", 18), command= lambda: button_click("."))
button_point.grid(row=4, column=2, sticky = tk.W+tk.E)

buttonframe.pack(fill="x")


root.mainloop()
