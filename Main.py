import tkinter as tk
from tkinter import ttk
import Inlägg as i
#from GUI import GUI

#Gå från omslag till basic GUI
def start(self):
    frame_left.place(x=0, y=0, width=360, height=560)
    bygg_vänster()
    root['bg'] = '#8b4513'
    root['padx'] = 20
    root['pady'] = 20
    cover.destroy()

#Återställ högersidan för att kunna visa ny sida
def rensa_höger():
    for widget in frame_right.winfo_children():
        widget.destroy()

#Återställ vänstersidan
def rensa_vänster():
    for widget in frame_left.winfo_children():
        widget.destroy()
    bygg_vänster()

#Skapa vänstersidan
def bygg_vänster():
    # b1 = 'Öppna anteckningar' @TODO
    # b2 = 'Skriv i journal'
    # b3 = 'Hämta inlägg'
    # if sida == 1:
    #     b1 = 'Stäng anteckningar'
    # if sida == 2:
    #     b2 = 'Stäng journal'
    # if sida == 3:
    #     b3 = 'Stäng inlägg'
    buttonlabel1 = ttk.Label(frame_left, text=b1, anchor='center', relief='raised', style='Button.TLabel')
    buttonlabel1.pack(padx=20, pady=20, ipadx=10, ipady=10, fill='x')
    buttonlabel1.bind("<Button-1>", öppna_kladd)
    buttonlabel2 = ttk.Label(frame_left, text=b2, anchor='center', relief='raised', style='Button.TLabel')
    buttonlabel2.pack(padx=20, pady=20, ipadx=10, ipady=10, fill='x')
    buttonlabel2.bind("<Button-1>", öppna_journal)
    buttonlabel3 = ttk.Label(frame_left, text=b3, anchor='center', relief='raised', style='Button.TLabel')
    buttonlabel3.pack(padx=20, pady=20, ipadx=10, ipady=10, fill='x')
    buttonlabel3.bind("<Button-1>", hämta)

#Stäng höger - inget länkar hit @TODO
def stäng(self):
    #sida = 0
    root.geometry('400x600')
    rensa_vänster()


def öppna_kladd(self):
    #sida = 1
    root.geometry('800x600')
    rensa_höger()
    rensa_vänster()

    textf = tk.Text(frame_right, height=20, font=('Lucida Calligraphy', 12))
    textf.pack(padx=20, pady=20)
    textf.insert('1.0', i.Kladd.hämta())

    #Kanske ska användas - får se @TODO
    #scrollbar = ttk.Scrollbar(textf, orient='vertical', command=textf.yview)
    #textf['yscrollcommand'] = scrollbar.set

    savebutton = ttk.Label(frame_right, text='Spara', anchor='center', relief='raised', style='Button.TLabel')
    savebutton.pack(padx=20, pady=20, ipadx=20, ipady=10, fill='x')
    savebutton.bind("<Button-1>", lambda event: spara_kladd(textf.get('1.0', 'end')))

    textf.focus()

def öppna_journal(self):
    #sida = 2
    root.geometry('800x600')
    rensa_höger()
    rensa_vänster()

    rubrik_label = ttk.Label(frame_right, text='Rubrik:', style = 'TLabel', background='#faf0e6')
    rubrik_label.pack(padx=20, pady=20, anchor='w')

    rubrik = ttk.Entry(frame_right, font=('Lucida Calligraphy', 12))
    rubrik.pack(padx=20, fill='x')

    text_label = ttk.Label(frame_right, text='Text:', style = 'TLabel', background='#faf0e6')
    text_label.pack(padx=20, pady=14, anchor='w')

    textf = tk.Text(frame_right, height=15, font=('Lucida Calligraphy', 12))
    textf.pack(padx=20)

    savebutton = ttk.Label(frame_right, text='Spara', anchor='center', relief='raised', style='Button.TLabel')
    savebutton.pack(padx=20, pady=20, ipadx=10, ipady=10, fill='x')
    savebutton.bind("<Button-1>", lambda event: spara(rubrik.get(), textf.get('1.0', 'end')))

    rubrik.focus()

#Spara texter samt gå tillbaka
def spara_kladd(text):
    inlägg = i.Kladd(text)
    inlägg.spara()
    sparat(1)

def spara(rubrik, text):
    inlägg = i.Journal(rubrik, text)
    inlägg.spara_till_fil()
    sparat(2)

def sparat(x):
    rensa_höger()
    sparat = ttk.Label(frame_right, text='Sparat!', style = 'TLabel')
    sparat.pack(padx=20, pady=20, anchor='center')
    tillbaka = ttk.Label(frame_right, text='Gå tillbaka', anchor='center', relief='raised', style='Button.TLabel')
    tillbaka.pack(padx=20, pady=20, ipadx=10, ipady=10, fill='x')
    if x==1:
        tillbaka.bind('<Button-1>', öppna_kladd)
    else:
        tillbaka.bind('<Button-1>', öppna_journal)

#Hämta och lista alla sparade inlägg
def hämta(self):
    #sida = 3
    root.geometry('800x600')
    rensa_höger()
    rensa_vänster()

    for x in i.Journal.hämta():
        label = ttk.Label(frame_right, text=x.get_rubrik(), style='Button.TLabel')
        label['relief'] = 'raised'
        label.pack(padx=20, pady=10, fill='both')
        label.bind("<Button-1>", lambda event, obj=x: inlägg(obj))

#Visa enskilt journalinlägg
def inlägg(x):
    rensa_höger()
    rubrik = ttk.Label(frame_right, text=x.get_rubrik(), style = 'TLabel')
    rubrik['font'] = ('Lucida Calligraphy', 14)
    rubrik.pack(padx=20, pady=20, fill='x')
    tid = ttk.Label(frame_right, text=x.get_time(), style = 'TLabel')
    tid['font'] = ('Lucida Calligraphy', 10)
    tid.pack(padx=20, pady=5, fill='x')
    text = ttk.Label(frame_right, text=x.get_text(), style = 'TLabel')
    text.pack(padx=20, pady=20, fill='x')

#Håll koll på vilken sida vi är på - fungerar ej just nu - ändras aldrig (pga scope?) @TODO
#sida = 0

#Skapa UI
root = tk.Tk()
root.title('Henkes Journalprojekt')
root.geometry('400x600')
root.resizable(False, False)
img = tk.PhotoImage(file='Cover.png')
cover = ttk.Label(root, image=img)
cover.pack()
cover.bind("<Button-1>", start)

s = ttk.Style()
s.configure('TFrame', background='#faf0e6')
s.configure('TLabel', background='#faf0e6', font=('Lucida Calligraphy', 12))
s.configure('Button.TLabel', background='#f5deb3', font=('Lucida Calligraphy', 12))

frame_left = ttk.Frame(root, style = 'TFrame')
frame_left['relief'] = 'ridge'

frame_right = ttk.Frame(root, style = 'TFrame')
frame_right['relief'] = 'ridge'
frame_right.place(x=400, y=0, width=360, height=560)

#Kör UI/program
root.mainloop()