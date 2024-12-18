#Buoc 1: Nhap thu vien

from tkinter import *
import math
import tkinter.messagebox
#Buoc 2: Khoi tao CUA SO WINDOW
window = Tk()
window.title("Scientific Calculator")
window.configure(background='white')
window.resizable(width=False, height=False)
window.geometry("480x568")
calc = Frame(window)
calc.grid()
#Buoc3: Tao Backend
class backendmaytinh():

    # Buoc 3.1: Khoi tao gia tri
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    # Buoc 3.2: Tao cach thuc nhap so
    def numberEnter(self, num):
        self.result = False
        if self.input_value:
            self.current = str(num)
            self.input_value = False
        else:
            if str(num) == '.' and '.' in self.current:
                return
            self.current += str(num)
        self.display(self.current)

    # Buoc 3.3: thiet ket dau bang
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(display.get())

    # Buoc 3.4: Thiet ke hien thi
    def display(self, value):
        display.delete(0, END)
        display.insert(0, value)

    # Buoc 3.5: Tinh toan phep tinh
    def valid_function(self):
        operations = {
            "add": lambda x, y: x + y,
            "sub": lambda x, y: x - y,
            "multi": lambda x, y: x * y,
            "divide": lambda x, y: x / y,
            "mod": lambda x, y: x % y
        }
        self.total = operations[self.op](self.total, self.current)
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    # Buoc3.6: ten phep toan
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    # Buoc 3.7: Xoa dong dang viet
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    # Buoc 3.8: Xoa toan bo du lieu
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    # Buoc 3.9: Tao cac gia tri toan hoc
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(display.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(display.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(display.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(display.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(display.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(display.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(display.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(display.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(display.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(display.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(display.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(display.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(display.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(display.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(display.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(display.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(display.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(display.get()))
        self.display(self.current)


added_value = backendmaytinh()
#Buoc 4: Thiet ke nut bam
def create_button(text, row, column, bg="powder blue", fg="black", width=6, height=2, font=('Helvetica', 20, 'bold'), command=None,colspan=1):
    button = Button(calc, text=text, width=width, height=height, bg=bg, fg=fg, font=font, bd=4, command=command)
    button.grid(row=row, column=column, columnspan=colspan, pady=1)
    return button


def key_event_handler(event):
    key = event.char
    if key.isdigit() or key == '.':
        added_value.numberEnter(key)
    elif key == '+':
        added_value.operation("add")
    elif key == '-':
        added_value.operation("sub")
    elif key == '*':
        added_value.operation("multi")
    elif key == '/':
        added_value.operation("divide")
    elif key == '\r':
        added_value.sum_of_total()
    elif key.lower() == 'c':
        added_value.Clear_Entry()
    elif key == "=":
        added_value.sum_of_total()

window.bind("<Key>", key_event_handler)


# Number buttons
numberpad = "789456123"
i = 0
for j in range(2, 5):
    for k in range(3):
        create_button(numberpad[i], j, k, bg="black", fg="white", command=lambda x=numberpad[i]: added_value.numberEnter(x))
        i += 1

# Functional buttons
create_button("C", 1, 0, command=added_value.Clear_Entry)
create_button("CE", 1, 1, command=added_value.All_Clear_Entry)
create_button("\u221A", 1, 2, command=added_value.squared)
create_button("+", 1, 3, command=lambda: added_value.operation("add"))
create_button("-", 2, 3, command=lambda: added_value.operation("sub"))
create_button("x", 3, 3, command=lambda: added_value.operation("multi"))
create_button("/", 4, 3, command=lambda: added_value.operation("divide"))
create_button("0", 5, 0, bg="black", fg="white", command=lambda: added_value.numberEnter(0))
create_button(".", 5, 1, command=lambda: added_value.numberEnter("."))
create_button(chr(177), 5, 2, command=added_value.mathPM)
create_button("=", 5, 3, command=added_value.sum_of_total)
create_button("ngu",6,1,bg="black", fg="white", command=added_value.sum_of_total)

# Scientific buttons
scientific_buttons = [
    ("pi", added_value.pi), ("Cos", added_value.cos), ("tan", added_value.tan), ("sin", added_value.sin),
    ("2pi", added_value.tau), ("Cosh", added_value.cosh), ("tanh", added_value.tanh), ("sinh", added_value.sinh),
    ("log", added_value.log), ("exp", added_value.exp), ("Mod", lambda: added_value.operation("mod")), ("e", added_value.e),
    ("log10", added_value.log10), ("log1p", added_value.log1p), ("expm1", added_value.expm1), ("gamma", added_value.lgamma),
    ("log2", added_value.log2), ("deg", added_value.degrees), ("acosh", added_value.acosh), ("asinh", added_value.asinh)
]

row, col = 1, 4
for text, cmd in scientific_buttons:
    create_button(text, row, col, bg="black", fg="white", command=cmd)
    col += 1
    if col > 7:
        col = 4
        row += 1

#Buoc 5: Thiet ke Entry
display = Entry(calc, font=('Helvetica', 20, 'bold'),
                bg='black', fg='white',
                bd=30, width=28, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4, pady=1)
display.insert(0, "0")

lblDisplay = Label(calc, text="MÁY TÍNH KHOA HỌC",
                   font=('Helvetica', 30, 'bold'),
                   bg='black', fg='white', justify=CENTER)

lblDisplay.grid(row=0, column=4, columnspan=4)
#Buoc 6: Thiet ke Menubar
def exit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit ?")
    if iExit > 0:
        window.destroy()
        return

def Scientific():
    window.resizable(width=False, height=False)
    window.geometry("944x568")

def Standard():
    window.resizable(width=False, height=False)
    window.geometry("480x568")


menubar = Menu(calc)

# MenuBar 1 :
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_command(label="Scientific", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)

# MenuBar 2 :
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

window.config(menu=menubar)


window.mainloop()
