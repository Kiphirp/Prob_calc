from tkinter import *
from tkinter import ttk
from logic import Prob_easy
from tkinter import messagebox
from logic import Prob_mult

def full_Prob_mult_indep():
    try:
        A = float(entry_indep_Prob_multiA.get())
        B = float(entry_indep_Prob_multiB.get())
        result = Prob_mult(A,B)
        if Error_check(result):
            label_indep_result.config(text='Вероятность равна: ' + str(result))
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')
        
def full_Prob_mult_dep():
    try:
        A = float(entry_dep_Prob_multiA.get())
        B = float(entry_dep_Prob_multiB.get())
        result = Prob_mult(A,B)
        if Error_check(result):
            label_dep_result.config(text='Вероятность равна: ' + str(result))
    except ValueError:
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')
        
def Error_check(result):
    if result == 'Error:belowzero':
        messagebox.showerror('Ошибка','Все значения должны быть >= нуля!')
        return False
    elif result == 'Error:notsatisfy_easy':
        messagebox.showerror('Ошибка','Ваши числа не выполняют условие m <= n')
        return False
    elif result == 'Error:higher1':
        messagebox.showerror('Ошибка','Вероятность не может быть больше единицы')
        return False
    return True
def full_Prob_easy():
    try:
        m = int(enter_Prob_easy_m.get())
        n = int(enter_Prob_easy_n.get())
        result = Prob_easy(m,n)
        if Error_check(result):
            label_Prob_easy_result.config(text = 'Вероятность равна: '+ str(result))
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'Нельзя делить на ноль!')
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')

def forget():
    if frame_indep_visual.winfo_ismapped():
        frame_indep_visual.pack_forget()
    if frame_dep_visual.winfo_ismapped():
        frame_dep_visual.pack_forget()

def indep_visual():
    forget()
    frame_indep_visual.pack()
    label_indep_Prob_multiA.pack()
    entry_indep_Prob_multiA.pack()
    label_indep_Prob_multiB.pack()
    entry_indep_Prob_multiB.pack()
    btn_indep_visual.pack()
    label_indep_result.pack()
def dep_visual():
    forget()
    frame_dep_visual.pack()
    label_dep_Prob_multiA.pack()
    entry_dep_Prob_multiA.pack()
    label_dep_Prob_multiB.pack()
    entry_dep_Prob_multiB.pack()
    btn_dep_visual.pack()
    label_dep_result.pack()

root = Tk()
root.geometry('1000x500')
root.resizable(width = False, height = False)
root.title('Калькулятор вероятностей')
root.iconbitmap('Dice.ico') 

tab_control = ttk.Notebook(root)
tab_control.pack()

tab_main = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab_main, text = 'Главная')
tab_control.add(tab1, text = 'Простая вероятность')
tab_control.add(tab2, text = 'Умножение вероятностей')


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

label_tab2 = Label(tab2, text='Выберите режим вычисления:').pack()




var = IntVar(value = 1)

radbtn_indep = Radiobutton(tab2, text='Независимые события', variable=var, value=1, command=indep_visual, takefocus=0).pack()
radbtn_dep = Radiobutton(tab2, text='Зависимые события    ', variable=var, value = 2, command=dep_visual, takefocus=0).pack()

frame_indep_visual = Frame(tab2)
label_indep_Prob_multiA = Label(frame_indep_visual, text='Введите вероятность события А: ')
entry_indep_Prob_multiA = Entry(frame_indep_visual)
label_indep_Prob_multiB = Label(frame_indep_visual, text='Введите вероятность события B: ')
entry_indep_Prob_multiB = Entry(frame_indep_visual)
btn_indep_visual = Button(frame_indep_visual, text='Вычислить', command=full_Prob_mult_indep)
label_indep_result = Label(frame_indep_visual, text='Вероятность равна:')

frame_indep_visual.pack()
label_indep_Prob_multiA.pack()
entry_indep_Prob_multiA.pack()
label_indep_Prob_multiB.pack()
entry_indep_Prob_multiB.pack()
btn_indep_visual.pack()
label_indep_result.pack()

frame_dep_visual = Frame(tab2)
label_dep_Prob_multiA = Label(frame_dep_visual, text='Введите вероятность события А: ')
entry_dep_Prob_multiA = Entry(frame_dep_visual)
label_dep_Prob_multiB = Label(frame_dep_visual, text='Введите вероятность события B|A: ')
entry_dep_Prob_multiB = Entry(frame_dep_visual)
btn_dep_visual = Button(frame_dep_visual, text='Вычислить', command=full_Prob_mult_dep)
label_dep_result = Label(frame_dep_visual, text='Вероятность равна:')


root.mainloop()


