import tkinter as tk
from tkinter import ttk
import Inlägg as i
from GUI import GUI

#Återställ högersidan för att kunna visa ny sida
def rensa_höger():
    for widget in frame_right.winfo_children():
        widget.destroy()

#Återställ vänstersidan
def rensa_vänster():
    for widget in frame_left.winfo_children():
        widget.destroy()
    bygg_vänster()

def bygg_vänster():
    b1 = 'Öppna anteckningar'
    b2 = 'Skriv i journal'
    b3 = 'Hämta inlägg'
    if sida == 1:
        b1 = 'Stäng anteckningar'
    if sida == 2:
        b2 = 'Stäng journal'
    if sida == 3:
        b3 = 'Stäng inlägg'
    button1 = ttk.Button(frame_left, text=b1, command=öppna_kladd)
    button1.pack(padx=20, pady=20, fill='x')
    button2 = ttk.Button(frame_left, text=b2, command=öppna_journal)
    button2.pack(padx=20, pady=20, fill='x')
    button3 = ttk.Button(frame_left, text=b3, command=hämta)
    button3.pack(padx=20, pady=20, fill='x')

#Öppna och stäng anteckningar
def stäng():
    sida = 0
    root.geometry('400x600')
    rensa_vänster()

def öppna_kladd():
    sida = 1
    root.geometry('800x600')
    rensa_höger()
    rensa_vänster()

    textf = tk.Text(frame_right, height=20)
    textf.pack(padx=20, pady=5)
    textf.insert('1.0', i.Kladd.hämta())
    #scrollbar = ttk.Scrollbar(textf, orient='vertical', command=textf.yview)
    #textf['yscrollcommand'] = scrollbar.set

    save = ttk.Button(frame_right, text='Spara', command=lambda: spara_kladd(textf.get('1.0', 'end')))
    save.pack(pady=10)

    textf.focus()

def öppna_journal():
    sida = 2
    root.geometry('800x600')
    rensa_höger()
    rensa_vänster()

    rubrik_label = ttk.Label(frame_right, text='Rubrik:', style = 'TLabel')
    rubrik_label.pack(padx=20, pady=10, anchor='nw')

    rubrik = ttk.Entry(frame_right)
    rubrik.pack(padx=20, fill='x')

    text_label = ttk.Label(frame_right, text='Text:', style = 'TLabel')
    text_label.pack(padx=20, pady=5, anchor='nw')

    textf = tk.Text(frame_right, height=20)
    textf.pack(padx=20, pady=5)

    save = ttk.Button(frame_right, text='Spara', command=lambda: spara(rubrik.get(), textf.get('1.0', 'end')))
    save.pack(pady=10)

    rubrik.focus()

def spara(rubrik, text):
    inlägg = i.Journal(rubrik, text)
    inlägg.spara_till_fil() 

def spara_kladd(text):
    inlägg = i.Kladd(text)
    inlägg.spara()

def hämta():
    sida = 3
    root.geometry('800x600')
    rensa_höger()
    rensa_vänster()

    for x in i.Journal.hämta():
        label = ttk.Label(frame_right, text=x.get_rubrik(), style = 'TLabel')
        label['relief'] = 'raised'
        label.pack(padx=20, pady=5, fill='both')
        label.bind("<Button-1>", lambda event, obj=x: inlägg(obj))

#Visa enskilt journalinlägg
def inlägg(x):
    rensa_höger()
    label = ttk.Label(frame_right, text=f'{x.get_rubrik()} - {x.get_time()}', style = 'TLabel')
    label['font'] = ('Helvetica', 14)
    label.pack(padx=20, pady=20, fill='x')
    text = ttk.Label(frame_right, text=x.get_text(), style = 'TLabel')
    text.pack(padx=20, pady=20, fill='x')
    



#Håll koll på vilken sida vi är på - fungerar ej just nu - ändras aldrig (pga scope?)
sida = 0

#Skapa UI
root = tk.Tk()
root.title('Henkes Journalprojekt')
root.geometry('400x600')
root.resizable(False, False)
root['bg'] = 'brown'
root['padx'] = 20
root['pady'] = 20

s = ttk.Style()
s.configure('TFrame', background='tan')
s.configure('TLabel', background='tan', font=('Helvetica', 12))

frame_left = ttk.Frame(root, style = 'TFrame')
frame_left['relief'] = 'ridge'
frame_left.place(x=0, y=0, width=360, height=560)

bygg_vänster()

frame_right = ttk.Frame(root, style = 'TFrame')
frame_right['relief'] = 'ridge'
frame_right.place(x=400, y=0, width=360, height=560)


#Kör UI/program
root.mainloop()