import tkinter as tk
import random
from tkinter import messagebox

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo('Mensagem', 'Então ele é !!!!!!')
    root.destroy()

def denied():
    button_1.place_forget()


root = tk.Tk()
root.title('Tu ess??')
root.geometry('600x600')
root.configure(background='#ffc8dd')

margin = tk.Canvas(root, width=500, bg='#ffc8dd', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = tk.Label(root, bg='#ffc8dd', text='Você é gay?', fg='#590d22', font=('Montserrat', 8, 'bold'))
text_id.pack()

button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=denied, relief=tk.RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)

button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=tk.RIDGE, bd=3, command=accepted, font=('Montserrat', 8, 'bold'))
button_2.pack()

root.mainloop()
