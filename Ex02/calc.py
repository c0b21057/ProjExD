import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event): 
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num) 


def click_equal(event):
    try:
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "計算不可")

def click_allclear(event):
    entry.delete(0, tk.END)


root = tk.Tk() 
root.geometry("300x500")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") 
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0 
numbers = list(range(9, -1, -1)) 
operators = ["+","-","*","/","(",")"] 
for i, num in enumerate(numbers+operators, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=1)
    btn.bind("<1>", click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

btn = tk.Button(root, text=f"=", font=("", 30), width=4, height=1)
btn.bind("<1>", click_equal)
btn.grid(row=r, column=c)

btn = tk.Button(root, text=f"AC", font=("", 30), width=4, height=1)
btn.bind("<1>", click_allclear)
btn.grid(row=6, column=2)

root.mainloop()