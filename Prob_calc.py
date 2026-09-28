from os import system

def Enter():
    input("Нажмите Enter чтобы продолжить")
    system('cls')
        
def Error():
    print('Некорретное число, попробуйте снова!')

def Prob_mult(): # Умножение вероятностей
    i = int(input('Выберите режим умножения:\n1 - Независимыe события\n2 - Зависисые события\n'))
    if i == 1:
        A = float(input('Введите вероятность события А: '))
        B = float(input('Введите вероятность события B: '))
        if Formula(A,B) and Prob_check(A,B):
            print('Вероятность, что оба события произойдут равна:', A * B)
    elif i == 2:
        A = float(input('Введите вероятность события А: '))
        B = float(input('Введите условную вероятность события B|A: '))
        
        print('Вероятность, что оба события произойдут равна:', A*(B))
    else:
        Error()
def Prob_add(): #Сложение вреоятностей
    i = int(input('Выберите режим сложения:\n1 - Несовместные события\n2 - Совместные события\n'))
    if i == 1:
        A = float(input('Введите вероятность события А: '))
        B = float(input('Введите вероятность события B: '))
        if (Formula(A,B) and Prob_check(A,B)): 
            print('Верятность, что произойдёт одно из событий равна:', A+B)
            if A+B > 1: 
                print('У вас где-то ошибка!(Вероятность не может быть больше еденицы!)')
    elif i == 2:
        i2 = int(input('1 - Независмиые события\n2- Зависимые события'))
        if i2 == 1:
            A = float(input('Введите вероятность события А: '))
            B = float(input('Введите вероятность события B: '))
            if Formula(A,B) and Prob_check(A,B):
                print('Верятность, произойдёт одно из событий равна:', A + B -(A * B))
        elif i2 == 2:
            A = float(input('Введите вероятность события А: '))
            B = float(input('Введите вероятность события B: '))
            A0B = float(input('Введите вероятность события, что А и Б произошли одновременно(P(A∩B)): '))
            if Formula(A,B,A0B) and Prob_check(A,B,A0B):
                print('Верятность, произойдёт одно из событий равна:', ((A + B) - A0B))
        else:
            Error()
    else:
        Error()
def Prob_check(*args): # Проверка чтобы вероятности не были больше единицы
    for x in args:
        if x > 1:
            print('Вероятность не может быть больше еденицы!')
            return False 
    return True
def Prob_at_least(): # Вероятность хотя бы одного в n попыток
    p = float(input(('Введите вероятность успеха в одной конкретной попытке: ')))
    n = int(input('Введите кол-во независимых испытаний: '))
    if Formula(p,n) and Prob_check(p):
            print('Вероятность того, что случайное событие произойдет хотя бы один раз равна:', (1-((1-p)**n)))

def Formula(*args): # Проверка чтобы все значения были не отрицательными
    for x in args:
        if x < 0:
            print('Все значения должны быть >= нуля!')
            return False
    return True
 
def Prob_easy(): # Определние вероятностей
    m = int(input('Введите число благоприятных исходов: '))
    n = int(input('Общее число всех возможных исходов: '))
    if Formula(m,n):
            print('Вероятность равна:', m/n)
    
def Start(): # Стартовая функция меню и всё такое
    start_inf1 = 'Выберети режим работы\n0 - Выход\n1 - Обычная вероятность(m/n)\n' 
    start_inf2 = '2 - Умножение вероятностей\n'
    start_inf3 = '3 - Сложение вероятностей\n'
    start_inf4 = '4 - Вероятность того, что случайное событие произойдет хотя бы один раз\n'
    start_inf = start_inf1 + start_inf2 + start_inf3 + start_inf4
    i = int(input(start_inf))

    if i == 0:
        exit()
    elif i == 1:
        Prob_easy()
    elif i == 2:
        Prob_mult()
    elif i == 3:
        Prob_add()
    elif i == 4:
        Prob_at_least()


while True:
    try:
        while True:
            Start() # Начало основного кода
            break
        Enter()
        Start()
        
        
    
    except ValueError: # Проверки всякие на ошибки, чтоб программа не падала!
        print('Введите целое число либо введите число через "."')
        Enter()
    except ZeroDivisionError:
        print('Число должно быть больше  нуля!')
        Enter()
            