from tkinter import *
import tkinter as tk
from tkinter import messagebox
import easygui
from PIL import Image, ImageDraw 
                                      
def start(flag):
    def decrypt():
        def exit():
            for i in widgets_crypte:
                i.place_forget()
            start(flag)
#########################################################################################################################
        def open_file():
            de_colors = []
            input_file = easygui.fileopenbox(filetypes=["*.*"])
            image = Image.open(input_file)  # Открываем изображение
            draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
            width = image.size[0]  # Определяем ширину
            height = image.size[1]  # Определяем высоту
            pix = image.load()
            for x in range(0,1):
                for y in range(0,1):
                    s = ""
                    r = pix[x, y][0] #узнаём значение красного цвета пикселя
                    s += from_10(r, 16)
                    g = pix[x, y][1] #зелёного
                    s += from_10(g, 16)
                    b = pix[x, y][2] #синего
                    s += from_10(b, 16)
                    de_colors.append(s)
            answer = Label(text = color_to_text(de_colors))
            answer.place(x= 100, y = 100)
            widgets_crypte.append(answer)
#########################################################################################################################
        def color_to_text(colors):
            tmp = ""
            for i in colors:
                tmp += i
            d = to_10(tmp, 16)
            res = from_10(d, 36)
            return res
#########################################################################################################################
        for i in widgets_main:
            i.place_forget()
        widgets_main.clear()

        flag = 1
        widgets_crypte = []

        label_greet = Label(text = "Выберите файл с\nзашифрованным сообщением", justify=CENTER, font="Verdana 14")
        label_greet.place(x = 100, y = 200)
        widgets_crypte.append(label_greet)

        button_enter = Button(text = "Выбрать", command = open_file)
        button_enter.place(x = 150, y = 50)
        widgets_crypte.append(button_enter)

        button_exit = Button(text = "Вернуться назад", command = exit)
        button_exit.place(x = 100, y = 300)
        widgets_crypte.append(button_exit)

#########################################################################################################################

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

#########################################################################################################################

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

        label_enter = Label(text = "Введите сообщение:", justify=CENTER, font="Verdana 14", bg = 'white')
        label_enter.place(x = 80, y = 50)
        widgets_crypte.append(label_enter)
    
        message = StringVar()
        e = Text(textvariable = message, width = 50, height = 5)
        scroll = Scrollbar(command=e.yview)
        scroll.pack(side=LEFT, fill=Y)
        e.config(yscrollcommand=scroll.set)
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
        root.title("Шифровальщик")
        #root.resizable(width=False, height=False)
        field = Canvas(root, width=500, height=500, bg='white')
        field.pack()

    widgets_main = []

    greeting = Label(text = "Добро пожаловать в шифровальщик.\nВы хотите:", justify=CENTER, font="Verdana 14", bg = 'white')
    greeting.place(x = 60, y = 50)
    widgets_main.append(greeting)

    button_encrypt = Button(command = encrypt, text = "Зашифровать", width = 30, height = 3)
    button_encrypt.place(x = 135, y = 200)
    widgets_main.append(button_encrypt)

    button_decrypt = Button(command = decrypt, text = "Расшифровать", width = 30, height = 3)
    button_decrypt.place(x = 135, y = 300)
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
 
 

 
 

 

 
