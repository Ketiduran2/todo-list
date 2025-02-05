tugas =[]

def add():
    new_task = input("Tambahkan tugas anda: ")
    tugas.append(new_task)

def ls():
    if not tugas:
        print("tidak ada tugas!")
    else:
        for i,t in enumerate (tugas, 1):
            print(f"{i}. {t}")

def hapus():
    ls()
    hps = int(input("masukan id tugas yang ingin di hapus: ")) - 1
    if 0 <= hps < len(tugas):
        tugas.pop(hps)
        print("Tugas berhasil di hapus !! ")
    else:
        print("id tugas tidak valid!!")

while True:
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        add()
    elif pilihan == '2':
        ls()
    elif pilihan == '3':
        hapus()
    elif pilihan == '4':
        break
    else:
        print("Pilihan tidak valid!")
