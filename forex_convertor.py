import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

def convertcurr():
    try:
        x = amount.get()
        y = currency_from.get().upper()
        z = currency_to.get().upper()
        curr = CurrencyRates()
        f = curr.convert(y, z, x)
        final.set(format(f, '.2f'))
    except Exception as e:
        final.set("Error: " + str(e))

root = tk.Tk()
root.geometry('350x350')
root.title('Currency Converter')

# Variables
amount = tk.DoubleVar()
currency_from = tk.StringVar()
currency_to = tk.StringVar()
final = tk.StringVar()

# Input amount
tk.Label(root, text='Input amount', font='Times').grid(row=0, column=0, columnspan=5, sticky='NSEW')
q = ttk.Entry(root, textvariable=amount)
q.grid(row=1, column=1, columnspan=3, sticky='NSWE', padx=5, pady=5)

# Convert From
tk.Label(root, text='Convert From (USD, INR, EUR, GBP, etc)', font='Times').grid(row=2, column=0, columnspan=5, sticky='NSEW')
q = ttk.Entry(root, textvariable=currency_from)
q.grid(row=3, column=1, columnspan=3, sticky='NSWE', padx=5, pady=5)

# Convert To
tk.Label(root, text='Convert To (USD, INR, EUR, GBP, etc)', font='Times').grid(row=4, column=0, columnspan=5, sticky='NSEW')
q = ttk.Entry(root, textvariable=currency_to)
q.grid(row=5, column=1, columnspan=3, sticky='NSWE', padx=5, pady=5)

# Convert button
w = ttk.Button(root, text='Convert', command=convertcurr)
w.grid(row=7, column=2, padx=5, pady=5, sticky='NSWE')

# Converted amount
tk.Label(root, text='--Converted Amount--', font='Times').grid(row=10, column=1, columnspan=3, sticky='NSWE')
l = ttk.Label(root, textvariable=final, relief='groove')
l.grid(row=11, column=1, columnspan=3, sticky='NSWE')

root.mainloop()
