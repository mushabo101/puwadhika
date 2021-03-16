def urutkan(n): 
    genap = []
    ganjil = []
    for i in n:
        if i % 2 == 0:
            genap.append(i)
            genap.reverse()
        else:
            ganjil.append(i)
            ganjil.sort()
    return ganjil+genap

sort_odd_even =[1,3,2,2,1,5,1,24,12,124,12,21,32,15]
print(urutkan(sort_odd_even))