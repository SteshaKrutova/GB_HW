
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

print(read_txt('phon.txt'))