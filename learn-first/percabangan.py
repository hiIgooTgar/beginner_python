nama = input("Masukkan nama anda : ")
umur = int(input("Masukan umur anda : "))

print("==== Percabangan | Python ====")
print("Nama anda adalah " + nama)    
if(umur <= 5):
    print("Masih balita")
elif(umur <= 10):
    print("Anda masih anak anak")
elif(umur <= 18):
    print("Anda masih remaja") 
else:
    print("Anda sudah dewasa")
