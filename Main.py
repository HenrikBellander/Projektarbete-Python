import tkinter as tk
from tkinter import ttk
import Inlägg as i

#Ska tas bort
def test():
    print('Hello World!')

#Öppna och stäng anteckningar
def stäng():
    root.geometry('400x600')
    button1['text'] = 'Öppna anteckningar'
    button1['command'] = öppna

def öppna():
    root.geometry('800x600')
    button1['text'] = 'Stäng anteckningar'
    button1['command'] = stäng

def spara():
    inlägg = i.Journal('Rubrik', entry.get('1.0', 'end'))
    print(inlägg.rubrik)


#Skapa UI
root = tk.Tk()
root.title('Henkes Journalprojekt')
root.geometry('400x600')
root.resizable(False, False)
root['bg'] = 'blue'
root['padx'] = 20
root['pady'] = 20

#frame_right = tk.Frame(root, background='yellow', width=360, height=560)
#entry = tk.Text(frame_right, height=20)

s = ttk.Style()
s.configure('TFrame', background='green')

frame_left = ttk.Frame(root, style = 'TFrame')
frame_left['relief'] = 'ridge'
frame_left.place(x=0, y=0, width=360, height=560)

frame_right = ttk.Frame(root, style = 'TFrame')
frame_right['relief'] = 'ridge'
frame_right.place(x=400, y=0, width=360, height=560)

entry = tk.Text(frame_right, height=20)
entry.pack(padx=20, pady=20)

save = ttk.Button(frame_right, text='Spara', command=spara)
save.pack()

button1 = ttk.Button(frame_left, text='Öppna anteckningar', command=öppna)
button1.pack(expand=True)
button2 = ttk.Button(frame_left, text='Skriv inlägg', command=test)
button2.pack(expand=True)

#Kör UI/program
root.mainloop()