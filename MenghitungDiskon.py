harga = float(input("masukan harga barang:"))
if harga >= 100000 :
    diskon = harga*0.10
    total_bayar = harga - diskon
    print ("anda mendapatkan diskon 10%")
    print ("jumlah diskon :", diskon)
else :
    total_bayar = harga
    print ("tidak mendapat diskon")
    print ("total yang harus dibayar:", total_bayar)