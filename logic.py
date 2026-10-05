from os import system
# raise
from math import comb

def Prob_Bernoulli():
    n = int(input('Введите общее число независимых испытаний: '))
    k = int(input('Введите число успехов события: '))
    p = float(input('Введите вероятность успеха события в каждом отдельном испытании: '))
    if Formula(n,k,p) and Prob_check(p):
        if k <= n:
            print('Вероятность того, что в серии из n независимых испытаний событие наступит ровно k раз равна: ', end='')
            print((comb(n,k))*(p**k)*((1-p)**(n-k)))
        else:
            print('Ваши числа не выполняют условия k <= n!')
        
def Enter():
    input("Нажмите Enter чтобы продолжить")
    system('cls')
        


def Prob_mult(A,B): # Умножение вероятностей
    if not Formula(A,B):
        return 'Error:belowzero' 
    if not Prob_check(A,B):
        return 'Error:higher1'
    return A*B  

def Prob_add_incomp(A,B): #Сложение вреоятностей
    if not Formula(A,B):
        return 'Error:belowzero' 
    if not Prob_check(A,B):
        return 'Error:higher1'
    if A+B > 1: 
        return 'Error:higher1_add'
    return A+B
    
def Prob_add_indep(A,B):
    if not Formula(A,B):
        return 'Error:belowzero' 
    if not Prob_check(A,B):
        return 'Error:higher1'
    if Formula(A,B) and Prob_check(A,B):
         return A + B -(A * B)
        
def Prob_add_dep(A,B,A0B):
    if not Formula(A,B,A0B):
        return 'Error:belowzero' 
    if not Prob_check(A,B,A0B):
        return 'Error:higher1'
    if ((A + B) - A0B) > 1:
        return 'Error:higher1_add'
    if ((A + B) - A0B) < 0:
        return 'Error:belowzero_add'
    if Formula(A,B,A0B) and Prob_check(A,B,A0B):
        return (A + B) - A0B
        
def Prob_check(*args): # Проверка чтобы вероятности не были больше единицы
    for x in args:
        if x > 1:
            return False 
    return True
def Prob_at_least(): # Вероятность хотя бы одного в n попыток
    p = float(input(('Введите вероятность успеха события в каждом отдельном испытании: ')))
    n = int(input('Введите кол-во независимых испытаний: '))
    if Formula(p,n) and Prob_check(p):
            print('Вероятность того, что случайное событие произойдет хотя бы один раз равна:', (1-((1-p)**n)))


def Formula(*args): # Проверка чтобы все значения были не отрицательными
    for x in args:
        if x < 0:
#             print('Все значения должны быть >= нуля!')
            return False
    return True

def Prob_easy(m,n): # Определние вероятностей 
    if Formula(m,n):
        if m<=n:
            return m/n
        else:
            return 'Error:notsatisfy_easy'
#            print('Ваши числа не выполняют условие m <= n')
    return 'Error:belowzero'

            
