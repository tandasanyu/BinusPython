def MenuCustom():
    print("Selamat Datang")
    print("Tentukan Pilihan : ")
    print("1. Kalkulator")
    pilihan = input("Masukan Pilihan Menu : ")
    pilihan = int(pilihan)

    if pilihan == 1 :
        usr = input("Masukan Username : ")
        usr_ = str(usr)
        pswd = input("Masukan Password : ")
        pswd_ = str(pswd)

        hasil = UsernamePswd(usr_,pswd_) # cara memanggil fungs dan menyimpan nilai fungsi di variabel
        # print(hasil)
        # di buat if untuk cek apakah variabel hasil nilainya true
            # panggil fungsi / blok matematik dasar
            fungsimatdas()
        #else : selesai program karena username psdw tidak cocok

    else :
        print("Pilihan yang anda masukan tidak valid") # program selesai




def UsernamePswd(user,pswd): # fungsi untuk Cek username password
    username = "Her"
    Pasword = "123"

    if username == user and pswd == Pasword :
        return True # kembalikan true jika username pswd sama
    else:
        return False # kembalikan false jika username pswd beda



#fungsi matdas
def fungsimatdas():
    print("1. Pertambahan")
    print("2. Pengurangan")
    PilihanFungsiMatdas = input("Masukan Pilihan Menu : ")
    PilihanFungsiMatdas = int(PilihanFungsiMatdas)

    if PilihanFungsiMatdas == 1:
        # masuk ke pertambahan
    elif PilihanFungsiMatdas == 2:
        #masuk ke pengurangan
    else:
        # jika kondisi tidak memenuhi
