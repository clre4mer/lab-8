import random
#импортирую библиотеку лога и провожу её стандартную настройку
import logging
logging.basicConfig(filename="secondLog.log", 
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%H: %M: %S',
                    level=logging.DEBUG)
#создаю функцию проверки на ошибки ввода
def errorCheck(n):
    try:
        n = int(n)
    except Exception:
        logging.error('Неверный ввод!')
        return -1
    return n
n=-1
#ввод количества бочёнков в мешке
while n ==-1:
    n = int(input('Введите количество бочёнков в мешке: \n'))
    n=errorCheck(n)
logging.info('Ввод значения прошёл успешно')
meshok = []
turn=0
#заполняю мешок боченками
for i in range(1,n+1):
    meshok.append(i)
logging.info('Мешок заполнен бочками')
#цикл достования случайного бочёнка из мешка
for i in range(1,n+1):
    j=1
    while j != 0:
        boch = random.randrange(1,n+1,1)
        for i1 in range (1,n+1-turn):
            if boch == meshok[i1-1]:
                print(f'Вытянут бочёнок под номером {boch}!\n')
                logging.info(f'Из мешка достали боченок под номером {boch}')
                meshok.pop(i1-1)
                turn = turn+1
                j=0
                print('Нажмите Enter для продолжения...\n')
                input('')
                break
print('Все бочёнки были вытянуты из мешка!')
logging.info('Из мешка достали все боченки')