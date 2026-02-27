angka1 = float(input("masukan angka pertama :"))
angka2 = float(input("masukan angka kedua :"))

if angka1 > angka2 :
    terbesar = angka1
elif angka2 > angka1 :
    terbesar = angka2
else :
    terbesar = angka1
    print ("kedua angka sama")
    print ("angka terbesar", terbesar)