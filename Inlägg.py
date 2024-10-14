from datetime import datetime

#Superklass
class Inlägg():
    def __init__(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

#Klass för journalinlägg som sparas/hämtas
class Journal(Inlägg):
    def __init__(self, rubrik, text, time=datetime.now()):
        super().__init__(text)
        self.__rubrik = rubrik
        self.__time = time

    def get_rubrik(self):
        return self.__rubrik

    def get_time(self):
        return self.__time

    def spara_till_fil(self):
        try:
            with open('Journal.txt', 'a', encoding='utf-8') as fil:
                fil.write(str(datetime.now())[:19]) #Kapar bort ms från datetime
                fil.write(f'\n{self.__rubrik}\n')
                fil.write(f'{self.get_text()}\n')
        except FileNotFoundError as e:
            print('Fel:', e)

#Hämtar inlägg, delar upp dem från fil
    def hämta():
        try:
            with open('Journal.txt', 'r', encoding='utf-8') as fil:
                alla = []
                for inlägg in fil.read().strip().split('\n\n'):
                    i = inlägg.split('\n')
                    alla.append(Journal(i[1], i[2], i[0]))
                return alla
        except FileNotFoundError as e:
            print('Fel:', e) 

#Klass för kladdblocket
class Kladd(Inlägg):
    def __init__(self, text):
        super().__init__(text)

    def spara(self):
        try:
            with open('Kladd.txt', 'w', encoding='utf-8') as fil:
                fil.write(self.get_text())
        except FileNotFoundError as e:
            print('Fel:', e)

    def hämta():
        try:
            with open('Kladd.txt', 'r', encoding='utf-8') as fil:
                return fil.read().strip()
        except FileNotFoundError as e:
            print('Fel:', e)
            return ''