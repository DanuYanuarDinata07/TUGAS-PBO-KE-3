# luas dan volume kubus
def hitung_luas_kubus(rusuk):
    Luas = 6 * (rusuk * rusuk)
    return Luas

def hitung_volume_kubus(Rusuk):
    Volume =  (Rusuk * Rusuk * Rusuk)
    return Volume

# luas dan volume balok
def hitung_luas_balok(panjang, lebar, tinggi):
    Luas = ((2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi))
    return Luas

def hitung_volume_balok(Panjang, Lebar, Tinggi):
    Volume = (Panjang * Lebar * Tinggi)
    return Volume

# luas dan volume limas segiempat
def hitung_luas_limassegiempat(sisi, tinggiempat):
    Luas = (sisi*sisi)+(4*sisi*tinggiempat/2)
    return Luas

def hitung_volume_limassegiempat(sisi, tinggilimas):
    Volume = 1/3*(sisi*sisi)*tinggilimas
    return Volume

# luas dan volume prisma segitiga
def hitung_luasalas_prismasegitiga(sisi1, sisi2, sisi3, tinggiprisma):
    Luas = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma
    return Luas

def hitung_luassisi_prismasegitiga(sisi1, sisi2, sisi3, tinggiprisma, alas, tinggi):
    Luassisi = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma + alas * tinggi
    return Luassisi

def hitung_volume_prismasegitiga(alas, tinggi, tinggiprisma):
    Volume = ( alas * tinggi ) / 2 * tinggiprisma
    return Volume

# luas dan volume limas segitiga
def hitung_luaspermukaan_limassegitiga(alassegitiga, tinggisegitiga, tinggilimas):
    Luas = 4*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return Luas

def hitung_volume_limassegitiga(alassegitiga, tinggisegitiga, tinggilimas):
    Volume =  1/3*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return Volume

# luas dan volume tabung silinder
def hitung_luasselimut_tabung(jarijari, tinggi):
    Luasselimut = 2*3.14*jarijari*tinggi
    return Luasselimut

def hitung_luaspermukaan_tabung(jarijari, tinggi):
    Luaspermukaan = 2*3.14*jarijari*tinggi+2*3.14*jarijari**2
    return Luaspermukaan

def hitung_volume_tabung(jarijari, tinggi):
    Volume = 3.14*jarijari**2*tinggi
    return Volume

# luas dan volume kerucut
def hitung_luasselimut_kerucut(jarijari, sisi):
    luasselimut = 3.14*jarijari*sisi
    return luasselimut

def hitung_luaspermukaan_kerucut(jarijari, sisi):
    luaspermukaan = 3.14*jarijari*sisi
    return luaspermukaan

def hitung_luasvolume_kerucut(jarijari, tinggi):
    luasvolume = 1/3*3.14*jarijari**2*tinggi
    return luasvolume

# luas dan volume bola
def hitung_luas_bola(jarijari):
    luas = 4*3.14*jarijari**2
    return luas

def hitung_volume_bola(jarijari):
    Volume = 4/3*3.14*jarijari**3
    return Volume