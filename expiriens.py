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

def new_contact(phone_book,last_name,new_number,new_name='',description=''):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    Temp = "\n"+last_name+", "+new_name+", "+new_number+", "+description
    phone_book.append(dict(zip(fields,Temp.split(","))))
    return phone_book

def print_result(phone_book):
    for i in range(len(phone_book)):
        s=''
        for j in phone_book[i].values():
            s = s+j + ','
        print(f'{s[:-1]}')

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(s[:-1])

phone_book=read_txt('phon.txt')
last_name=input('Last name ')
new_name=input('Name ')
new_number=input('New number ')
description = input('Description ')
phone_book= new_contact(phone_book,last_name,new_number,new_name,description)
print_result(phone_book)
write_txt('phon.txt',phone_book)

#print_result(new_contact(phone_book,last_name,new_number,new_name,description))
