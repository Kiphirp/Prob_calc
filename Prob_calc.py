def Formula(*args):
    for x in args:
        if x <=0:
            return False
    return True
 
def Prob(m,n):
    if not Formula(m,n):
        print('Все значения должны быть больше нуля!')
        
    else: return m/n
try:
    m = int(input('Введите число благоприятных исходов: '))
    n = int(input('Общее число всех возможных исходов: '))
    print(Prob(m,n))
        
            
except ValueError:
    print('Введите целое число')

    