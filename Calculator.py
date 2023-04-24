from tkinter import *
def bind_key():
    window.bind("<Return>", lambda event: equals())
    for key in range(10):
        window.bind(str(key), lambda event, button=key: button_press(Button))

    window.bind(".", lambda event: button_press("."))
    window.bind("+", lambda event: button_press("+"))
    window.bind("-", lambda event: button_press("-"))
    window.bind("*", lambda event: button_press("*"))
    window.bind("/", lambda event: button_press("/"))

    window.bind("1", lambda event: button_press("1"))
    window.bind("2", lambda event: button_press("2"))
    window.bind("3", lambda event: button_press("3"))
    window.bind("4", lambda event: button_press("4"))
    window.bind("5", lambda event: button_press("5"))
    window.bind("6", lambda event: button_press("6"))
    window.bind("7", lambda event: button_press("7"))
    window.bind("8", lambda event: button_press("8"))
    window.bind("9", lambda event: button_press("9"))
    window.bind("0", lambda event: button_press("0"))



def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total
    except SyntaxError:

        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:

        equation_label.set("arithmetic error")
        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("Calculator Program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

botton1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
botton1.grid(row=0, column=0)

botton2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
botton2.grid(row=0, column=1)

botton3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
botton3.grid(row=0, column=2)

botton4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
botton4.grid(row=1, column=0)

botton5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
botton5.grid(row=1, column=1)

botton6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
botton6.grid(row=1, column=2)

botton7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
botton7.grid(row=2, column=0)

botton8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
botton8.grid(row=2, column=1)

botton9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
botton9.grid(row=2, column=2)

botton0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
botton0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equel = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equel.grid(row=3, column=2)

dot = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
dot.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.pack()

bind_key()

window.mainloop()
