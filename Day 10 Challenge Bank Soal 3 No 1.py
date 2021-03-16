a = input('Masukan Sebuah Kalimat : ')

if len(a) != 0 and len(a) < 200:
    print('*'+a.upper()+'*')
elif len(a) > 200:
    print('Batas Karakter Maksimal Hanya 200 ')
else :
    b = input('Masukkan Sebuah Inputan')
    