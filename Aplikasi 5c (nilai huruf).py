'''
program cek nilai huruf
    by Alief Hijrul Kirom (20083000038)
    kelas 2B
'''
import os
clear = lambda : os.system('cls')
jwb = "y"
while jwb == "Y" or jwb == "y" :
    clear()
    print("PROGRAM CEK NILAI HURUF")
    print("---------------------")
    print()
    a = input("Masukkan Nilai = ")
    n = int(a)
    if n < 0 or n > 100 :
        sts = "Inputan hanya boleh 0 sampai 100 saja"
    elif n > 80 :
        sts = "BAIK SEKALI"   
    elif n >= 65 :
        sts = "BAIK"   
    elif n >= 55 :
        sts = "CUKUP"   
    elif n >= 40 :
        sts = "KURANG"   
    else :
        sts = "KURANG SEKALI" 
    print()
    print(sts)
    print()
    jwb = input("Cek lagi? (y/t) : ")
    if jwb == "t" or jwb == "T":
        break