
# NAMA : JUHARI
# NIM : D0221322
# KELAS : E INFORMATIKA

# Memanggil semua class yang ada pada file Hitungluas
# Jadi yang dijalankan cuman file Main.py

from Hitungluas import *


# ---------------------------------------------------
def stopCode():
    stop = input("Do You Want To Continue?[Y/n] : ")
    if stop == "n":
        return True
    return False   


next = False
while (not next):
    print("=====================")
    print("======== MENU =======")
    print("=====================")
    print("== 1. Bangun Datar ==")
    print("== 2. Bangun Ruang ==")
    print("===  0. LogOut  ===")
    print("=====================")

    try:
        menu = int(input("Pilih : "))

        stop = False

        if menu == 1:
            while (not stop):
                print("MENGHITUNG LUAS BANGUN DATAR")
                print("1. Persegi")
                print("2. Lingkaran")
                print("3. Segitiga")

                pilih = int(input("Masukkan Pilihan Diatas! : "))
                if pilih == 1:
                    p = int(input("Masukkan panjang : "))
                    l = int(input("Masukkan lebar   : "))
                    persegi = Persegi(p, l)
                    persegi.Luas()
                
                elif pilih == 2:
                    a = int(input("Masukkan alas    : "))
                    t = int(input("Masukkan tinggi  : "))
                    lingkaran = Lingkaran(a, t)
                    lingkaran.Luas()

                elif pilih == 3:
                    phi = 3.14
                    j = int(input("Masukkan Jari-jari : "))
                    segitiga = Segitiga(phi, j)
                    segitiga.Luas()
                
                if stopCode() == True:
                    stop = True

        elif menu == 2:
            while (not stop):
                print("MENGHITUNG LUAS BANGUN RUANG")
                print("1. Kubus")
                print("2. Balok")
                print("3. Tabung")

                pilih = int(input("Masukkan Pilihan! : "))
                if pilih == 1:
                    r = 6
                    s = int(input("Masukkan sisi : "))
                    kubus = Kubus(r, s)
                    kubus.Luas()

                elif pilih == 2:
                    p = int(input("Masukkan panjang : "))
                    l = int(input("Masukkan lebar   : "))
                    t = int(input("Masukkan tinggi  : "))
                    balok = Balok(p, l)
                    balok.Luas(t)

                elif pilih == 3:
                    J = int(input("Masukkan jari    : "))
                    T = int(input("Masukkan tinggi  : "))
                    tabung = Tabung(J, T)
                    tabung.luas()
                
                if stopCode() == True:
                    stop = True
    
        elif menu == 0:
            print("=================")
            print("== Program Out ==")
            print("=================")
            break
        else:
            print("Pilihan Tidak Tersedia!")

    except:
        print("Silahkan masukkan angka")
