class Inlägg():
    def __init__(self, text):
        self.text = text

class Journal(Inlägg):
    def __init__(self, rubrik, text):
        super().__init__(text)
        self.rubrik = rubrik

    #def spara etc

class Kladd(Inlägg):
    def __init__(self, text):
        super().__init__(text)