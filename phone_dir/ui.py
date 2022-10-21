import logger
import model

while True:
    mode = model.typeAction()
    if mode == 1:
        cont = model.getRequest()
        direct = logger.logDirect()
        print(model.searchContact(direct, cont))
    elif mode == 2:
        logger.logContact(model.enterContactPhNum())
    elif mode == 0:
        print('Выход')
        break
    else:
        print('Выберете вариант действий из предложенных')

# def choiceAction():
#     data = int(input('Если хотите добавить контакт в справочник введите: 1, - а если найти, то введите 2'))
#     if data == 'enter':
#         enterContact(data)
#         enterPhNum(data)
#     else:
#         searchContact(data)



# # метод вывода информации
# def showContact(z):
#     print(z)

# # введение имени пользователем
# enterCont = enterContact()
# logger.logContact(enterCont)

# # введение номера пользователем
# phoneNum = enterPhNum()
# logger.logPhNum(phoneNum)

# # вывод запрашиваемого пользователем контакта
# searchCont = model.searchContact()
# searchRes = model.findCont(searchCont)
# showContact(searchRes)