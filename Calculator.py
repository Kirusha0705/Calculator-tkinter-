import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = name.get()
    if value[0] == '0' and len(value)==1:
        value = value[1:]
    name.delete(0, tk.END)
    name.insert(0, value+digit)


def get_operation(operation):
    value = name.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        get_result()
        value = name.get()
    name.delete(0, tk.END)
    name.insert(0, value + operation)


def get_result():
    value = name.get()
    if value[-1] in '*-/+':
        value = value + value[:-1]
    name.delete(0, tk.END)
    try:
        name.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Вычисление невозможно. Введите цифры')
        name.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На 0 делить нельзя')
        name.insert(0, '0')


def del_all():
    name.delete(0, tk.END)
    name.insert(0, '0')

def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '*/-+':
        get_operation(event.char)
    elif event.char == '\r':
        get_result()




def get_button(digit: (str, int)):
    return tk.Button(text=digit, bd=5, font=('Arial', 15), command=lambda: add_digit(digit))


def get_operation_button(operation: str):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), command=lambda: get_operation(operation))


def get_equal_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 15), command=get_result)

def make_clear_button(letter):
    return tk.Button(text='C', bd=5, font=('Arial', 15), command=del_all)


win = tk.Tk()
win.geometry('237x270+900+100')
win['bg'] = 'green'
win.title('Калькулятор')

win.bind('<Key>', press_key)

name = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
name.insert(0, '0')
name.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

get_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
get_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
get_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
get_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
get_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
get_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
get_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
get_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
get_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
get_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

get_equal_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

get_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
get_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
get_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
get_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

for i in range(1, 5):
    win.grid_rowconfigure(i, minsize=60)

for i in range(0, 4):
    win.grid_columnconfigure(i, minsize=60)

win.mainloop()
