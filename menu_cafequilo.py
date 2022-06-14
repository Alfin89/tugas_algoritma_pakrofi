def infinite():
    while True:
        yield None

class menuMinuman:
    def ConnuClassic():
        bayar = int(input("Bayar     : "))
        print("Kembalian :",bayar-24000)
        print('Harga     :',24000)
        print('Minuman   : CONNU CLASSIC ')
        print("")

    def RedVelvet():
        bayar = int(input("Bayar     : "))
        print("Kembalian :",bayar-25000)
        print('Harga     :',25000)
        print('Minuman   : RED VELVET')
        print("")
        
    def LemonTea():
        bayar = int(input("Bayar     : "))
        print("Kembalian :",bayar-23000)
        print('Harga     :',23000)
        print('Minuman   : LEMOT TEA  ')
        print("")
        
    def GreenTea():
        bayar = int(input("Bayar     : "))
        print("Kembalian :",bayar-21000)
        print('Harga     :',21000)
        print('Minuman   : GREEN TEA ')
        print("")

    def MiloGreentea():
        bayar = int(input("Bayar     : "))
        print("Kembalian :",bayar-25000)
        print('Harga     :',25000)
        print('Minuman   : MILO GREENTEA  ')
        print("")

    def ChocoMild():
        bayar = int(input("Bayar     : "))
        print("Kembalian :",bayar-20000)
        print('Harga     :',20000)
        print('Minuman   : CHOCO MILD ')
        print("")

i = 0
for j in infinite():
    print('•••••♦•••••••••••••••••••••••••••••••••••••••••••••♦•••••')
    print('\t\tMENU MINUMAN QUILO CAFFE ')
    print("\nPilih kategori Minuman yang akan di beli")
    print("============================================================")
    print("1. CONNU CLASSIC : Rp.24000")
    print("2. RED VELVET    : Rp.25000")
    print("3. LEMOT TEA     : Rp.23000")
    print("4. GREEN TEA     : Rp.21000")
    print("5. MILO GREENTEA : Rp.25000")
    print("6. CHOCO MILD    : Rp.20000")
    print("============================================================\n")
    pilih = int(input("Masukkan Pilihan : "))
    if pilih == 1:
        menuMinuman.ConnuClassic()
    elif pilih == 2:
        menuMinuman.RedVelvet()
    elif pilih == 3:
        menuMinuman.LemonTea()
    elif pilih == 4:
        menuMinuman.GreenTea()
    elif pilih == 5:
        menuMinuman.MiloGreentea()
    elif pilih == 6:
        menuMinuman.ChocoMild()
    else:
        print("Pilihan Tidak Ada")
    lanjut = input("\nLanjutkan (Y/T) : ")
    if lanjut == "T" or lanjut == "t":
        break
    else:
        i = 0
