import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def init_data():
    global list_data
    list_data = []

def show_menu():
    clear_screen()
    print("=== APLIKASI KONTAK ===")
    print("[1] Lihat Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[0] Exit")
    print("-----------------------")
    menu = input("pilih menu> ")
    if menu == "1":
        menu1()
    elif menu == "2":
        menu2()
    elif menu == "3":
        menu3()
    elif menu == "4":
        menu4()
    elif menu == "0":
        print("Terimakasih Telah Berkunjung")
        exit()
    else:
        print("Menu yang anda masukkan tidak ada, masukkan pilihan yang tersedia...!!")
        kembali()

def menu1(): # Menampilkan data
    print("No || Nama || NIM")
    if len(list_data) <= 0:
        print("Data masih kosong")
    else:
        for index, data in enumerate(list_data):
            print(f"{index}. {data[0]} || {data[1]}")
    kembali()

def menu2(): # Menambah data
    nama = input("Masukkan nama mahasiswa : ")
    nim = input("Masukkan NIM mahasiswa : ")
    list_data.append((nama, nim))
    print("Data berhasil ditambahkan")
    kembali()

def menu3(): # Mengedit data
    index = int(input("Masukkan nomor index: "))
    if 0 <= index < len(list_data):
        nama_lama, nim_lama = list_data[index]
        nama_baru = input("Masukkan nama baru : ")
        nim_baru = input("Masukkan NIM baru : ")
        list_data[index] = (nama_baru, nim_baru)
        print("Data berhasil dirubah")
    else:
        print("Nomor index tidak valid")
    kembali()

def menu4(): # Menghapus data
    index = int(input("Masukkan nomor index: "))
    if 0 <= index < len(list_data):
        data = list_data.pop(index)
        print(f"Data {data[0]} dengan NIM {data[1]} berhasil dihapus")
    else:
        print("Nomor index tidak valid")
    kembali()

def kembali():
    print("\n")
    input("Tekan enter untuk kembali...")
    show_menu()


init_data()

while True:
    show_menu()