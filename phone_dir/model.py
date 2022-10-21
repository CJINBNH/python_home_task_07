# метод получения информации

def enterContactPhNum():
    name = input('Введите имя абонента: ')
    phone = input('Введите номер: ')
    return f'{name} || {phone} \n'


# метод получения информации для поиска

def searchContact(direct: list, cont: str) -> str:
    z = ''
    for i in direct:
        if i.find(cont) != -1:
            z = i
    if z == '':
        return "Контакт не найден"
    else:
        return z

# запрос контакта для поиска

def getRequest():
    return input('Введите имя контакта из записной книжки: ')

# выбор действия поиск или добавление

def typeAction():
    return int(input('Укажите операцию цифрой: поиск - 1; добавление - 2; выход - 0 \n'))

# метод поиска контакта в файле по имени
# def findCont(z):
#     with open('phone_directory.txt', 'r',  encoding='utf-8') as f:
#         f.read(z)