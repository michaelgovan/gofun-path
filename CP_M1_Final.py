daftarbuku = [
    {
        'ID Buku':'101',
        'Nama Buku':'The Snowball \t',
        'Penulis':'Alice Schroeder',
        'Genre':'Biografi',
        'Tahun Terbit':2008,
        'Jumlah Halaman':976,
        'Ketersediaan':'Tersedia',
    },
    {   'ID Buku':'102',
        'Nama Buku':'Things Slowing Down',
        'Penulis':'Haemin Sunim \t',
        'Genre':'Self Help',
        'Tahun Terbit':2012,
        'Jumlah Halaman':201,
        'Ketersediaan':'Tersedia'
    },
    {   'ID Buku':'103',
        'Nama Buku':'Norwegian Wood',
        'Penulis':'Haruki Murakami',
        'Genre':'Novel\t',
        'Tahun Terbit':1987,
        'Jumlah Halaman':296,
        'Ketersediaan':'Tersedia'
    },
    {   'ID Buku':'104',
        'Nama Buku':'Rich Dad Poor Dad',
        'Penulis':'Robert Kiyosaki',
        'Genre':'Prsnl Finnce',
        'Tahun Terbit':1997,
        'Jumlah Halaman':207,
        'Ketersediaan':'Tersedia'
    },
    {   'ID Buku':'105',
        'Nama Buku':'The Principles',
        'Penulis':'Ray Dalio \t',
        'Genre':'Biografi',
        'Tahun Terbit':2017,
        'Jumlah Halaman':592,
        'Ketersediaan':'Tersedia'
    },
    {   'ID Buku':'106',
        'Nama Buku':'Bumi Manusia \t',
        'Penulis':'Pramoedya Ananta T',
        'Genre':'Novel\t',
        'Tahun Terbit':1980,
        'Jumlah Halaman':287,
        'Ketersediaan':'Tersedia'
    },
    {   'ID Buku':'107',
        'Nama Buku':'Strytllng With Data',
        'Penulis':'Cole Nussbaumer K',
        'Genre':'Non Fiksi',
        'Tahun Terbit':2015,
        'Jumlah Halaman':292,
        'Ketersediaan':'Tersedia'
    },


]


def menuawal():
    while True:
        menuutama=input('''
        ================================
        SELAMAT DATANG DI GO FUN LIBRARY
        ================================

        List Menu:
        1. Menampilkan Koleksi Buku
        2. Menambah Koleksi Buku
        3. Memperbaharui Koleksi Buku
        4. Menghapus Koleksi Buku
        5. Keluar
        
        Masukan menu yang ingin dijalankan:''')
    
        if (menuutama=='1'):
            menu10()
            break
        elif (menuutama=='2'):
            menu20()
            break
        elif (menuutama=='3'):
            menu30()
            break
        elif (menuutama=='4'):
            menu40()
            break
        elif (menuutama=='5'):
            menu50()
            break
        else:
            print(''' 
            \t    ============   Maaf menu yang anda pilih tidak ada   ============
            ''')


def menu10():
    while True:
        inputmenu10=input('''
        ========================
        MENU PENCARIAN DATA BUKU
        ========================
        
        List Menu:
        1. Menampilkan Daftar Buku
        2. Menampilkan Data Buku Tertentu
        3. Kembali ke Menu Utama

        Masukkan menu yang anda inginkan: 
        ''')
        if (inputmenu10=='1'):
            menu11()
            break
        elif (inputmenu10=='2'):
            menu12()
            break
        elif (inputmenu10=='3'):
            menuawal()
            break
        else:
            print('''
            ===================================
            Maaf menu yang anda pilih tidak ada
            ===================================
            ''')

            



def menu11():
    print('ID Buku\t| Nama Buku\t\t| Penulis\t\t| Genre\t\t| Tahun Terbit\t\t| Jumlah Halaman| Ketersediaan')
    for i in range(len(daftarbuku)):
        print(f"{daftarbuku[i]['ID Buku']} \t| {daftarbuku[i]['Nama Buku']} \t| {daftarbuku[i]['Penulis']} \t| {daftarbuku[i]['Genre']} \t| {daftarbuku[i]['Tahun Terbit']} \t\t\t| {daftarbuku[i]['Jumlah Halaman']} \t\t| {daftarbuku[i]['Ketersediaan']}\t")
    menu10()
            

def menu12():
    inputmenu12=input('Masukan ID Buku: ')
    hasil=[]
    for i in range(len(daftarbuku)):
        hasil.append(daftarbuku[i]['ID Buku'])
        if inputmenu12 in daftarbuku[i]['ID Buku']:
            cari=i
    if inputmenu12 in hasil:
        print('ID Buku\t| Nama Buku\t\t| Penulis\t\t| Genre\t\t| Tahun Terbit\t\t| Jumlah Halaman| Ketersediaan')
        print(f"{daftarbuku[cari]['ID Buku']} \t| {daftarbuku[cari]['Nama Buku']} \t| {daftarbuku[cari]['Penulis']} \t| {daftarbuku[cari]['Genre']} \t| {daftarbuku[cari]['Tahun Terbit']} \t\t\t| {daftarbuku[cari]['Jumlah Halaman']} \t\t| {daftarbuku[cari]['Ketersediaan']}\t")
        menu10()
    else:
        print('\n \t ================ Maaf, Buku yang anda masukkan tidak tersedia =================')
        menu10()

def menu211():
    while True:
        inputmenu211=input('Apakah Anda Yakin Ingin Menyimpan Data Buku Ini (Y/N)? ')
        if (inputmenu211=='Y'):
            print('\n ========= Terimakasih, Data Yang Anda Masukkan Telah Tersimpan =========')
            menu20()
            break
        else:
            menu20()
            break


def menu21(): 
    addIDBuku=input('Masukan1 ID Buku tambahan :')
    addNamaBuku=input('Masukan Nama  Buku: ')
    addPenulis=input('Masukan Penulis Buku: ')
    addGenre=input('Masukan Genre Buku: ')
    addTahunTerbit=input('Tahun Terbit: ')
    addjmlhhalaman=input('Jumlah Halaman: ')
    addketersediaan='Tersedia'

    hasil_i=[]
    for ii in range(len(daftarbuku)):
        hasil_i.append(daftarbuku[ii]['ID Buku'])
    if addIDBuku in hasil_i:
        print('''
            ==================================================================================================
            Maaf, ID Buku Yang Anda Masukan Sudah Ada, Mohon Masukan Kembali Dengan Input ID Buku Yang berbeda
            ==================================================================================================
            ''')
        menu20()
    else:
        inputmenu211=input('Apakah Anda Yakin Ingin Menyimpan Data Buku Ini (Y/N)? ')
        if inputmenu211.lower()=='y':
            daftarbuku.append({
                'ID Buku': addIDBuku,
                'Nama Buku': addNamaBuku,
                'Penulis': addPenulis,
                'Genre': addGenre,
                'Tahun Terbit' : addTahunTerbit,
                'Jumlah Halaman' : addjmlhhalaman,
                'Ketersediaan':addketersediaan
                })
            print('\n ========= Terimakasih, Data Yang Anda Masukkan Telah Tersimpan =========')
            menu20()
        elif inputmenu211.lower()=='n':
            menu20()




def menu20():
    while True:
        inputmenu21=input('''
        ==========================
        MENU MENAMBAH KOLEKSI BUKU
        ==========================
        
        List Menu:
        1. Menambah Daftar Buku
        2. Kembali Ke Menu Utama
        
        Masukkan Menu Yang Anda Inginkan:
        ''')
        if (inputmenu21=='1'):
            menu21()
            break
        elif (inputmenu21=='2'):
            menuawal()
            break
        else:
            print('''
            ===================================
            Maaf menu yang anda pilih tidak ada
            ===================================
            ''')
        

def menu40() :
    while True:
        inputmenu40=input('''
        ===========================
        MENU MENGHAPUS KOLEKSI BUKU
        ===========================
        
        List Menu:
        1. Hapus Data Berdasarkan ID
        2. Kembali Ke Menu Utama
        
        Masukkan Menu Yang Anda Inginkan:
        ''')
        if (inputmenu40=='1'):
            listkosong=[]
            for i in range(len(daftarbuku)):
                listkosong.append(daftarbuku[i]['ID Buku'])
            inputmenu41=input('Silakan Masukan ID Buku Yang Ingin Anda Hapus: ')
            if inputmenu41 in listkosong:
                idhps=listkosong.index(inputmenu41) 
                checkkeluar=input(f'Apakah Anda Yakin Akan Menghapus ID tersebut? (Y/N): ')
                if checkkeluar.lower()=='y':
                    del daftarbuku[idhps]
                    print('\n ========= Terimakasih, ID Buku Yang Anda Pilih Telah Terhapus =========')
                    menu40()
                    break
                elif checkkeluar.lower()=='n':
                    print('selesai')
            else:
                print(('''
                ===================================
                Maaf buku yang anda pilih tidak ada
                ===================================
                '''))
        elif (inputmenu40=='2'):
            menuawal()
            break
        else:
            print('''
            ===================================
            Maaf menu yang anda pilih tidak ada
            ===================================
            ''')
            menu40()
            break



def menu30() :
    while True:
        inputmenu30=input('''
        ==========================
        MENU MENGUBAH KOLEKSI BUKU
        ==========================
        
        List Menu:
        1. Ubah Data Berdasarkan ID
        2. Kembali Ke Menu Utama
        
        Masukkan Menu Yang Anda Inginkan:
        ''')
        if (inputmenu30=='1'):
            menu31()
            break
        elif (inputmenu30=='2'):
            menuawal()
            break


def menu31():
    inputmenu311=str(input('Masukan ID Buku Yang Mau Diupdate: '))
    hasil31=[]
    for i31 in range(len(daftarbuku)):
        hasil31.append(daftarbuku[i31]['ID Buku']) 
    if inputmenu311 in hasil31:
        indexupdate=hasil31.index(inputmenu311)
        print('ID Buku\t| Nama Buku\t\t| Penulis\t\t| Genre\t\t| Tahun Terbit\t\t| Jumlah Halaman| Ketersediaan')
        print(f"{daftarbuku[indexupdate]['ID Buku']} \t| {daftarbuku[indexupdate]['Nama Buku']} \t| {daftarbuku[indexupdate]['Penulis']} \t| {daftarbuku[indexupdate]['Genre']} \t| {daftarbuku[indexupdate]['Tahun Terbit']} \t\t\t| {daftarbuku[indexupdate]['Jumlah Halaman']} \t\t| {daftarbuku[indexupdate]['Ketersediaan']}\t")
        hasil31=[]
        inputmenu312=input('Apakan Anda Ingin Mengubah Data Buku Tersebut? (Y/N)')
        if inputmenu312.lower()=='y':
            while True:
                kolom=input('Kolom Apakah Yang Ingin Anda Rubah?  ')
                if kolom.lower()=='nama buku':
                    namabaru=input('Masukan Nama Baru: ')
                    daftarbuku[indexupdate]['Nama Buku']=namabaru
                    print('''
                    ========== Data Sudah Diperbaharui ==========
                    ''')
                    menu30()
                    break
                elif kolom.lower()=='penulis':
                    namabaru=input('Masukan Penulis Baru: ')
                    daftarbuku[indexupdate]['Penulis']=namabaru
                    print('''
                    ========== Data Sudah Diperbaharui ==========
                    ''')
                    menu30()
                    break
                elif kolom.lower()=='genre':
                    namabaru=input('Masukan Genre Baru: ')
                    daftarbuku[indexupdate]['Genre']=namabaru
                    print('''
                    ========== Data Sudah Diperbaharui ==========
                    ''')
                    menu30()
                    break
                elif kolom.lower()=='tahun':
                    namabaru=input('Masukan Tahun Terbit Baru: ')
                    daftarbuku[indexupdate]['Tahun Terbit']=namabaru
                    print('''
                    ========== Data Sudah Diperbaharui ==========
                    ''')
                    menu30()
                    break
                elif kolom.lower()=='jumlah halaman':
                    namabaru=input('Masukan Jumlah Halaman Baru: ')
                    daftarbuku[indexupdate]['Jumlah Halaman']=namabaru
                    print('''
                    ========== Data Sudah Diperbaharui ==========
                    ''')
                    menu30()
                    break
        
        elif inputmenu312.lower()=='n':
            menu30() 
        else:
            print('''
            ======== Maaf, Pilihan Yang Anda Masukan Tidak Ada =======
            ''')
            menu30()

    else:
        print('''
        ======== Maaf, Buku Yang Anda Maksud Tidak Ada =======
        ''')
        menu30()



def menu41():
    menu11()
    listkosong=[]
    for i in range(len(daftarbuku)):
        listkosong.append(daftarbuku[i]['ID Buku'])
    inputmenu41=input('Silakan Masukan ID Buku Yang Ingin Anda Hapus: ')
    if inputmenu41 in listkosong:
        idhps=listkosong.index(inputmenu41) 
        checkkeluar=input(f'Apakah Anda Yakin Akan Menghapus ID tersebut? (Y/N): ')
        if checkkeluar.lower()=='y':
            del daftarbuku[idhps]
            print('\n ========= Terimakasih, ID Buku Yang Anda Pilih Telah Terhapus =========')
            menu40()
        elif checkkeluar.lower()=='n':
            print('selesai')
    else:
        print(('''
        ===================================
        Maaf buku yang anda pilih tidak ada
        ===================================
        '''))
        listkosong=[]
 


def menu50():
    while True:
        inputmenu22=input('''
        Apakah Anda Yakin Ingin Keluar (Y/N)?
        ''')
        if (inputmenu22.lower()=='y'):
            break
        elif (inputmenu22.lower()=='n'):
            menuawal()
            break


menuawal()