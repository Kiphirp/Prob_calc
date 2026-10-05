from tkinter import *
from tkinter import ttk
from logic import Prob_easy
from tkinter import messagebox
from logic import Prob_mult
from logic import Prob_add_incomp
from logic import Prob_add_indep
from logic import Prob_add_dep

def full_Prob_add_dep():
    try:
        A = float(entry_add_depA.get())
        B = float(entry_add_depB.get())
        A0B = float(entry_add_depA0B.get())
        result = Prob_add_dep(A,B,A0B)
        if Error_check(result):
            label_add_dep_result.config(text='Верятность, что произойдёт одно из событий равна: ' + str(result))
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')

def full_Prob_add_indep():
    try:
        A = float(entry_add_indepA.get())
        B = float(entry_add_indepB.get())
        result = Prob_add_indep(A,B)
        if Error_check(result):
            label_add_indep_result.config(text='Верятность, что произойдёт одно из событий равна: '+ str(result))
    except ValueError: 
        messagebox.showerror('Ошибка', 'Введите целое число либо введите число через "."')
def full_Prob_add_incomp():
    try:
        A = float(entry_add_incompA.get())
        B = float(entry_add_incompB.get())
        result = Prob_add_incomp(A,B)
        if Error_check(result):
            label_add_incomp_result.config(text='Верятность, что произойдёт одно из событий равна: '+ str(result))
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
    elif result == 'Error:higher1_add':
        messagebox.showerror('Ошибка','Вероятность при сложении не может быть больше единицы')
        return False
    elif result == 'Error:belowzero_add':
        messagebox.showerror('Ошибка','Вероятность при сложении не может быть меньше нуля')
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
tab3 = ttk.Frame(tab_control)

tab_control.add(tab_main, text = 'Главная')
tab_control.add(tab1, text = 'Простая вероятность')
tab_control.add(tab2, text = 'Умножение вероятностей')
tab_control.add(tab3, text = 'Сложение вероятностей')

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

var_add = IntVar(value=1)

radbtn_add_incomp = Radiobutton(tab3, variable=var_add, value=1, text='Несовместные события', takefocus=0, command=Prob_add_incomp_visual).pack()
radbtn_add_comp_indep = Radiobutton(tab3, variable=var_add, value=2, text='Совместные и независимые события', takefocus=0, command=Prob_add_indep_visual).pack()
radbtn_add_comp_dep = Radiobutton(tab3, variable=var_add, value=3, text='Совместные и зависимые события', takefocus=0, command=Prob_add_dep_visual).pack()

frame_add_incomp = Frame(tab3)
label_add_incompA = Label(frame_add_incomp, text='Введите вероятность события А: ')
entry_add_incompA = Entry(frame_add_incomp)
label_add_incompB = Label(frame_add_incomp, text='Введите вероятность события B: ')
entry_add_incompB = Entry(frame_add_incomp)
btn_add_incomp = Button(frame_add_incomp, text='Вычислить', command=full_Prob_add_incomp)
label_add_incomp_result = Label(frame_add_incomp, text='Верятность, что произойдёт одно из событий равна: ')

frame_add_incomp.pack()
label_add_incompA.pack()
entry_add_incompA.pack()
label_add_incompB.pack()
entry_add_incompB.pack()
btn_add_incomp.pack()
label_add_incomp_result.pack()

frame_add_indep = Frame(tab3)
label_add_indepA = Label(frame_add_indep, text='Введите вероятность события А: ')
entry_add_indepA = Entry(frame_add_indep)
label_add_indepB = Label(frame_add_indep, text='Введите вероятность события B: ')
entry_add_indepB = Entry(frame_add_indep)
btn_add_indep = Button(frame_add_indep, text='Вычислить', command=full_Prob_add_indep)
label_add_indep_result = Label(frame_add_indep, text='Верятность, что произойдёт одно из событий равна: ')

frame_add_dep = Frame(tab3)
label_add_depA = Label(frame_add_dep, text='Введите вероятность события А: ')
entry_add_depA = Entry(frame_add_dep)
label_add_depB = Label(frame_add_dep, text='Введите вероятность события B: ')
entry_add_depB = Entry(frame_add_dep)
label_add_depA0B = Label(frame_add_dep, text='Введите вероятность события, что А и Б произошли одновременно(P(A∩B))')
entry_add_depA0B = Entry(frame_add_dep)
btn_add_dep = Button(frame_add_dep, text='Вычислить', command=full_Prob_add_dep)
label_add_dep_result = Label(frame_add_dep, text='Верятность, что произойдёт одно из событий равна: ')

root.mainloop()

