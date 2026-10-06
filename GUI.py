from customtkinter import *
from tkinter import ttk
from logic import Prob_easy
from tkinter import messagebox
from logic import Prob_mult
from logic import Prob_add_incomp
from logic import Prob_add_indep
from logic import Prob_add_dep
from logic import Prob_at_least
from logic import Prob_Bernoulli

def set_light():
    set_appearance_mode('light')

def set_dark():
    set_appearance_mode('dark')

def full_Prob_Bernoulli():
    try:
        n = int(entry_Bernoulli_n.get())
        k = int(entry_Bernoulli_k.get())
        p = float(entry_Bernoulli_p.get())
        result = Prob_Bernoulli(n,k,p)
        if Error_check(result):
            label_Bernoulli_result.configure(text='Вероятность того, что в серии из n независимых испытаний событие наступит ровно k раз равна:\n' + str(result))
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')
def full_Prob_at_least():
    try:
        p = float(entry_at_least_p.get())
        n = int(entry_at_least_n.get())
        result = Prob_at_least(p,n)
        if Error_check(result):
            label_at_least_result.configure(text='Вероятность того, что случайное событие произойдет хотя бы один раз равна:\n'+ str(result))
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')
def full_Prob_add_dep():
    try:
        A = float(entry_add_depA.get())
        B = float(entry_add_depB.get())
        A0B = float(entry_add_depA0B.get())
        result = Prob_add_dep(A,B,A0B)
        if Error_check(result):
            label_add_dep_result.configure(text='Вероятность, что произойдёт одно из событий равна: ' + str(result))
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')

def full_Prob_add_indep():
    try:
        A = float(entry_add_indepA.get())
        B = float(entry_add_indepB.get())
        result = Prob_add_indep(A,B)
        if Error_check(result):
            label_add_indep_result.configure(text='Вероятность, что произойдёт одно из событий равна: '+ str(result))
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')
def full_Prob_add_incomp():
    try:
        A = float(entry_add_incompA.get())
        B = float(entry_add_incompB.get())
        result = Prob_add_incomp(A,B)
        if Error_check(result):
            label_add_incomp_result.configure(text='Вероятность, что произойдёт одно из событий равна: '+ str(result))
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')
def forget_add():
    if frame_add_incomp.winfo_ismapped():
        frame_add_incomp.pack_forget()
    if frame_add_indep.winfo_ismapped():
        frame_add_indep.pack_forget()
    if frame_add_dep.winfo_ismapped():
        frame_add_dep.pack_forget()
def Prob_add_dep_visual():
    forget_add()
    frame_add_dep.pack()
    label_add_depA.pack()
    entry_add_depA.pack()
    label_add_depB.pack()
    entry_add_depB.pack()
    label_add_depA0B.pack()
    entry_add_depA0B.pack()
    btn_add_dep.pack()
    label_add_dep_result.pack()

def Prob_add_indep_visual():
    forget_add()
    frame_add_indep.pack()
    label_add_indepA.pack()
    entry_add_indepA.pack()
    label_add_indepB.pack()
    entry_add_indepB.pack()
    btn_add_indep.pack()
    label_add_indep_result.pack()

def Prob_add_incomp_visual():
    forget_add()
    frame_add_incomp.pack()
    label_add_incompA.pack()
    entry_add_incompA.pack()
    label_add_incompB.pack()
    entry_add_incompB.pack()
    btn_add_incomp.pack()
    label_add_incomp_result.pack()

def full_Prob_mult_indep():
    try:
        A = float(entry_indep_Prob_multiA.get())
        B = float(entry_indep_Prob_multiB.get())
        result = Prob_mult(A,B)
        if Error_check(result):
            label_indep_result.configure(text='Вероятность равна: ' + str(result))
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')
        
def full_Prob_mult_dep():
    try:
        A = float(entry_dep_Prob_multiA.get())
        B = float(entry_dep_Prob_multiB.get())
        result = Prob_mult(A,B)
        if Error_check(result):
            label_dep_result.configure(text='Вероятность равна: ' + str(result))
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
    elif result == 'Error:higher1_add':
        messagebox.showerror('Ошибка','Вероятность при сложении не может быть больше единицы')
        return False
    elif result == 'Error:belowzero_add':
        messagebox.showerror('Ошибка','Вероятность при сложении не может быть меньше нуля')
        return False
    elif result == 'Error:notsatisfy_Bernoulli':
        messagebox.showerror('Ошибка','Ваши числа не выполняют условие k <= n')
    return True
def full_Prob_easy():
    try:
        m = int(enter_Prob_easy_m.get())
        n = int(enter_Prob_easy_n.get())
        result = Prob_easy(m,n)
        if Error_check(result):
            label_Prob_easy_result.configure(text = 'Вероятность равна: '+ str(result))
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

root = CTk()
root.geometry('940x400')
root.resizable(width = False, height = False)
root.title('Калькулятор вероятностей')
root.iconbitmap('Dice.ico') 
set_appearance_mode("light")

tab_control = CTkTabview(root)
tab_control.pack(fill='both', expand=True)

tab_main = tab_control.add('Главная')
tab1 = tab_control.add('Простая вероятность')
tab2 = tab_control.add('Умножение вероятностей')
tab3 = tab_control.add('Сложение вероятностей')
tab4 = tab_control.add('Вероятность хотя бы раз из n')
tab5 = tab_control.add('Вероятность k успехов из n')


label_Prob_easy_m = CTkLabel(tab1, text='Введите число благоприятных исходов: ')
label_Prob_easy_m.pack()

enter_Prob_easy_m = CTkEntry(tab1)
enter_Prob_easy_m.pack()

label_Prob_easy_n = CTkLabel(tab1, text='Общее число всех возможных исходов: ')
label_Prob_easy_n.pack()

enter_Prob_easy_n = CTkEntry(tab1)
enter_Prob_easy_n.pack()

button_Prob_easy = CTkButton(tab1, text='Вычислить', command = full_Prob_easy)
button_Prob_easy.pack()



label_Prob_easy_result = CTkLabel(tab1, text = 'Вероятность равна:')
label_Prob_easy_result.pack()

label_tab2 = CTkLabel(tab2, text='Выберите режим вычисления:').pack()


var = IntVar(value = 1)

radbtn_indep = CTkRadioButton(tab2, text='Независимые события', variable=var, value=1, command=indep_visual).pack()
radbtn_dep = CTkRadioButton(tab2, text='Зависимые события    ', variable=var, value = 2, command=dep_visual).pack()

frame_indep_visual = CTkFrame(tab2)
label_indep_Prob_multiA = CTkLabel(frame_indep_visual, text='Введите вероятность события А: ')
entry_indep_Prob_multiA = CTkEntry(frame_indep_visual)
label_indep_Prob_multiB = CTkLabel(frame_indep_visual, text='Введите вероятность события B: ')
entry_indep_Prob_multiB = CTkEntry(frame_indep_visual)
btn_indep_visual = CTkButton(frame_indep_visual, text='Вычислить', command=full_Prob_mult_indep)
label_indep_result = CTkLabel(frame_indep_visual, text='Вероятность равна:')

frame_indep_visual.pack()
label_indep_Prob_multiA.pack()
entry_indep_Prob_multiA.pack()
label_indep_Prob_multiB.pack()
entry_indep_Prob_multiB.pack()
btn_indep_visual.pack()
label_indep_result.pack()

frame_dep_visual = CTkFrame(tab2)
label_dep_Prob_multiA = CTkLabel(frame_dep_visual, text='Введите вероятность события А: ')
entry_dep_Prob_multiA = CTkEntry(frame_dep_visual)
label_dep_Prob_multiB = CTkLabel(frame_dep_visual, text='Введите вероятность события B|A: ')
entry_dep_Prob_multiB = CTkEntry(frame_dep_visual)
btn_dep_visual = CTkButton(frame_dep_visual, text='Вычислить', command=full_Prob_mult_dep)
label_dep_result = CTkLabel(frame_dep_visual, text='Вероятность равна:')

label_add_incomp = CTkLabel(tab3, text='Выберите режим вычисления:')
label_add_incomp.pack()


var_add = IntVar(value=1)

radbtn_add_incomp = CTkRadioButton(tab3, variable=var_add, value=1, text='Несовместные события', command=Prob_add_incomp_visual).pack()
radbtn_add_comp_indep = CTkRadioButton(tab3, variable=var_add, value=2, text='Совместные и независимые события', command=Prob_add_indep_visual).pack()
radbtn_add_comp_dep = CTkRadioButton(tab3, variable=var_add, value=3, text='Совместные и зависимые события', command=Prob_add_dep_visual).pack()

frame_add_incomp = CTkFrame(tab3)

label_add_incompA = CTkLabel(frame_add_incomp, text='Введите вероятность события А: ')
entry_add_incompA = CTkEntry(frame_add_incomp)
label_add_incompB = CTkLabel(frame_add_incomp, text='Введите вероятность события B: ')
entry_add_incompB = CTkEntry(frame_add_incomp)
btn_add_incomp = CTkButton(frame_add_incomp, text='Вычислить', command=full_Prob_add_incomp)
label_add_incomp_result = CTkLabel(frame_add_incomp, text='Вероятность, что произойдёт одно из событий равна: ')

frame_add_incomp.pack()
label_add_incompA.pack()
entry_add_incompA.pack()
label_add_incompB.pack()
entry_add_incompB.pack()
btn_add_incomp.pack()
label_add_incomp_result.pack()

frame_add_indep = CTkFrame(tab3)
label_add_indepA = CTkLabel(frame_add_indep, text='Введите вероятность события А: ')
entry_add_indepA = CTkEntry(frame_add_indep)
label_add_indepB = CTkLabel(frame_add_indep, text='Введите вероятность события B: ')
entry_add_indepB = CTkEntry(frame_add_indep)
btn_add_indep = CTkButton(frame_add_indep, text='Вычислить', command=full_Prob_add_indep)
label_add_indep_result = CTkLabel(frame_add_indep, text='Вероятность, что произойдёт одно из событий равна: ')

frame_add_dep = CTkFrame(tab3)
label_add_depA = CTkLabel(frame_add_dep, text='Введите вероятность события А: ')
entry_add_depA = CTkEntry(frame_add_dep)
label_add_depB = CTkLabel(frame_add_dep, text='Введите вероятность события B: ')
entry_add_depB = CTkEntry(frame_add_dep)
label_add_depA0B = CTkLabel(frame_add_dep, text='Введите вероятность события, что А и Б произошли одновременно(P(A∩B))')
entry_add_depA0B = CTkEntry(frame_add_dep)
btn_add_dep = CTkButton(frame_add_dep, text='Вычислить', command=full_Prob_add_dep)
label_add_dep_result = CTkLabel(frame_add_dep, text='Вероятность, что произойдёт одно из событий равна: ')

frame_at_least = CTkFrame(tab4)
label_at_leat_p = CTkLabel(frame_at_least, text='Введите вероятность успеха события в каждом отдельном испытании: ')
entry_at_least_p = CTkEntry(frame_at_least)
label_at_least_n = CTkLabel(frame_at_least, text='Введите кол-во независимых испытаний: ')
entry_at_least_n = CTkEntry(frame_at_least)
btn_at_least = CTkButton(frame_at_least, text='Вычислить', command=full_Prob_at_least)
label_at_least_result = CTkLabel(frame_at_least, text='Вероятность того, что случайное событие произойдет хотя бы один раз равна:')

frame_at_least.pack()
label_at_leat_p.pack()
entry_at_least_p.pack()
label_at_least_n.pack()
entry_at_least_n.pack()
btn_at_least.pack()
label_at_least_result.pack()

frame_Bernoulli = CTkFrame(tab5)
label_Bernoulli_n = CTkLabel(frame_Bernoulli, text='Введите общее число независимых испытаний: ')
entry_Bernoulli_n = CTkEntry(frame_Bernoulli)
label_Bernoulli_k = CTkLabel(frame_Bernoulli, text='Введите число успехов события: ')
entry_Bernoulli_k = CTkEntry(frame_Bernoulli)
label_Bernoulli_p = CTkLabel(frame_Bernoulli, text='Введите вероятность успеха события в каждом отдельном испытании: ') 
entry_Bernoulli_p = CTkEntry(frame_Bernoulli)
btn_Bernoulli = CTkButton(frame_Bernoulli, text='Вычислить', command=full_Prob_Bernoulli)
label_Bernoulli_result = CTkLabel(frame_Bernoulli, text='Вероятность того, что в серии из n независимых испытаний событие наступит ровно k раз равна: ')


frame_Bernoulli.pack()
label_Bernoulli_n.pack()
entry_Bernoulli_n.pack()
label_Bernoulli_k.pack()
entry_Bernoulli_k.pack()
label_Bernoulli_p.pack()
entry_Bernoulli_p.pack()
btn_Bernoulli.pack()
label_Bernoulli_result.pack()


title = CTkLabel(tab_main, text='Калькулятор вероятностей', font =('Arial', 16, 'bold'))
title.pack(pady=20)

Name = CTkLabel(tab_main,font=('Times New Roman', 16),text='Для индивидуального проекта разработал:\nученик 9 "Б" класса\nМБОУ СОШ №2\nНовиков Артём\n')
Name.pack()

var_theme = IntVar(value=1)

label_theme = CTkLabel(tab_main, text='Выберите тему:')

rdbtn_set_light = CTkRadioButton(tab_main,text='Светлая',variable=var_theme, value=1, command=set_light)
rdbtn_set_dark = CTkRadioButton(tab_main,text='Тёмная',variable=var_theme, value=2, command=set_dark)


rdbtn_set_light.pack(side='bottom')
rdbtn_set_dark.pack(side='bottom', pady=6)
label_theme.pack(side='bottom', pady=8)

root.mainloop()
