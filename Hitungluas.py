
class Bangundatar:
    def __init__(self, nilai1, nilai2):
        self.x = nilai1
        self.y = nilai2
    
class Persegi(Bangundatar):
    def Luas(self):
        print(f"Luas Persegi   = {float(self.x * self.y)}")

class Lingkaran(Bangundatar):
    def Luas(self):
        print(f"Luas Lingkaran = {float(0.5 * self.x * self.y)}")
    
class Segitiga(Bangundatar):
    def Luas(self):
        print(f"Luas Segitiga  = {float(self.x * self.y * self.y)}")

class Bangunruang(Bangundatar):
    pass

class Kubus(Bangunruang):
    def Luas(self):
        sisi = self.x * self.y**2
        print(f"Luas Kubus = {float(sisi)}")
    
class Balok(Bangunruang):
    def Luas(self, t):
        p = self.x
        l = self.y
        Luas = 2 * ((p * l) + (l * t) + (p * t))
        print(f"Luas Balok = {float(Luas)}")

class Tabung(Bangunruang):
    def luas(self):
        j = self.x
        t = self.y
        Luas = (2 * 22/7 * j * t) + (2 * 22/7 * j**2) 
        print(f"Luas Tabung = {float(round(Luas,2))}")    



