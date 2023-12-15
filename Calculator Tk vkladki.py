import tkinter as tk
from tkinter import ttk
from math import pi

def calc_rashod():
    delta1 = 0.098066 * float(e_delta1.get().replace(',', '.')) 
    plotn1 = float(e_plotn1.get().replace(',', '.'))
    diam1 = float(e_diam1.get().replace(',', '.'))
    mu1 = float(e_mu1.get().replace(',', '.')) 
    S = pi * (diam1 /2)**2
    result1 = str(round(60 * mu1 * S * ((2 * delta1)/ plotn1) ** (1/2), 2))
    label1 = tk.Label(tab1,text = 'Расход жидкости = ' + result1 + ' л/мин', font=('Arial', 15))
    label1.grid(row=5, column=0, columnspan=2)

def calc_perepad():
    rashod2 = float(e_rashod2.get().replace(',', '.'))
    plotn2 = float(e_plotn2.get().replace(',', '.'))
    diam2 = float(e_diam2.get().replace(',', '.'))
    mu2 = float(e_mu2.get().replace(',', '.')) 
    S = pi * (diam2 /2)**2
    result2 = str(round(((((rashod2 / (60 * mu2 * S)) ** 2)*plotn2) / 2) / 0.098066, 2))
    label2 = tk.Label(tab2,text = 'Перепад давления = ' + result2 + ' кгс/см2', font=('Arial', 15))
    label2.grid(row=5, column=0, columnspan=2)    

def calc_leak():
    delta3 = 0.098066 * float(e_delta3.get().replace(',', '.')) 
    zazor = float(e_zazor.get().replace(',', '.'))
    diam3 = float(e_diam3.get().replace(',', '.'))
    Kvyazk = float(e_Kvyazk.get().replace(',', '.')) 
    plotn3 = float(e_plotn3.get().replace(',', '.'))
    Lz = float(e_Lz.get().replace(',', '.'))
    Lk = float(e_Lk.get().replace(',', '.'))
    Nk = float(e_Nk.get().replace(',', '.'))
    leak = str(round((delta3 * pi * diam3 * (zazor ** 3)) / (2 * (plotn3 * Kvyazk * (10 ** -6)) * (Lz - (Lk * Nk)) * (10 ** 5)), 2))
    label3 = tk.Label(tab3,text = 'Утечки по зазору = ' + leak + ' см3/мин', font=('Arial', 15))
    label3.grid(row=9, column=0, columnspan=2)


okno = tk.Tk()     
okno.title("Расчет расхода жидкости")    
okno.geometry("555x450")
okno.resizable(height=False, width=False)

tabs = ttk.Notebook(okno)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tab3 = ttk.Frame(tabs)
tabs.add(tab1, text = 'Расход')
tabs.add(tab2, text = 'Перепад')
tabs.add(tab3, text = 'Утечки через кольцевой зазор')
tabs.grid(row=0, column=0)


l_delta1 = tk.Label(tab1, text = 'Перепад давления, кгс/см2', font=('Arial', 15))
l_delta1.grid(row=0, column=0, padx=5, pady=5)
l_plotn1 = tk.Label(tab1, text = 'Плотность жидкости, кг/м3', font=('Arial', 15))
l_plotn1.grid(row=1, column=0, padx=5, pady=5)
l_diam1 = tk.Label(tab1, text = 'Диаметр отверстия, мм', font=('Arial', 15))
l_diam1.grid(row=2, column=0, padx=5, pady=5)
l_mu1 = tk.Label(tab1, text = 'Коэффициент расхода', font=('Arial', 15))
l_mu1.grid(row=3, column=0, padx=5, pady=5)

e_delta1 = tk.Entry(tab1, font=('Arial', 15))
e_delta1.grid(row=0, column=1)
e_plotn1 = tk.Entry(tab1, font=('Arial', 15))
e_plotn1.grid(row=1, column=1)
e_diam1 = tk.Entry(tab1, font=('Arial', 15))
e_diam1.grid(row=2, column=1)
e_mu1 = tk.Entry(tab1, font=('Arial', 15))
e_mu1.grid(row=3, column=1)

r_btn1 = tk.Button(tab1, text = 'Расчет', bd=3, command=calc_rashod, font=('Arial', 15), background='#D8C8FF')
r_btn1.grid(row=4, column=0, columnspan=2,sticky='we', padx=5, pady=5)


l_rashod2 = tk.Label(tab2, text = 'Расход, л/мин', font=('Arial', 15))
l_rashod2.grid(row=0, column=0, padx=5, pady=5)
l_plotn2 = tk.Label(tab2, text = 'Плотность жидкости, кг/м3', font=('Arial', 15))
l_plotn2.grid(row=1, column=0, padx=5, pady=5)
l_diam2 = tk.Label(tab2, text = 'Диаметр отверстия, мм', font=('Arial', 15))
l_diam2.grid(row=2, column=0, padx=5, pady=5)
l_mu2 = tk.Label(tab2, text = 'Коэффициент расхода', font=('Arial', 15))
l_mu2.grid(row=3, column=0, padx=5, pady=5)

e_rashod2 = tk.Entry(tab2, font=('Arial', 15))
e_rashod2.grid(row=0, column=1)
e_plotn2 = tk.Entry(tab2, font=('Arial', 15))
e_plotn2.grid(row=1, column=1)
e_diam2 = tk.Entry(tab2, font=('Arial', 15))
e_diam2.grid(row=2, column=1)
e_mu2 = tk.Entry(tab2, font=('Arial', 15))
e_mu2.grid(row=3, column=1)

r_btn2 = tk.Button(tab2, text = 'Расчет', bd=3, command=calc_perepad, font=('Arial', 15), background='#D3FFCC')
r_btn2.grid(row=4, column=0, columnspan=2,sticky='we', padx=5, pady=5)


l_delta3 = tk.Label(tab3, text = 'Перепад давления, кгс/см2', font=('Arial', 15))
l_delta3.grid(row=0, column=0, padx=5, pady=5)
l_zazor = tk.Label(tab3, text = 'Радиальный зазор, мкм', font=('Arial', 15))
l_zazor.grid(row=1, column=0, padx=5, pady=5)
l_diam3 = tk.Label(tab3, text = 'Диаметр золотника, мм', font=('Arial', 15))
l_diam3.grid(row=2, column=0, padx=5, pady=5)
l_Kvyazk = tk.Label(tab3, text = 'Кинематическая вязкость, сСт', font=('Arial', 15))
l_Kvyazk.grid(row=3, column=0, padx=5, pady=5)
l_plotn3 = tk.Label(tab3, text = 'Плотность жидкости, кг/м3', font=('Arial', 15))
l_plotn3.grid(row=4, column=0, padx=5, pady=5)
l_Lz = tk.Label(tab3, text = 'Длина зазора вдоль оси, мм', font=('Arial', 15))
l_Lz.grid(row=5, column=0, padx=5, pady=5)
l_Lk = tk.Label(tab3, text = 'Длина разгрузочной канавки, мм', font=('Arial', 15))
l_Lk.grid(row=6, column=0, padx=5, pady=5)
l_Nk = tk.Label(tab3, text = 'Количество разгрузочных канавок', font=('Arial', 15))
l_Nk.grid(row=7, column=0, padx=5, pady=5)

e_delta3 = tk.Entry(tab3, font=('Arial', 15))
e_delta3.grid(row=0, column=1)
e_zazor = tk.Entry(tab3, font=('Arial', 15))
e_zazor.grid(row=1, column=1)
e_diam3 = tk.Entry(tab3, font=('Arial', 15))
e_diam3.grid(row=2, column=1)
e_Kvyazk = tk.Entry(tab3, font=('Arial', 15))
e_Kvyazk.insert(0,'10')
e_Kvyazk.grid(row=3, column=1)
e_plotn3 = tk.Entry(tab3, font=('Arial', 15))
e_plotn3.insert(0,'860')
e_plotn3.grid(row=4, column=1)
e_Lz = tk.Entry(tab3, font=('Arial', 15))
e_Lz.grid(row=5, column=1)
e_Lk = tk.Entry(tab3, font=('Arial', 15))
e_Lk.grid(row=6, column=1)
e_Nk = tk.Entry(tab3, font=('Arial', 15))
e_Nk.grid(row=7, column=1)

r_btn3 = tk.Button(tab3, text = 'Расчет', bd=3, command=calc_leak, font=('Arial', 15), background='#FFFFCC')
r_btn3.grid(row=8, column=0, columnspan=2,sticky='we', padx=5, pady=5)


okno.mainloop()