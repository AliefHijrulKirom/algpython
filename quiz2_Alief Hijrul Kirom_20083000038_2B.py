# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 13:12:37 2021

@author: Alief Hijrul Kirom (20083000038) kelas 2B
#algorithma
1. set variabel kode,merk oli, harga, total belanja,potongan, total harga, ppn
2. input pilihan barang, jumlah
3. jika a= Duration SW20 1L = @ Rp53.000
        b= Castrol Magnatec 1L = @ Rp50.000
        c= Federal Supreme XX 1L = @ Rp54.000
        d= Yamalube 1L = @ Rp45.000
   selain itu e= Shell 1L = @ Rp46.000
4.hitung biaya total awal 
5.setiap pembelian dikenakan pajak PPN 1%, jika pembelian 
  minimal Rp.200.000 maka mendapat potongan harga 5% 
6.tampilkan biaya akhir 
7.repeat
"""
jwb = "y"
while jwb=="y" or jwb=="Y":
    print("==============================")
    print(" daftar harga oli UD.Matahari ")
    print("==============================")
    print(" Kode : a= Duration sw20 ")
    print(" Kode : b= Castrol Magnetic ")
    print(" Kode : c= Federal Supreme ")
    print(" Kode : d= yamalub ")
    print(" Kode : e= Shell ")
    print("[Ukuran 1L]")
    print("================================")

    Kode = ('a', 'b', 'c', 'd', 'e')              
    Oli = ('Duration sw20', 'Castrol Magnetic', 'Federal Supreme', 'Yamalube', 'Shell')
    harga = [53000, 50000, 54000, 45000, 46000]
    
    pilihan = input(">> Masukkan Kode =  ")
    #
    if pilihan=="a" or "A":
        idx= 0
    elif pilihan=="b" or "B":
        idx= 1
    elif pilihan=="c" or "C":
        idx= 2
    elif pilihan=="d" or "D":
        idx= 3
    elif pilihan=="e" or "E":
        idx= 4
    else:
        idx= 0
     #
    print(">>> Merk Oli          = " + Oli[idx])   
    print(">>> harga             = Rp. " + str(harga[idx]))
    #
    n = input("Masukan jumlah Oli yang akan dibeli =  ")   
    x = int(n)
    TotalAwalA = x * int(harga[idx])
    
    TotalMinimalSebelumppn = 200000 
        
    if TotalAwalA < TotalMinimalSebelumppn : 
            TotalAwalB = TotalAwalA - TotalAwalA*5/100
    else:
            TotalAwalB = TotalAwalA
    
        #TotalBiaya Dengan PPN 1%
    TotalAkhir = TotalAwalB + TotalAwalB*1/100
    
        #tampilkan Total Biaya
    print(">>>> Total Akhir     = Rp. " + str(TotalAkhir))
    print(" ")
    print("==============================================")
    jwb = input(">> ingin melakukan transaksi lain ? y/t = ")
    if jwb=="t" or jwb=="T":
        break
     

