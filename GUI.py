from tkinter import *

root = Tk()
root.title('Тестовое приложение')
root.geometry('1280x720')
root.resizable(width = False, height = False)
root.iconbitmap('dice.ico')

# root.config(background= 'Black')

def click():
    print('Привет')

root['bg'] = 'Black'
label = Label(root,
    text = 'Текст',
    font = ('Comic Sans MS', 20, 'bold'),
    bg = 'lime',
    fg = 'black'
    )
label.place(x = 300, y = 200, anchor = 'center')

img = PhotoImage(file = 'python.png')
l_logo = Label(root, image=img)
l_logo.pack()





root.mainloop()
