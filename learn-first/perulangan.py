sum = 1
for i in range(10):
    sum += 1
    print(sum, "Igo Tegar | Looping For")

while sum <= 5:
    print(sum, "Igo Tegar | Looping While")
    sum += 1

while True:
    angka = input("Masukkan angka (ketik 0 untuk keluar): ")
    
    if angka.isdigit():
        angka = int(angka)
        if angka == 0:
            print("Selesai")
            break
        else:
            print("Anda memasukkan angka:", angka)