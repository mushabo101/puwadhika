def terpanjang(s):
    kata = s.split()
    kamus ={}
    for i in kata :
        kamus[i] = len(i)
    print ('Jumlah Karakter Terbanyak Adalah Sebesar', str(max(kamus.values())), 'Karakter')
    for i in kamus :
        if kamus[i] == max(kamus.values()) :
            print ('Karakter Yang Berjumlah', str(max(kamus.values())), 'Adalah', i)

kalimat = input('Masukkan Kalimat : ')
terpanjang(kalimat)