import sys
from prettytable import PrettyTable
from db_manager import Session, init_db, seed_data, word_to_numeric, get_sorted_numbers, delete_by_parity, Number
from shapes import Square, Rectangle, Circle, display_shape_info

def print_menu():
    print("\n" + "="*30)
    print(" APLIKASI SERTIFIKASI PYTHON ")
    print("="*30)
    print("1. Bagian 1: Operasi Database")
    print("2. Bagian 2: Bangun Datar (OOP)")
    print("0. Keluar")
    print("="*30)

def db_menu(session):
    while True:
        print("\n--- OPERASI DATABASE ---")
        print("1. Inisialisasi & Isi Data (Reset)")
        print("2. Ubah Kata ke Simbol Angka (misal: 'satu' -> 1)")
        print("3. Tampilkan Tabel Terurut")
        print("4. Hapus Angka Berdasarkan Ganjil/Genap")
        print("5. Kembali ke Menu Utama")
        choice = input("Pilih menu: ")

        if choice == '1':
            init_db()
            seed_data(session)
        elif choice == '2':
            word_to_numeric(session)
        elif choice == '3':
            sorted_nums = get_sorted_numbers(session)
            table = PrettyTable()
            table.field_names = ["ID", "Angka"]
            for num in sorted_nums:
                table.add_row([num.id, num.angka])
            print(table)
        elif choice == '4':
            p_type = input("Pilih pola penghapusan ('genap' atau 'ganjil'): ").lower()
            if p_type in ['genap', 'ganjil']:
                mapping = {'genap': 'even', 'ganjil': 'odd'}
                delete_by_parity(session, mapping[p_type])
            else:
                print("Tipe tidak valid.")
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid.")

def shapes_menu():
    while True:
        print("\n--- BANGUN DATAR (OOP) ---")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Lingkaran")
        print("4. Kembali ke Menu Utama")
        choice = input("Pilih bentuk: ")

        try:
            if choice == '1':
                side = float(input("Masukkan panjang sisi: "))
                sq = Square(side)
                display_shape_info(sq)
            elif choice == '2':
                w = float(input("Masukkan lebar: "))
                h = float(input("Masukkan tinggi: "))
                rect = Rectangle(w, h)
                display_shape_info(rect)
                print(f"DEBUG: Lebar saat ini adalah {rect.width}")
            elif choice == '3':
                r = float(input("Masukkan jari-jari: "))
                circ = Circle(r)
                display_shape_info(circ)
            elif choice == '4':
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError as e:
            print(f"Kesalahan: {e}")

def main():
    init_db()
    session = Session()

    try:
        while True:
            print_menu()
            choice = input("Pilih menu: ")
            
            if choice == '1':
                db_menu(session)
            elif choice == '2':
                shapes_menu()
            elif choice == '0':
                print("Keluar dari aplikasi. Sampai jumpa!")
                break
            else:
                print("Opsi tidak valid.")
    finally:
        session.close()

if __name__ == "__main__":
    main()
