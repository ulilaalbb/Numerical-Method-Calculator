m0 = 'MENU UTAMA'

mmenus = ['1. Metode Gauss ', '2. Metode Trapeziodal', '3. Metoda Regresi Kuadrat Terkecil',
          '4. Metoda Interpolasi', '5. Tentang Program', '0. Keluar']

menu_gauss = ['1. Sistem Persamaan Linier (SPL) 3 Variabel', '2. Sistem Persamaan Linier (SPL) 4 Variabel',
              '3. Sistem Persamaan Linier (SPL) 5 Variabel', '4. Kembali ke menu sebelumnya']

m21 = ['1. Input Soal secara manual', '2. Input soal dari file.', '3. Hitung Solusi.',
        '4. Tulis solusi ke dalam file.', '5. Kembali ke menu sebelumnya', '6. Kembali ke menu utama']

menu_trap = ['1. Persamaan polinom pangkat 2', '2. Persamaan polinom pangkat 3', '3. Persamaan polinom pangkat 4', '4. Kembali ke menu sebelumnya']



def mula(nilai,matriks):
    print("========================================")
    print('%s > %s ' % (m0, matriks[nilai-1] ))
    print("----------------------------------------")

##fungsi untuk menampilkan header menu 2
def mula1(nilai1, nilai2,matriks1, matriks2):
    print("========================================")
    print('%s > %s > %s ' % (m0, matriks1[nilai1-1], matriks2[nilai2-1]))
    print("----------------------------------------")
def mula2(nilai1, nilai2, nilai3, matriks1, matriks2, matriks3):
    print("========================================")
    print('%s > %s > %s > %s' % (m0, matriks1[nilai1-1], matriks2[nilai2-1], matriks3[nilai3-1]))
    print("----------------------------------------")
##fungsi menampilkan daftar menu pilihan 1
def menu1(menu_gauss):
    for x in (menu_gauss):
        print(x)
##fungsi menampilkan daftar menu inputan soal
def menu2():
    for x in m21:
        print(x)
    print()
def header1():
    print("========================================")
    print("MENU UTAMA")
    print("----------------------------------------")

def header2():
    print('******************************************************')
    print('*******SOFTWARE KALKULATOR PERHITUNGAN NUMERIK *******')
    print('Programmer\t\t: 1. Muhammad Ulil Albab\t 12315055\n'
          '\t\t\t  2. Jeremy Bona Carlo\t\t 12315005')
    print('versi\t\t\t: 1.0')
    print('Last Updated \t\t: 10 November 2019')
    print('******************************************************')
    print('contact\t\t\t: [ ulilaalbb@gmail.com ]')
    print('\t\t\t: [ jeremybonacarlo@yahoo.com ]\n\n')

def punyakita():
    print('Program adalah software yang didesain khusus untuk melakukan perhitungan secara matematis untuk ')
    print('berbagai permasalahan persamaan matematika dengan metode-metode tertentu. User dapat ')
    print('melakukan input bilangan-bilangan variabel maupun file yang telah dipersiapkan sebelumnya untuk ')
    print('diselesaikan di program ini. Metode-metode matematis yang dimaksud adalah Metode Gauss, Metode ')
    print('Trapezoidal, Metode Regresi Kuadrat Terkecil, dan Metode Interpolasi Polinom Newton. Dari masing-')
    print('masing metode, diperoleh pilihan untuk menyelesaikan permasalahan tiga variabel atau pun lebih dari ')
    print('tiga variabel seperti Metode Gauss, dan persamaan polinom pangkat dua atau lebih dari dua seperti ')
    print('Metode Trapezoidal. Langkah-langkah untuk menjalankan program sudah berada dalam urutan di buku ')
    print('panduan berikut, terima kasih. -Pemrogram')



