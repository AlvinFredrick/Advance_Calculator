import tkinter as Tk
from tkinter import *
import math
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

expr = ""   # Global expression string

# ------------------ CALCULATOR FUNCTIONS ------------------
def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def clear():
    global expr
    expr = ""
    display.set("")

def backspace():
    global expr
    expr = expr[:-1]
    display.set(expr)

def equal():
    global expr
    try:
        calc = expr.replace("√", "math.sqrt") \
                   .replace("cbrt", "(lambda x: x**(1/3))") \
                   .replace("^", "**") \
                   .replace("sin", "math.sin") \
                   .replace("cos", "math.cos") \
                   .replace("tan", "math.tan") \
                   .replace("asin", "math.asin") \
                   .replace("acos", "math.acos") \
                   .replace("atan", "math.atan") \
                   .replace("sinh", "math.sinh") \
                   .replace("cosh", "math.cosh") \
                   .replace("tanh", "math.tanh") \
                   .replace("sec", "(lambda x: 1/math.cos(x))") \
                   .replace("cosec", "(lambda x: 1/math.sin(x))") \
                   .replace("cot", "(lambda x: 1/math.tan(x))") \
                   .replace("deg", "math.degrees") \
                   .replace("rad", "math.radians") \
                   .replace("log2", "math.log2") \
                   .replace("log1p", "math.log1p") \
                   .replace("expm1", "math.expm1") \
                   .replace("floor", "math.floor") \
                   .replace("ceil", "math.ceil") \
                   .replace("gamma", "math.gamma") \
                   .replace("mod", "%") \
                   .replace("π", "math.pi") \
                   .replace("e", "math.e")

        result = str(eval(calc))
        display.set(result)
        history_list.insert(END, expr + " = " + result)
        expr = ""
    except:
        display.set("**Error**")
        expr = ""

# ---------- SCIENTIFIC MODE TOGGLE ----------
def toggle_scientific():
    if sci_frame.winfo_ismapped():
        sci_frame.grid_remove()
        sci_button.config(text="Scientific Mode ON")
    else:
        sci_frame.grid()
        sci_button.config(text="Scientific Mode OFF")

# ------------------ PAGE MANAGEMENT ------------------
def show_frame(frame):
    for f in [calc_frame, currency_frame, length_frame, temp_frame, date_frame]:
        f.grid_remove()
    frame.grid(row=1, column=0, padx=10, pady=10)

# ------------------ MAIN WINDOW ------------------
root = Tk()
root.title("Advance Calculator")
root.resizable(False, False)

# ------------------ TOP MENU BUTTONS ------------------
menu_frame = Frame(root)
menu_frame.grid(row=0, column=0, pady=10)

Button(menu_frame, text="Calculator", width=12, command=lambda: show_frame(calc_frame)).grid(row=0, column=0, padx=5)
Button(menu_frame, text="Currency", width=12, command=lambda: show_frame(currency_frame)).grid(row=0, column=1, padx=5)
Button(menu_frame, text="Length", width=12, command=lambda: show_frame(length_frame)).grid(row=0, column=2, padx=5)
Button(menu_frame, text="Temperature", width=12, command=lambda: show_frame(temp_frame)).grid(row=0, column=3, padx=5)
Button(menu_frame, text="Date", width=12, command=lambda: show_frame(date_frame)).grid(row=0, column=4, padx=5)

# ================== CALCULATOR FRAME ==================
calc_frame = Frame(root, bd=2, relief="ridge")
# Display
display = StringVar()
Entry(calc_frame, textvariable=display, font=("Arial", 20), bd=8, relief="sunken", width=25, justify="right").grid(row=0, column=0, columnspan=5, pady=10)

# History panel
history_frame = Frame(calc_frame)
history_frame.grid(row=0, column=5, rowspan=10, padx=10)
Label(history_frame, text="History", font=("Arial", 13, "bold")).pack()
history_list = Listbox(history_frame, width=28, height=25, font=("Arial", 11))
history_list.pack()

# Buttons style
btn_config = {"fg": "White", "bg": "Gray20", "height": 1, "width": 7, "font": ("Arial", 12, "bold")}

# Standard Buttons
buttons = [
    ('C', clear), ('⌫', backspace), ('(', lambda: press("(")), (')', lambda: press(")")), ('÷', lambda: press("/")),
    ('7', lambda: press(7)), ('8', lambda: press(8)), ('9', lambda: press(9)), ('×', lambda: press("*")), ('-', lambda: press("-")),
    ('4', lambda: press(4)), ('5', lambda: press(5)), ('6', lambda: press(6)), ('+', lambda: press("+")), ('^', lambda: press("^")),
    ('1', lambda: press(1)), ('2', lambda: press(2)), ('3', lambda: press(3)), ('√', lambda: press("√(")), ('%', lambda: press("%")),
    ('0', lambda: press(0)), ('.', lambda: press(".")), ('π', lambda: press("π")), ('e', lambda: press("e")), ('=', equal)
]

row = 1
col = 0
for text, cmd in buttons:
    Button(calc_frame, text=text, command=cmd, **btn_config).grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Scientific Buttons
sci_frame = Frame(calc_frame)
# --- Row 1 ---
Button(sci_frame, text='sin', command=lambda: press("sin("), **btn_config).grid(row=0, column=0)
Button(sci_frame, text='cos', command=lambda: press("cos("), **btn_config).grid(row=0, column=1)
Button(sci_frame, text='tan', command=lambda: press("tan("), **btn_config).grid(row=0, column=2)
Button(sci_frame, text='asin', command=lambda: press("asin("), **btn_config).grid(row=0, column=3)
Button(sci_frame, text='acos', command=lambda: press("acos("), **btn_config).grid(row=0, column=4)
# --- Row 2 ---
Button(sci_frame, text='atan', command=lambda: press("atan("), **btn_config).grid(row=1, column=0)
Button(sci_frame, text='sinh', command=lambda: press("sinh("), **btn_config).grid(row=1, column=1)
Button(sci_frame, text='cosh', command=lambda: press("cosh("), **btn_config).grid(row=1, column=2)
Button(sci_frame, text='tanh', command=lambda: press("tanh("), **btn_config).grid(row=1, column=3)
Button(sci_frame, text='cbrt', command=lambda: press("cbrt("), **btn_config).grid(row=1, column=4)
# --- Row 3 ---
Button(sci_frame, text='sec', command=lambda: press("sec("), **btn_config).grid(row=2, column=0)
Button(sci_frame, text='cosec', command=lambda: press("cosec("), **btn_config).grid(row=2, column=1)
Button(sci_frame, text='cot', command=lambda: press("cot("), **btn_config).grid(row=2, column=2)
Button(sci_frame, text='deg', command=lambda: press("deg("), **btn_config).grid(row=2, column=3)
Button(sci_frame, text='rad', command=lambda: press("rad("), **btn_config).grid(row=2, column=4)
# --- Row 4 ---
Button(sci_frame, text='log', command=lambda: press("log("), **btn_config).grid(row=3, column=0)
Button(sci_frame, text='log2', command=lambda: press("log2("), **btn_config).grid(row=3, column=1)
Button(sci_frame, text='log1p', command=lambda: press("log1p("), **btn_config).grid(row=3, column=2)
Button(sci_frame, text='ln', command=lambda: press("ln("), **btn_config).grid(row=3, column=3)
Button(sci_frame, text='gamma', command=lambda: press("gamma("), **btn_config).grid(row=3, column=4)
# --- Row 5 ---
Button(sci_frame, text='x²', command=lambda: press("^2"), **btn_config).grid(row=4, column=0)
Button(sci_frame, text='x³', command=lambda: press("^3"), **btn_config).grid(row=4, column=1)
Button(sci_frame, text='xʸ', command=lambda: press("^"), **btn_config).grid(row=4, column=2)
Button(sci_frame, text='1/x', command=lambda: press("1/("), **btn_config).grid(row=4, column=3)
Button(sci_frame, text='!', command=lambda: press("math.factorial("), **btn_config).grid(row=4, column=4)

sci_frame.grid(row=row+1, column=0, columnspan=5)
sci_button = Button(calc_frame, text="Scientific Mode OFF", command=toggle_scientific,
                    bg="orange", fg="black", font=("Arial", 11, "bold"))
sci_button.grid(row=row+2, column=0, columnspan=5, pady=10)

# ================== CURRENCY FRAME ==================
currency_frame = Frame(root, bd=2, relief="ridge")
Label(currency_frame, text="Amount").grid(row=0, column=0)
amt = StringVar()
Entry(currency_frame, textvariable=amt).grid(row=0, column=1)
Label(currency_frame, text="From").grid(row=1,column=0)
frm = StringVar(value="USD")
Entry(currency_frame, textvariable=frm).grid(row=1,column=1)
Label(currency_frame, text="To").grid(row=2,column=0)
to = StringVar(value="INR")
Entry(currency_frame, textvariable=to).grid(row=2,column=1)
curr_result = StringVar()
Label(currency_frame, textvariable=curr_result).grid(row=4,column=0,columnspan=2)
def convert_currency():
    try:
        amount = float(amt.get())
        rates = {"USD":1,"INR":82,"EUR":0.93,"GBP":0.81,"JPY":148}
        res = amount / rates[frm.get()] * rates[to.get()]
        curr_result.set(f"{res:.2f} {to.get()}")
    except:
        messagebox.showerror("Error","Invalid input")
Button(currency_frame, text="Convert", command=convert_currency).grid(row=3,column=0,columnspan=2,pady=5)

# ================== LENGTH FRAME ==================
length_frame = Frame(root, bd=2, relief="ridge")
Label(length_frame, text="Length").grid(row=0,column=0)
length_val = StringVar()
Entry(length_frame, textvariable=length_val).grid(row=0,column=1)
Label(length_frame, text="Convert").grid(row=1,column=0)
length_type = StringVar(value="m to cm")
ttk.Combobox(length_frame, textvariable=length_type,
             values=["m to cm","cm to m","km to m","m to km","inch to cm","ft to m","yard to m"]).grid(row=1,column=1)
length_result = StringVar()
Label(length_frame, textvariable=length_result).grid(row=3,column=0,columnspan=2)
def convert_length():
    try:
        val = float(length_val.get())
        conv = length_type.get()
        factors = {"m":1,"cm":0.01,"km":1000,"inch":0.0254,"ft":0.3048,"yard":0.9144}
        val_in_m = val * factors[conv.split(" ")[0]]
        res = val_in_m / factors[conv.split(" ")[-1]]
        length_result.set(f"{res:.4f}")
    except:
        messagebox.showerror("Error","Invalid input")
Button(length_frame, text="Convert", command=convert_length).grid(row=2,column=0,columnspan=2,pady=5)

# ================== TEMPERATURE FRAME ==================
temp_frame = Frame(root, bd=2, relief="ridge")
Label(temp_frame, text="Temperature").grid(row=0,column=0)
temp_val = StringVar()
Entry(temp_frame, textvariable=temp_val).grid(row=0,column=1)
Label(temp_frame, text="Convert").grid(row=1,column=0)
temp_type = StringVar(value="C to F")
ttk.Combobox(temp_frame, textvariable=temp_type, values=["C to F","F to C","C to K","K to C"]).grid(row=1,column=1)
temp_result = StringVar()
Label(temp_frame, textvariable=temp_result).grid(row=3,column=0,columnspan=2)
def convert_temperature():
    try:
        t = float(temp_val.get())
        conv = temp_type.get()
        if conv=="C to F": r = t*9/5+32
        elif conv=="F to C": r = (t-32)*5/9
        elif conv=="C to K": r = t+273.15
        elif conv=="K to C": r = t-273.15
        temp_result.set(f"{r:.2f}")
    except:
        messagebox.showerror("Error","Invalid input")
Button(temp_frame, text="Convert", command=convert_temperature).grid(row=2,column=0,columnspan=2,pady=5)

# ================== DATE FRAME ==================
date_frame = Frame(root, bd=2, relief="ridge")
Label(date_frame, text="Date 1 (YYYY-MM-DD)").grid(row=0,column=0)
d1 = StringVar()
Entry(date_frame, textvariable=d1).grid(row=0,column=1)
Label(date_frame, text="Date 2 (YYYY-MM-DD)").grid(row=1,column=0)
d2 = StringVar()
Entry(date_frame, textvariable=d2).grid(row=1,column=1)
date_result = StringVar()
Label(date_frame, textvariable=date_result).grid(row=3,column=0,columnspan=2)
def calculate_date():
    try:
        date1 = datetime.strptime(d1.get(), "%Y-%m-%d")
        date2 = datetime.strptime(d2.get(), "%Y-%m-%d")
        diff = abs((date2 - date1).days)
        date_result.set(f"{diff} days")
    except:
        messagebox.showerror("Error","Use YYYY-MM-DD format")
Button(date_frame,text="Calculate Difference",command=calculate_date).grid(row=2,column=0,columnspan=2,pady=5)

# Show calculator page by default
show_frame(calc_frame)

root.mainloop()
