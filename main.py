import datetime
import os
import sys
import time
from pathlib import Path

from colorama import init, AnsiToWin32

init()  # init the colorama library
stream = AnsiToWin32(sys.stderr).stream  # for colorized text


class Item:
    """Item Class"""

    def __init__(self, provider, nomor_id, nama_item, masa_aktif, harga_jual, harga_beli, stok, stok_default,
                 waktu_penambahan):
        self.provider = provider
        self.nomor_id = nomor_id
        self.nama_item = nama_item
        self.masa_aktif = masa_aktif
        self.harga_jual = harga_jual
        self.harga_beli = harga_beli
        self.stok = stok
        self.waktu_penambahan = waktu_penambahan
        self.stok_default = stok_default


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def sleep(sec):
    time.sleep(sec)


def initiate_data(item_path, dir_path):
    if not os.path.exists(dir_path):
        os.makedirs("data/")
    file = open(item_path, "w")
    file.write("Inisiasi, 0, 0, 0, 0, 0, 0, 0, 0")
    file.close()


def backup_data(file_path):
    """"will backup  to prevent data lost and Return backup data Path"""
    file = open(file_path, "r").read()
    open(Path("data/old_item.txt"), "w").write(file)
    return Path("data/old_item.txt")


def load_data(file_path):
    """will return list of item classes"""
    file = open(file_path, "r").read()
    item_name = file.split("\n")
    item_list = [x.split(", ") for x in item_name]
    item_name = []
    item = []

    for i in range(len(item_list)):
        item_name.append("item_" + str(i + 1))
    for i in range(1, len(item_name)):
        #  For Checking missing data
        #print(item_list[i][0])
        #print(item_list[i][1])
        #print(item_list[i][2])
        #print(item_list[i][3])
        #print(item_list[i][4])
        #print(item_list[i][5])
        #print(item_list[i][6])
        #print(item_list[i][7])
        #print(item_list[i][8])
        item_name[i] = Item(provider=item_list[i][0], nomor_id=item_list[i][1], nama_item=item_list[i][2],
                            masa_aktif=item_list[i][3], harga_jual=item_list[i][4], harga_beli=item_list[i][5],
                            stok=item_list[i][6], stok_default=item_list[i][7], waktu_penambahan=item_list[i][8])
        item.append(item_name[i])
    return item


def save_data(item_list, path):
    """will save from list of item classes to item.txt"""
    file = open(path, "w")
    for i in range(len(item_list)):
        file.write(str(item_list[i].provider) + ", ")
        file.write(str(item_list[i].nomor_id) + ", ")
        file.write(str(item_list[i].nama_item) + ", ")
        file.write(str(item_list[i].masa_aktif) + ", ")
        file.write(str(item_list[i].harga_jual) + ", ")
        file.write(str(item_list[i].harga_beli) + ", ")
        file.write(str(item_list[i].stok) + ", ")
        file.write(str(item_list[i].stok_default) + ", ")
        file.write(str(item_list[i].waktu_penambahan))
        if not i == len(item_list) - 1:
            file.write("\n")

    file.close()


def search_item(keyword, item_list):
    """"Will Return list of searched item index"""
    item = []
    for i in range(len(item_list)):
        if keyword.upper() in str(item_list[i].nama_item).upper():
            item.append(i)
    return item


def money_format_print(money):
    """ Return correct format for money"""
    money = str(money)
    correct_format = ""
    count = 0
    for i in reversed(range(len(money))):
        correct_format += money[i]
        count += 1
        if count >= 3 and len(money[0:i]):
            correct_format += "."
            count = 0
    return correct_format[::-1]


def add_item(item_list):  # Need Improvement ####
    """"add Item classes Object to a target list"""
    provider_list = ["1. Telkomsel", "2. Smartfren", "3. XL", "4. Axis", "5. Indosat", "6. Three"]
    current_item = []

    while True:
        while True:
            print(provider_list)
            try:
                provider = int(input("Provider (1/2/3/4/5/6) : "))
                if 0 < provider <= len(provider_list):
                    provider = provider_list[int(provider) - 1][3:]
                    break
            except ValueError:
                print("Masukan Angka yang tersedia")
                sleep(1.2)

        nama_item = provider + " " + input("Nama Item (tanpa provider): ")
        current_item.append(nama_item)

        while True:
            try:
                masa_aktif = int(input("Masa aktif (Hari) : "))
                masa_aktif = str(masa_aktif) + " Hari"
                current_item.append(masa_aktif)
                break
            except ValueError:
                print("Masukan Angka")
                sleep(1.2)
                clear()
                print(current_item)
        while True:
            try:
                harga_jual = int(input("Harga Jual : "))
                current_item.append(harga_jual)
                break
            except ValueError:
                print("Masukan Angka")
                sleep(1.2)
                clear()
                print(current_item)
        while True:
            try:
                harga_beli = int(input("Harga Beli : "))
                current_item.append(harga_beli)
                break
            except ValueError:
                print("Masukan Angka")
                sleep(1.2)
                clear()
                print(current_item)
        while True:
            try:
                stok = int(input("Stok : "))
                current_item.append(stok)
                break
            except ValueError:
                print("Masukan Angka")
                sleep(1.2)
                clear()
                print(current_item)
        while True:
            try:
                default_stok = int(input("Default Stok : "))
                break
            except ValueError:
                print("Masukan Angka")
                sleep(1.2)
                clear()
                print(current_item)

        nomor_id = int(item_list[-1].nomor_id) + 1  # generated item_id will be last item in list +1

        temp_item = Item(str(provider), str(nomor_id), str(nama_item), str(masa_aktif), str(harga_jual),
                         str(harga_beli), str(stok), default_stok, datetime.datetime.now())

        item_list.append(temp_item)
        del temp_item
        print(f"{nama_item} {masa_aktif}, harga jual : {harga_jual}, stok : {stok}")
        user = input("Lanjutkan?(y/n)")
        if not user.upper() == "Y":
            break


def del_item(item_id, item_list):
    """"delete Item classes Object from a target list with item_id"""
    del_id = []
    for i in range(len(item_list)):
        if item_list[i].nomor_id == str(item_id):
            del_id.append(int(i))
            print(item_list[i].nama_item)
    if not del_id:
        print("Tidak Ada data ditemukan")
    else:
        user = input("Yakin untuk Menghapus ? (y/n)\n> ")
        if user.upper() == "Y":
            for i in del_id:
                del item_list[i]
                input("Barang Berhasil dihapus")
        input("Kembali")


def edit_item(item_list):  # Need Improvement
    def edit_provider(item_edit_list):
        provider_list = ["1. Telkomsel", "2. Smartfren", "3. XL", "4. Axis", "5. Indosat", "6. Three"]
        print(item_edit_list)
        for item in item_edit_list:
            clear()
            print_table(item_edit_list, [])
            print(provider_list)
            while True:
                try:
                    print(item.nama_item, item.masa_aktif)
                    provider = int(input("Provider (1/2/3/4/5/6) : "))
                    provider = provider_list[int(provider) - 1][3:]
                    item.provider = provider
                    break
                except ValueError:
                    print("Masukan nilai yang valid")

    def edit_nama(item_edit_list):
        for item in item_edit_list:
            clear()
            print(item.nama_item, item.masa_aktif)
            print(item.nama_item)
            nama_item = item.provider + " " + input("Nama Item (tanpa provider): ")
            item.nama_item = nama_item

    def edit_masa_aktif(item_edit_list):
        for item in item_edit_list:
            clear()
            print(item.nama_item, item.masa_aktif)
            print(item.nama_item)
            masa_aktif = input("Masa aktif (Hari) : ") + " Hari"
            item.masa_aktif = masa_aktif

    def edit_jual(item_edit_list):
        for item in item_edit_list:
            clear()
            print_table(item_edit_list, [])
            while True:
                try:
                    print(item.nama_item, item.masa_aktif)
                    harga_jual = int(input("Harga Jual : "))
                    item.harga_jual = str(harga_jual)
                    break
                except ValueError:
                    print("Masukan angka")

    def edit_beli(item_edit_list):
        for item in item_edit_list:
            clear()
            print_table(item_edit_list, [])
            while True:
                try:
                    print(item.nama_item, item.masa_aktif)
                    harga_beli = int(input("Harga Jual : "))
                    item.harga_beli = str(harga_beli)
                    break
                except ValueError:
                    print("Masukan angka")

    def edit_stok(item_edit_list):
        for item in item_edit_list:
            clear()
            print_table(item_edit_list, [])
            while True:
                try:
                    print(item.nama_item, item.masa_aktif)
                    stok = int(input("Masukan Stok Terkini : "))
                    item.stok = str(stok)
                    break
                except ValueError:
                    print("Masukan angka")

    def edit_default(item_edit_list):
        for item in item_edit_list:
            clear()
            print_table(item_edit_list, [])
            while True:
                try:
                    print(item.nama_item, item.masa_aktif)
                    stok_default = int(input("Stok Default : "))
                    item.stok_default = str(stok_default)
                    break
                except ValueError:
                    print("Masukan angka")

    item_edit = []
    menu = """
1. Provider
2. Nama Item
3. Masa Aktif
4. Harga Jual
5. Harga Beli
6. Stok
7. Stok Default
8. Semua
9. Exit
"""
    print_table(item_list, [])
    item_id = input("Masukan list id barang yang ingin diubah (dipisahkan spasi), Masukan 0 untuk merubah semuanya: ")
    item_id = item_id.split()

    if item_id == ["0"]:
        item_edit = item_list
    else:
        for x in item_list:
            for i in item_id:
                if str(x.nomor_id) == str(i):
                    item_edit.append(x)
                    break
        if not item_edit:
            print("Tidak Ada Barang ditemukan")
            return

    clear()
    print_table(item_edit, [])

    while True:
        print(menu)
        while True:
            try:
                choice = int(input("Apa yang anda ingin ubah? "))
                if 0 < choice <= 9:
                    break
                raise ValueError("Nilai tidak ada dalam daftar pilih")
            except ValueError:
                print("Masukan angka yang valid")

        if choice == 1:  # Provider
            edit_provider(item_edit)
        elif choice == 2:  # Nama Item
            edit_nama(item_edit)
        elif choice == 3:  # Masa Aktif
            edit_masa_aktif(item_edit)
        elif choice == 4:  # Jual
            edit_jual(item_edit)
        elif choice == 5:  # Beli
            edit_beli(item_edit)
        elif choice == 6:  # Stok
            edit_stok(item_edit)
        elif choice == 7:  # Stok Default
            edit_default(item_edit)
        elif choice == 8:  # Semua
            for i in item_edit:
                edit_provider([i])
                edit_nama([i])
                edit_masa_aktif([i])
                edit_jual([i])
                edit_beli([i])
                edit_stok([i])
                edit_default([i])
        elif choice == 9:  # Exit
            break


def generate_order(item_list):
    estimate_price = 0
    for i in item_list:
        order = 0
        if int(i.stok_default) - int(i.stok) > 0:
            order = int(i.stok_default) - int(i.stok)
            estimate_price += int(i.harga_beli) * (int(i.stok_default) - int(i.stok))
        print(i.nama_item, " = ", order)
    print("Estimasi Harga : ", money_format_print(estimate_price))


def renew_stock(item_list):
    """Will edit/update stok attributes of Item Classes list and return the old list"""
    save_data(item_list, "temp.txt")
    old_list = load_data("temp.txt")
    os.remove("temp.txt")

    print("Angka di Dalam Kurung Merupakan Jumlah Stok Lama, untuk menambah stok dari stok lama tambahkan + didepan "
          "angka ex:+3\n")
    for i in item_list:
        while True:
            try:
                user_input = input(i.nama_item + " " + i.masa_aktif + " (" + i.stok + ")" + " : ")
                if user_input[0] == "+":
                    i.stok = str(int(i.stok) + int(user_input[1:]))
                else:
                    i.stok = str(user_input)
                break
            except ValueError:
                print("Masukan Salah")
    return old_list


def profit(new_list, old_list):
    """Return int of profit"""
    profit_ = 0
    total = 0
    total_sell = 0
    if not old_list:
        for i in range(len(new_list)):
            total += int(int(new_list[i].harga_beli) * int(new_list[i].stok))
            print(new_list[i].nama_item, "(", new_list[i].stok, ")", " = ", "Rp ",
                  money_format_print(int(new_list[i].harga_beli) * int(new_list[i].stok)))
        print("Total Harga beli Keseluruhan Barang  : Rp ", money_format_print(total))
        print("Untuk Mengetahui Total Keuntungan dan total harga barang yang terjual harap lakukan update stok "
              "terlebih dahulu")
    else:
        for i in range(len(new_list)):
            try:
                total += int(int(new_list[i].harga_beli) * int(new_list[i].stok))
                x = (int(new_list[i].harga_jual) - int(new_list[i].harga_beli)) * \
                    (int(old_list[i].stok) - int(new_list[i].stok))
                y = int(new_list[i].harga_jual) * \
                    (int(old_list[i].stok) - int(new_list[i].stok))
                if x > 0:
                    profit_ += x
                    total_sell += y
            except IndexError or ZeroDivisionError:
                pass
        print("Total Harga beli Keseluruhan Barang  : Rp ", money_format_print(total))
        print("Total harga barang terjual : Rp ", money_format_print(total_sell))
    return profit_


def main_menu():
    """Return number of User Choice"""
    clear()
    menu = """Cek Stok Voucher
1. Lihat Data
2. Perbarui stock
3. Cari barang
4. Cek Keuntungan
5. Tambah Barang
6. Hapus Barang
7. Edit Barang
8. Buat Daftar Pesanan
9. Simpan Data
10. Exit"""
    while True:
        print(menu)
        choice = input("> ")
        try:
            if 1 <= int(choice) <= 10:
                return int(choice)
        except ValueError:
            print("Masukan Salah")


def print_table(item_list, index):  # It just works Lmao
    """Will Print a list of Item Object from list of index, input empty list to print all"""
    inden_no = 1
    inden_nama_barang, no_ = 12, " " * inden_no + "No" + " " * inden_no
    inden_id, barang_ = 1, " " * inden_nama_barang + "Nama Barang" + ' ' * inden_nama_barang
    inden_harga_jual, id_ = 4, " " * inden_id + "Id" + ' ' * inden_id
    inden_harga_beli, jual_ = 4, " " * inden_harga_jual + "Harga Jual" + ' ' * inden_harga_jual
    inden_stok, beli_ = 1, " " * inden_harga_beli + "Harga Beli" + ' ' * inden_harga_beli
    inden_hari, stok_ = 4, " " * inden_stok + "Stok" + ' ' * inden_stok
    inden_stok_default, hari_ = 1, " " * inden_hari + "Masa Aktif" + ' ' * inden_hari
    stok_default_ = " " * inden_stok_default + "Stok Default" + ' ' * inden_stok_default
    time_now = open("data/time.txt", "r")
    print("Data Terupdate tanggal : ", time_now.read())
    print(
        "|" + no_ + "|" + barang_ + "|" + hari_ + "|" + id_ + "|" + jual_ + "|" + beli_ + "|" + stok_ + "|" + stok_default_ + "|")
    print(
        "-" * len(
            "|" + no_ + "|" + barang_ + "|" + hari_ + "|" + id_ + "|" + jual_ + "|" + beli_ + "|" + stok_ + "|" + stok_default_ + "|"))

    def set_inden(text_len, row_len):
        """"Return int of a correct indent to print"""
        x = (row_len - text_len) // 2
        y = 0
        while (x * 2) + text_len < row_len:
            x += 1
        if (x * 2) + text_len < row_len:
            y -= 1
        if (x * 2) + text_len > row_len:
            y += 1
        return [x, y]

    if not index:
        for i in range(len(item_list)):
            index.append(i)

    for i in index:
        nama_barang = item_list[i].nama_item
        id_barang = item_list[i].nomor_id
        harga_jual = item_list[i].harga_jual
        harga_beli = item_list[i].harga_beli
        stok = item_list[i].stok
        stok_default = item_list[i].stok_default
        hari = item_list[i].masa_aktif

        no_inden = set_inden(len(str(i)), len(no_))
        nama_inden = set_inden(len(nama_barang), len(barang_))
        id_inden = set_inden(len(id_barang), len(id_))
        jual_inden = set_inden(len(harga_jual), len(jual_))
        beli_inden = set_inden(len(harga_beli), len(beli_))
        stok_inden = set_inden(len(stok), len(stok_))
        stok_default_inden = set_inden(len(stok_default), len(stok_default_))
        hari_inden = set_inden(len(hari), len(hari_))
        print("|" +
              " " * (no_inden[0] - no_inden[1]) +
              str(i) +
              " " * no_inden[0] +
              "|" +
              " " * (nama_inden[0] - nama_inden[1]) +
              str(nama_barang) +
              " " * nama_inden[0] +
              "|" +
              " " * (hari_inden[0] - hari_inden[1]) +
              str(hari) +
              " " * hari_inden[0] +
              "|" +
              " " * (id_inden[0] - id_inden[1]) +
              str(id_barang) +
              " " * id_inden[0] +
              "|" +
              " " * (jual_inden[0] - jual_inden[1]) +
              str(harga_jual) +
              " " * jual_inden[0] +
              "|" +
              " " * (beli_inden[0] - beli_inden[1]) +
              str(harga_beli) +
              " " * beli_inden[0] +
              "|" +
              " " * (stok_inden[0] - stok_inden[1]) +
              str(stok) +
              " " * stok_inden[0] +
              "|" +
              " " * (stok_default_inden[0] - stok_default_inden[1]) +
              str(stok_default) +
              " " * stok_default_inden[0] +
              "|"
              )

    print(
        "-" * len(
            "|" + no_ + "|" + barang_ + "|" + hari_ + "|" + id_ + "|" + jual_ + "|" + beli_ + "|" + stok_ + "|" + stok_default_ + "|"))


def main():
    item_path = Path("data/item.txt")
    dir_path = Path("data")
    if not item_path.is_file():
        initiate_data(item_path, dir_path)
    backup_path = backup_data(item_path)  # doing backup data first
    item_list = load_data(item_path)
    backup_list = load_data(backup_path)
    old_list = None
    while True:  # Main Loop
        clear()
        choice = main_menu()
        if choice == 1:  # Lihat Data
            clear()
            print_table(item_list, [])
            input("")

        elif choice == 2:  # Perbarui Stok
            clear()
            old_list = renew_stock(item_list)
            input("Stok Berhasil Diperbaharui")

        elif choice == 3:  # Cari Barang
            clear()
            keyword = input("Masukan Kata kunci : ")
            searched_list = search_item(keyword, item_list)
            if searched_list:
                print_table(item_list, searched_list)
            else:
                print("Tidak Ada Data Yang Ditemukan")
            input("")

        elif choice == 4:  # Keuntungan
            clear()
            if old_list:
                print("Keuntungan Anda : Rp ", profit(item_list, old_list))
                input()
            else:
                profit(item_list, None)
                input()

        elif choice == 5:  # Tambah Barang
            clear()
            add_item(item_list)

        elif choice == 6:  # Hapus Barang
            clear()
            item_id = input("Masukan Id Barang : ")
            del_item(item_id, item_list)

        elif choice == 7:  # Edit Barang
            clear()
            edit_item(item_list)
            input()

        elif choice == 8:  # Buat Pesanan
            clear()
            generate_order(item_list)
            input()

        elif choice == 9:  # Save data
            clear()
            save_data(item_list, item_path)
            input("Data Berhasi Disimpan")

        elif choice == 10:  # Exit
            clear()
            choice = input("Simpan Perubahan data?(y/n)").upper()
            if choice == "Y":
                save_data(item_list, item_path)
                if old_list:
                    file = open("data/time.txt", "w")
                    time_now = datetime.datetime.now()
                    file.write(str(time_now))
                sys.exit()
            save_data(backup_list, backup_path)
            sys.exit()


if __name__ == "__main__":
    main()
