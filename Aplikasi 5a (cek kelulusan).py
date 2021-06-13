'''
program cek kelulusan 
created by Alief Hijrul Kirom (20083000038)
kelas 2B
'''
import os
clear = lambda : os.system('cls')
jwb = "y"
while jwb == "Y" or jwb == "y" :
    clear()
    print("PROGRAM CEK KELULUSAN")
    print("---------------------")
    print()
    a = input("Masukkan Nilai = ")
    n = int(a)
    if n < 0 or n > 100 :
        sts = "Inputan hanya boleh 0 sampai 100 saja"
    elif n > 60 :
        sts = "LULUS"
    else :
        sts = "TIDAK LULUS"
    print()
    print(sts)
    print()
    jwb = input("Cek lagi? (y/t) : ")
    if jwb == "t" or jwb == "T":
        break
