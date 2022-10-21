# метод записи в файл имени контакта

def logContact(z):
    with open('phone_directory.txt', 'a',  encoding='utf-8') as f:
        f.write(z)

# метода записи в файл номера контакта

def logDirect():
    direct = []
    with open('phone_directory.txt', 'r', encoding='utf-8') as f:
        for line in f:
            direct.append(line)
    return direct