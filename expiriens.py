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

def print_result(phone_book):
    for i in range(len(phone_book)):
        s=''
        for j in phone_book[i].values():
            s = s+j + ','
        print(s[:-1])

def delete_by_lastname(phone_book,lastname):
    for i in range(len(phone_book)):
        if phone_book[i-1]["Фамилия"]==lastname:
            phone_book.pop(i-1)
            write_txt('phon.txt', phone_book)
            print_result(phone_book)
            return phone_book
    print("Данной фамилии не существует")


user_data=input('new data ')
add_user(phone_book,user_data)
write_txt('phonebook.txt',phone_book)

phone_book=read_txt('phon.txt')

print_result(phone_book)
print('-----')
lastname='Петров'
delete_by_lastname(phone_book,lastname)
