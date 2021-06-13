'''
cek total harga printer
created by Alief hijrul Kirom (20083000038)
    kelas 2B
'''
import os
clear = lambda : os.system('cls')

jwb = "y"
while jwb == "y" or jwb == "Y" :
    clear()
    print("PROGRAM HITUNG TOTAL HARGA PRINTER EPSON T20")
    print("--------------------------------------------")   
    hrgPrinter = 660000
    diskon = 0.15   
    a = input("Masukkan Jumlah Printer = ")
    jmlhPrt = int(a)
    totHrg = jmlhPrt * hrgPrinter

    if totHrg > 1500000 :
        totDiskon = diskon * totHrg
        totBy = totHrg - totDiskon
        print()
        print("Diskon 15%")
        print("Total Harga  = ",format(totHrg,',.2f'))
        print("Total Diskon = ",format(totDiskon,',.2f'))
        print("Total Biaya  = ",format(totBy,',.2f')) 
    else :
        totBy = totHrg
        print()
        print("Total Biaya = ",format(totBy,',.2f'))  
    print() 
    jwb = input("Cek Lagi? (y/t) = ")
    if jwb == "t" or jwb == "T" :
        break




    