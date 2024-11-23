import tkinter as tk
from fractions import Fraction
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import PhotoImage

root = tk.Tk()
root.title("Calculator")
tabControl = ttk.Notebook(root)
root.resizable(False, False)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Równania kwadratowe', padding="5")
tabControl.add(tab2, text='Tab 2', padding="5")
tabControl.pack(expand = 1, fill="both")
tabControl.columnconfigure(3, weight=2)
imageMath = PhotoImage(file="mathImg1.png")

global x1, x2
valueA_let = StringVar()
valueB_let = StringVar()
valueC_let = StringVar()

#UI ustawienia
paddings = {'padx':10, 'pady': 10}
# tab1.columnconfigure(0,weight=3)
# tab1.columnconfigure(1,weight=1)

#Imput A
inputA = ttk.Entry(tab1, width=7, textvariable=valueA_let)
inputA.grid(column=2, row=1)
#Label
ttk.Label(tab1, text="Podaj współczynnik A równania kwadratowego").grid(row=1, column=1, **paddings)

#Imput B
inputB = ttk.Entry(tab1, width=7, textvariable=valueB_let)
inputB.grid(column=2, row=2)
#Label
ttk.Label(tab1, text="Podaj współczynnik B równania kwadratowego").grid(row=2, column=1, **paddings)

#Imput C
inputC = ttk.Entry(tab1, width=7, textvariable=valueC_let)
inputC.grid(column=2, row=3)
#Label
ttk.Label(tab1, text="Podaj współczynnik C równania kwadratowego").grid(row=3, column=1, **paddings)

#Image
mathImage = ttk.Label(tab1, image=imageMath)
mathImage.grid(row=1, column=3, rowspan=3, columnspan=2, sticky="NS", **paddings)

#Suma
sume = ttk.Label(tab1, text="SUMA:", font=('calibe', 15, 'bold'))
sume.grid(row=4, column=1,columnspan=2, padx=10)

def clear_inputs():
    inputA.delete(0, END)
    inputB.delete(0, END)
    inputC.delete(0, END)
    sume.config(text="")

def submit():
    valueA = int(valueA_let.get())
    valueB = int(valueB_let.get())
    valueC = int(valueC_let.get())
    # Delta
    delta = valueB ** 2 - (4 * valueA * valueC)
    if type(valueA) == str or type(valueB) == str or type(valueC) == str:
        messageBoxReturn = messagebox.askretrycancel("Nieprawidłowa wartość", "Wartość musi być liczbą.")
        if messageBoxReturn is False:
            quit()
        else:
            clear_inputs()
    elif delta < 0:
        messageBoxReturn = messagebox.askretrycancel("Ujemna delta", f"Delta jest ujemna [{delta}], a to oznacza, że równanie nie ma żadnych rozwiązań")
        if messageBoxReturn is False:
            quit()
        else:
            clear_inputs()
    else:
        deltaElement = round(delta ** 0.5)
        # x1, x2
        x1 = Fraction((-valueB) - deltaElement, 2 * valueA)
        x2 = Fraction((-valueB) + deltaElement, 2 * valueA)
        # Lejbelka z wynikiem
        print(f"valueA - {valueA} valueB - {valueB} valueC - {valueC} delta - {delta} deltaElement - {deltaElement}")
        del valueA, valueB, valueC, delta, deltaElement
        return sume.config(text=f"SUMA X1: {x1} X2: {x2}")

#Przycisk calculate
ttk.Button(tab1, text='Calculate', command=submit).grid(row=4,column=3, **paddings)
ttk.Button(tab1, text='Clear', command=clear_inputs).grid(row=4, column=4, padx=10)

root.mainloop()