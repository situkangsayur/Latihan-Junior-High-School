#ruangbangunkubus
def hitung_kubus():
    print('Ruang bangun kubus:')
    s : int =12
    Luas = s * s
    Keliling = 12 * s
    Volume = s * s * s
    print('Luas:')
    print(Luas)
    print('Keliling:')
    print(Keliling)
    print('Volume:')
    print(Volume)
    
def hitung_balok():
# Ruang bangun balok
    print('Ruang bangun balok:')
    p = 15
    l = 10
    t = 20
    Luas = 2 * ((p * l) + (p * t) + (l * t))
    Keliling = 4 * (p + l + t)
    Volume = p * l * t
    print('Luas:')
    print(Luas)    
    print('Keliling:')
    print(Keliling)
    print('Volume  :   ')
    print(Volume)

# hitung luas segitiga
def hitung_segitiga():
    print("hitung luas segitiga ----------------------------")
    l = 10
    t = 15
    luas = 0.5 * l * t
    print('hasilnya adalah : ')
    print(luas)





if __name__ == '__main__' :

    hitung_balok()
    hitung_kubus()
    hitung_segitiga()

