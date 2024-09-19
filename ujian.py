harga_anak = 30000
harga_dewasa = 50000
harga_lansia = 35000

jumlah_pembeli = int(input("masukkan jumlah pembeli tiket: "))

total_harga = 0

for i in range(jumlah_pembeli): 
    print(f"\nPembeli {i+1}")
    
    usia = int(input("masukkan usia pembeli: "))
    jumlah_tiket = int(input("masukkan jumlah tiket yang ingin dibeli: "))

    if usia < 12: 
        harga_tiket = harga_anak
    elif 12<= usia <= 60: 
        harga_tiket = harga_dewasa
    else:
        harga_tiket = harga_lansia 

    total_per_pembeli = harga_tiket * jumlah_tiket 
print(f"harga untuk pembeli {1+i}: Rp {total_per_pembeli}")
print(f"\nTotal harga untuk semua tiket yang di beli : Rp {total_harga}")
