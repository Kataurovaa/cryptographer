from tkinter import *
import tkinter as tk
from tkinter import messagebox

def start(flag):
    def decrypt():
        flag = 1

##################################################################################

    def encrypt():
        flag = 1
        def create_color(crypt):
            tmp = str(crypt)
            l = len(tmp)
            colors = []
            while l >= 6:
                t = tmp[l-6:]
                tmp = tmp[:l-6]
                colors.append(t)
                l -= 6
            if l == 0:
                return colors
            t = tmp
            while l < 6:
                t = "0" + t
                l += 1
            colors.append(t)
            return colors

        def print_color(colors):
            coord_x = 10 
            coord_x2 = 50
            for i in range(len(colors) - 1, -1, -1):
                mycolor = '#'+ colors[i]
                field.create_rectangle(coord_x, 170, coord_x2, 240, fill = mycolor)
                coord_x += 50
                coord_x2 += 50
################################################################################################

        def enter_message():
            s = message.get()
            tmp = to_10(s, 36)
            res = from_10(tmp, 16)
            print_color(create_color(res))

        def exit():
            for i in widgets_crypte:
                i.place_forget()
            start(flag)

        for i in widgets_main:
            i.place_forget()
        widgets_main.clear()

        widgets_crypte = []

        label_enter = Label(text = "Введите сообщение:", justify=CENTER, font="Verdana 14")
        label_enter.place(x = 100, y = 200)
        widgets_crypte.append(label_enter)
    
        message = StringVar()
        e = Entry(textvariable = message)
        e.place(x = 100, y = 50)
        widgets_crypte.append(e)

        button_enter = Button(text = "Ввод", command = enter_message)
        button_enter.place(x = 150, y = 50)
        widgets_crypte.append(button_enter)

        button_exit = Button(text = "Вернуться назад", command = exit)
        button_exit.place(x = 100, y = 300)
        widgets_crypte.append(button_exit)

    if flag == 0:
        root = Tk()
        root.resizable(width=False, height=False)
        field = Canvas(root, width=500, height=500, bg='white')
        field.pack()

    widgets_main = []

    greeting = Label(text = "Добро пожаловать в шифровальщик.\nВы хотите:", justify=CENTER, font="Verdana 14")
    greeting.place(x = 100, y = 200)
    widgets_main.append(greeting)

    button_encrypt = Button(command = encrypt, text = "Зашифровать", width = 20, height = 10)
    button_encrypt.place(x = 200, y = 300)
    widgets_main.append(button_encrypt)

    button_decrypt = Button(command = decrypt, text = "Расшифровать", width = 20, height = 10)
    button_decrypt.place(x = 200, y = 400)
    widgets_main.append(button_decrypt)
   










    if flag == 0:
        root.mainloop()

def to_10(inp, osn):
    p = 0
    digit = 0
    for i in range(len(inp)-1, -1, -1):
        tmp = ord(inp[i])
        if tmp >= 65:
            digit += (tmp-55) * osn**p
        else:
            digit += (tmp-48) * osn**p
        p += 1
    return digit

def from_10(inp, osn):
    digit = ""
    while inp > 0:
        tmp = inp % osn
        if tmp > 9:
            digit += str(chr(tmp+55))
        else:
            digit += str(tmp)
        inp //= osn
    return digit[::-1]




flag = 0
start(flag)
 
 

 
 

 

 
