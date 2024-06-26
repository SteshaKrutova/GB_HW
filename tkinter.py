from tkinter import *  
import tkinter as tk

def show_menu():
    print("\n Выберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить номер\n"
          "6. Удалить контакт по фамилии\n"
          "7. Копирование строки в новый файл\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(s[:-1])

#1 Вывод результата
def print_result(phone_book):
    s=''
    for i in range(len(phone_book)):
        for j in phone_book[i].values():
            s = s+j + ','
    return s

def clicked():  
    turn=read_txt('phon.txt')
    turn1=print_result(turn)
    lbl.configure(text=print_result(turn))  

def btn_print_result():
    turn=read_txt('phon.txt')
    turn1=print_result(turn)
    label = Label(window,text = turn1)
    label.grid(column=2, row=2) 
  
  
window = tk.Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('450x450+500+170')
window.resizable(False,False)
lbl = Label(window, text="Привет", font=("Arial Bold", 10))  
lbl.grid(column=0, row=0)  
btn1 = Button(window, text="Не нажимать", command=clicked)  
btn1.grid(column=1, row=1)  
btn2 = Button(window, text="Вывод справочника", command=btn_print_result)  
btn2.grid(column=1, row=0) 
window.mainloop()

