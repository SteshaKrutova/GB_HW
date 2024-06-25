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
        print((i+1),"- ", s[:-1])

def transfer(phone_book,line_number,new_file="new_file"):
    line_number = int(line_number) -1
    Turn=list(phone_book[line_number].values())
    with open(new_file,'w',encoding='utf=8')  as phot:
        s=''
        for i in range(len(Turn)):
            s+=Turn[i]+" "
        phot.write(s)
    

phone_book=read_txt('phon.txt')

print_result(phone_book)
print('-----')
# line_number=input('line_number:')
# new_file=input('New file')
# if new_file =='':
#     transfer(phone_book, line_number)
# else:
#     transfer(phone_book, line_number,new_file)