import tkinter as tk
from tkinter import ttk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Henkes Journalprojekt')
        self.geometry('400x600')
        self.resizable(False, False)
        self['bg'] = 'brown'
        self['padx'] = 20
        self['pady'] = 20

        self.sida = 0

        s = ttk.Style()
        s.configure('TFrame', background='tan')
        s.configure('TLabel', background='tan', font=('Helvetica', 12))

        frame_left = ttk.Frame(self, style = 'TFrame')
        frame_left['relief'] = 'ridge'
        frame_left.place(x=0, y=0, width=360, height=560)

        self.bygg_vänster()

        frame_right = ttk.Frame(self, style = 'TFrame')
        frame_right['relief'] = 'ridge'
        frame_right.place(x=400, y=0, width=360, height=560)

    def bygg_vänster(self):
        b1 = 'Öppna anteckningar'
        b2 = 'Skriv i journal'
        b3 = 'Hämta inlägg'
        # if sida == 1:
        #     b1 = 'Stäng anteckningar'
        # if sida == 2:
        #     b2 = 'Stäng journal'
        # if sida == 3:
        #     b3 = 'Stäng inlägg'
        button1 = ttk.Button(frame_left, text=b1, command=öppna_kladd)
        button1.pack(padx=20, pady=20, fill='x')
        button2 = ttk.Button(frame_left, text=b2, command=öppna_journal)
        button2.pack(padx=20, pady=20, fill='x')
        button3 = ttk.Button(frame_left, text=b3, command=hämta)
        button3.pack(padx=20, pady=20, fill='x')