from tkinter import *
from tkinter import ttk
from logic import Prob_easy
from tkinter import messagebox
 
def full_Prob_easy():
    try:
        m = int(enter_Prob_easy_m.get())
        n = int(enter_Prob_easy_n.get())
        result = Prob_easy(m,n)
        if result == 'Error:belowzero':
            messagebox.showerror('Ошибка','Все значения должны быть >= нуля!')
        elif result == 'Error:notsatisfy':
            messagebox.showerror('Ошибка','Ваши числа не выполняют условие m <= n')
        else:
            label_Prob_easy_result.config(text = 'Вероятность равна:'+ str(result))
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'Нельзя делить на ноль!')
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')
    
root = Tk()
root.geometry('1000x500')
root.resizable(width = False, height = False)
root.title('Калькулятор вероятностей')
root.iconbitmap('Dice.ico')

tab_control = ttk.Notebook(root)
tab_control.pack()

tab_main = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)

tab_control.add(tab_main, text = 'Главная')
tab_control.add(tab1, text = 'Простая вероятность')



label_Prob_easy_m = Label(tab1, text='Введите число благоприятных исходов: ')
label_Prob_easy_m.pack()

enter_Prob_easy_m = Entry(tab1)
enter_Prob_easy_m.pack()

label_Prob_easy_n = Label(tab1, text='Общее число всех возможных исходов: ')
label_Prob_easy_n.pack()

enter_Prob_easy_n = Entry(tab1)
enter_Prob_easy_n.pack()

button_Prob_easy = Button(tab1, text='Вычислить', command = full_Prob_easy)
button_Prob_easy.pack()



label_Prob_easy_result = Label(tab1, text = 'Вероятность равна:')
label_Prob_easy_result.pack()



root.mainloop()


