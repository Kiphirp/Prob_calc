from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Вкладки')
root.geometry('400x250')
root.resizable(width=False, height = False)

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая')

lb1 =Label(tab1, text='Вкладка 1')
lb1.grid(column=0, row=0)

lb2 = Label(tab2, text='Вкладка 2')
lb2.grid(column=0, row=0)

tab_control.pack(expand=1, fill= 'both')



root.mainloop()





# root = Tk()
# root.title('Тестовое приложение')
# root.geometry('500x500')
# root.resizable(width = False, height = False)
# root.iconbitmap('dice.ico')
# 
# # root.config(background= 'Black')
# 
# # def click():
# #     print('Привет')
# 
# root['bg'] = 'Black'
# # label = Label(root,  (Button)
# #     text = 'Текст',
# #     font = ('Comic Sans MS', 20, 'bold'),
# #     bg = 'lime',
# #     fg = 'black'
# #     )
# # label.place(x = 300, y = 200, anchor = 'center')
# # 
# # img = PhotoImage(file = 'python.png')
# # l_logo = Label(root, image=img)
# # l_logo.pack()
# 
# # def add():
# #     e.insert(END, 'Hello')
# #     
# # def dele():
# #     e.delete(0,END)
# # 
# # def get():
# #     label1['text'] = e.get()
# # 
# # e = Entry(root, show='*')
# # e.pack()
# # 
# # e.insert(0, 'Hello')
# # e.insert(END, ' привет')
# # 
# # 
# # btn = Button(root, font='Arial 15', text='insert', command=add)
# # btn.pack()
# # 
# # btn1 = Button(root, font='Arial 15', text='delete', command=dele)
# # btn1.pack()
# # 
# # btn2 = Button(root, font='Arial 15', text='get', command=get)
# # btn2.pack()
# # 
# # label1 = Label(root, bg='black', fg='white')
# # label1.pack()
# 
# 
# frame_top =Frame(root)
# frame_top.pack()
# 
# label1 = Label(frame_top, width=7, height=4, bg='brown', text= '1')
# label1.pack(side=LEFT)
# label2 = Label(frame_top, width=7, height=4, bg='blue', text= '2')
# label2.pack(side=LEFT)
# 
# frame_bottom =Frame(root)
# frame_bottom.pack()
# 
# label3 = Label(frame_bottom, width=7, height=4, bg='yellow', text= '3')
# label3.pack(side=LEFT)
# label4 = Label(frame_bottom, width=7, height=4, bg='pink', text= '4')
# label4.pack(side=LEFT)
# 
# root.mainloop()
