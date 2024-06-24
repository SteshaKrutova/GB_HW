def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phon.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            number=input('print number ')
            print(find_by_number(phone_book,number))
        elif choice==4:
            last_name=input('Last name ')
            new_name=input('Name ')
            new_number=input('New number ')
            description = input('Description ')
            phone_book= new_contact(phone_book,last_name,new_number,new_name,description)
            print_result(phone_book)
        elif choice==5:
            last_name=input('Lastname: ')
            new_number=input('New  number: ')
            print_result(change_number(phone_book,last_name,new_number))
        elif choice==6:
            lastname=input('lastname ')
            delete_by_lastname(phone_book,lastname)
        elif choice==7:
            break
        choice=show_menu()

def show_menu():
    print("\n Выберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить номер\n"
          "6. Удалить контакт по фамилии\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    #line.split(',') ==['Питонов',    'Антон',     '777',    'умеет в Питон']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
            phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(s[:-1])

#1
def print_result(phone_book):
    for i in range(len(phone_book)):
        s=''
        for j in phone_book[i].values():
            s = s+j + ','
        print(f'{s[:-1]}')

#2
def find_by_lastname(phone_book,last_name):
    for i in range(len(phone_book)):
        if phone_book[i]["Фамилия"] ==last_name:
            return " ".join(phone_book[i].values())
        
#3       
def find_by_number(phone_book,number):
    for i in range(len(phone_book)):
        if phone_book[i]['Телефон'][1:] == number:
            return " ".join(phone_book[i].values())
        
#4
def new_contact(phone_book,last_name,new_number,new_name='',description=''):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    Temp = "\n"+last_name+", "+new_name+", "+new_number+", "+description
    phone_book.append(dict(zip(fields,Temp.split(","))))
    write_txt('phon.txt',phone_book)
    return phone_book

#5 Изменение номера контакта
def change_number (phone_book,last_name,new_number):
    new_number= " "+ new_number
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия']==last_name:
            phone_book[i]['Телефон']=new_number
    write_txt('phon.txt',phone_book)
    return phone_book

#6 Удаление контакта по фамилии
def delete_by_lastname(phone_book,lastname):
    for i in range(len(phone_book)):
        if phone_book[i-1]["Фамилия"]==lastname:
            phone_book.pop(i-1)
            write_txt('phon.txt', phone_book)
            print_result(phone_book)
            return phone_book
    print("Данной фамилии не существует")

work_with_phonebook()