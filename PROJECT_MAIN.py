import numpy as np
import matplotlib.pyplot as plt
from gauss import *
from newton import  *
from trapezoid import *
from localvar import *
from regresi import *
import pandas as pd

##inter_newton(x,y, N, x_soal):
##gauss_3spl(a,b):
##integral(bwh, ats, grd, fx):


loop = True
main_menus = True
header2()

while loop == True:
    if  main_menus == True:
        header1()
        menu1(mmenus)
        print("----------------------------------------")
    pilih = int(input("Masukkan menu untuk melanjutkan : "))
    ## main menus = menu utama
    ##main menus1 menu kedua
    ## main menu2 = menu solusi soal
    if pilih == 1:
        main_menus = False
        main_menus1 = True
        while main_menus1 == True:
            ## pilihan menu pertama
            mula(pilih, mmenus) ##menampilkan header menu > menu1
            menu1(menu_gauss)

            lanjut = int(input("Masukkan menu untuk melanjutkan : "))


            if lanjut ==1: # spl 3var
                main_menus1 = False
                main_menus2 = True
                a = []
                b = []
                while main_menus2 == True:
                    mula1(pilih, lanjut, mmenus, menu_gauss)
                    menu2()
                    lanjut2 = int(input("Masukkan menu untuk melanjutkan : "))
                    if lanjut2 == 1: #input manual
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        a = []
                        b = []
                        a,b = input3_gauss()
                        print('input berhasil!')
                        print_gauss3(a,b)
                    if lanjut2 ==2: #input dari file
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        a = [];
                        b = [];
                        mat = pd.read_csv('gauss3.csv')
                        a = mat.iloc[:, 0:3]
                        a = np.array(a)
                        b = mat.iloc[:, 3]
                        b = np.array(b).transpose()
                        print('input berhasil!')
                        print_gauss3(a, b)
                    if lanjut2 ==3: #hitung solusi
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        if a.size != 0:
                            print_gauss3(a,b)
                            solusi = gauss_3spl(a,b)
                            print('solusi didapatkan!')
                            ii = 0
                            for x in solusi:
                                print('x%d  = ' %ii,x)
                                ii +=1

                        else:
                            print('masukkin soal dulu')
                    if lanjut2 ==4:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        f = open('solusi_gauss_3_spl.txt', 'w+')
                        f.write('nilai x persamaan SPL 3 Variabel :\n\n')
                        for i in range(len(a)):
                            f.write('x%d = %d\n' %(i, solusi[i]))
                        f.close()
                        print('Solusi berhasil di simpan kedalam file (solusi_gauss_3_spl.txt)!')
                    if lanjut2 == 5:
                        main_menus2 = False
                        main_menus1 = True
                    elif lanjut2 == 6:
                        main_menus = True
                        main_menus2 = False
                        main_menus1 = False
            elif lanjut ==2: ##spl 4 var
                main_menus1 = False
                main_menus2 = True
                a = []
                b = []
                while main_menus2 == True:
                    mula1(pilih, lanjut, mmenus, menu_gauss)
                    menu2()
                    lanjut2 = int(input("Masukkan menu untuk melanjutkan : "))
                    if lanjut2 == 1:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        a = []
                        b = []
                        a,b = input4_gauss()
                        print('input berhasil!')
                        print_gauss4(a,b)
                    if lanjut2 ==2:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        a = [];
                        b = [];
                        mat = pd.read_csv('gauss4.csv')
                        a = mat.iloc[:, 0:4]
                        a = np.array(a)
                        b = mat.iloc[:, 4]
                        b = np.array(b).transpose()
                        print('input berhasil!')
                        print_gauss4(a, b)
                    if lanjut2 ==3:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        if a.size != 0:
                            print_gauss4(a,b)
                            solusi = gauss_4spl(a,b)
                            print('solusi didapatkan!')
                            ii = 0
                            for x in solusi:
                                print('x%d  = ' % ii, x)
                                ii += 1

                        else:
                            print('masukkin soal dulu')
                    if lanjut2 ==4:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        f = open('solusi_gauss_4_spl.txt', 'w+')
                        f.write('nilai x persamaan SPL 4 Variabel :\n\n')
                        for i in range(len(a)):
                            f.write('x%d = %d\n' %(i, solusi[i]))
                        f.close()
                        print('Solusi berhasil di simpan kedalam file (solusi_gauss_4_spl.txt)!')
                    if lanjut2 == 5:
                        main_menus2 = False
                        main_menus1 = True
                    elif lanjut2 == 6:
                        main_menus = True
                        main_menus2 = False
                        main_menus1 = False
            elif lanjut ==3: #spl 5 var
                main_menus1 = False
                main_menus2 = True
                a = []
                b = []
                while main_menus2 == True:
                    mula1(pilih, lanjut, mmenus, menu_gauss)
                    menu2()
                    lanjut2 = int(input("Masukkan menu untuk melanjutkan : "))
                    if lanjut2 == 1:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        a = []
                        b = []
                        a,b = input5_gauss()
                        print('Input berhasil!')
                        print_gauss5(a, b)
                    if lanjut2 ==2:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        a = [];
                        b = [];
                        mat = pd.read_csv('gauss5.csv')
                        a = mat.iloc[:, 0:5]
                        a = np.array(a)
                        b = mat.iloc[:, 5]
                        b = np.array(b).transpose()
                        print('Input berhasil!')
                        print_gauss5(a,b)
                    if lanjut2 ==3:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        if a.size != 0:
                            print_gauss5(a,b)
                            solusi = gauss_5spl(a,b)
                            print('solusi didapatkan!')
                            ii = 0
                            for x in solusi:
                                print('x%d  = ' % ii, x)
                                ii += 1
                        else:
                            print('masukkin soal dulu')
                    if lanjut2 ==4:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        f = open('solusi_gauss_5_spl.txt', 'w+')
                        f.write('nilai x persamaan SPL 5 Variabel :\n\n')
                        for i in range(len(a)):
                            f.write('x%d = %d\n' %(i, solusi[i]))
                        f.close()
                        print('Solusi berhasil di simpan kedalam file (solusi_gauss_4_spl.txt)!')
                    if lanjut2 == 5:
                        main_menus2 = False
                        main_menus1 = True
                    elif lanjut2 == 6:
                        main_menus = True
                        main_menus2 = False
                        main_menus1 = False
            elif lanjut == 4:
                main_menus2 = False
                main_menus1 = False
                main_menus = True
                break
            else:
                print("Input salah! silahkan masukkan angka sesuai pilihan yang ada.")
                main_menus1 = True

    elif pilih ==2:
        x = []
        y = []
        main_menus = False
        main_menus1 = True
        while main_menus1 == True:
            ## pilihan menu pertama
            mula(pilih, mmenus)
            menu1(menu_trap)

            lanjut = int(input("Masukkan menu untuk melanjutkan : "))

            if lanjut ==1: #polinom pangkat 2
                main_menus1 = False
                main_menus2 = True
                while main_menus2 == True:
                    mula1(pilih, lanjut, mmenus, menu_trap)
                    menu2()
                    lanjut2 = int(input("Masukkan menu untuk melanjutkan : "))
                    if lanjut2 == 1: #input manual
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        xvar = np.array(pol2())
                        a,b,grd = rentang()
                        print('Input berhasil!')
                        print('f(x) = %.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2]))
                        print('Batas bawah (a) : %d' % a)
                        print('Batas bawah (b) : %d' % b)
                        print('Jumlah Grid (N) : %d' % grd)

                    if lanjut2 ==2: #input dari file
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        mat = pd.read_csv('INPUT TRAPEZOIDAL - Persamaan polinom pangkat 2.csv')
                        xvar = mat.iloc[0, 0:3]
                        xvar = np.array(xvar)
                        a = mat.iloc[0, 3]
                        b = mat.iloc[0, 4]
                        grd = mat.iloc[0, 5]
                        print('Input berhasil!')
                        print('f(x) = %.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2]))
                        print('Batas bawah (a) : %d' % a)
                        print('Batas bawah (b) : %d' % b)
                        print('Jumlah Grid (N) : %d' % grd)
                    if lanjut2 ==3: #hitung solusi
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        if xvar.size != 0:
                            print('Persamaan : %.2fx^2 + %.2fx + %f.2'%(xvar[0],xvar[1],xvar[2]))
                            print('rentang bawah (a) \t= ', a)
                            print('rentang atas (b) \t= ', b)
                            print('jumlah grid \t\t= ', grd)
                            solusi = integral2(a,b,grd,xvar)
                            print('solusi didapatkan!')
                            print('I \t\t\t= ',solusi)

                        else:
                            print('masukkin soal dulu')
                    if lanjut2 ==4:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        f = open('Hasil Metoda Trapezoid polinom pangkat 2.txt', 'w+')
                        f.write('Persamaan : %.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2]))
                        f.write('\nrentang bawah (a)\t= ' + str(a))
                        f.write('\nrentang atas (b)\t= ' + str(b))
                        f.write('\njumlah grid \t\t= ' + str(grd))
                        f.write('\nI\t\t\t= ' + str(solusi))
                        f.close()
                        print('Solusi berhasil di simpan kedalam file (Hasil Metoda Trapezoid polinom pangkat 2.txt)!')

                    if lanjut2 == 5:
                        main_menus2 = False
                        main_menus1 = True
                    elif lanjut2 == 6:
                        main_menus = True
                        main_menus2 = False
                        main_menus1 = False
            elif lanjut ==2: #polinom pangkat 3
                main_menus1 = False
                main_menus2 = True
                while main_menus2 == True:
                    mula1(pilih, lanjut, mmenus, menu_trap)
                    menu2()
                    lanjut2 = int(input("Masukkan menu untuk melanjutkan : "))
                    if lanjut2 == 1:  # input manual
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        xvar = np.array(pol3())
                        a, b, grd = rentang()
                        print('Input berhasil!')
                        print('f(x) = %.2fx^3 + %.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2], xvar[3]))
                        print('Batas bawah (a) : %d' % a)
                        print('Batas bawah (b) : %d' % b)
                        print('Jumlah Grid (N) : %d' % grd)
                    if lanjut2 == 2:  # input dari file
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        mat = pd.read_csv('INPUT TRAPEZOIDAL - Persamaan polinom pangkat 3.csv')
                        xvar = mat.iloc[0, 0:4]
                        xvar = np.array(xvar)
                        a = mat.iloc[0, 4]
                        b = mat.iloc[0, 5]
                        grd = mat.iloc[0, 6]
                        print('Input berhasil!')
                        print('f(x) = %.2fx^3 + %.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2], xvar[3]))
                        print('Batas bawah (a) : %d' % a)
                        print('Batas bawah (b) : %d' % b)
                        print('Jumlah Grid (N) : %d' % grd)
                    if lanjut2 == 3:  # hitung solusi
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        if xvar.size != 0:
                            print('Persamaan : %.2fx^3 + %.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2],xvar[3]))
                            print('rentang bawah (a) \t= ', a)
                            print('rentang atas (b) \t= ', b)
                            print('jumlah grid \t\t= ', grd)
                            solusi = integral3(a, b, grd, xvar)
                            print('solusi didapatkan!')
                            print('I \t\t\t= ', solusi)

                        else:
                            print('masukkin soal dulu')
                    if lanjut2 == 4:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        f = open('Hasil Metoda Trapezoid polinom pangkat 3.txt' , 'w+')
                        f.write('Persamaan : %.2fx^3 +%.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2],xvar[3]))
                        f.write('\nrentang bawah (a)\t= ' + str(a))
                        f.write('\nrentang atas (b)\t= ' + str(b))
                        f.write('\njumlah grid \t\t= ' + str(grd))
                        f.write('\nI\t\t\t= ' + str(solusi))
                        f.close()
                        print('Solusi berhasil di simpan kedalam file (Hasil Metoda Trapezoid polinom pangkat 3.txt)!')
                    if lanjut2 == 5:
                        main_menus2 = False
                        main_menus1 = True
                    elif lanjut2 == 6:
                        main_menus = True
                        main_menus2 = False
                        main_menus1 = False
            elif lanjut ==3:    #polinom pangkat 4
                main_menus1 = False
                main_menus2 = True
                while main_menus2 == True:
                    mula1(pilih, lanjut, mmenus, menu_trap)
                    menu2()
                    lanjut2 = int(input("Masukkan menu untuk melanjutkan : "))
                    if lanjut2 == 1:  # input manual
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        xvar = np.array(pol4())
                        a, b, grd = rentang()
                        print('Input berhasil!')
                        print('f(x) = %.2fx^4 +%.2fx^3 + %.2fx^2 + %.2fx + %.2f' % (
                        xvar[0], xvar[1], xvar[2], xvar[3], xvar[4]))
                        print('Batas bawah (a) : %d' % a)
                        print('Batas bawah (b) : %d' % b)
                        print('Jumlah Grid (N) : %d' % grd)
                    if lanjut2 == 2:  # input dari file
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        mat = pd.read_csv('INPUT TRAPEZOIDAL - Persamaan polinom pangkat 4.csv')
                        xvar = mat.iloc[0, 0:5]
                        xvar = np.array(xvar)
                        a = mat.iloc[0, 5]
                        b = mat.iloc[0, 6]
                        grd = mat.iloc[0, 7]
                        print('Input berhasil!')
                        print('f(x) = %.2fx^4 +%.2fx^3 + %.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2], xvar[3], xvar[4]))
                        print('Batas bawah (a) : %d' % a)
                        print('Batas bawah (b) : %d' % b)
                        print('Jumlah Grid (N) : %d' % grd)
                    if lanjut2 == 3:  # hitung solusi
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        if xvar.size != 0:
                            print('Persamaan : %.2fx^4 + %.2fx^3 + %.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2], xvar[3],xvar[4]))
                            print('rentang bawah (a) \t= ', a)
                            print('rentang atas (b) \t= ', b)
                            print('jumlah grid \t\t= ', grd)
                            solusi = integral4(a, b, grd, xvar)
                            print('solusi didapatkan!')
                            print('I \t\t\t= ', solusi)

                        else:
                            print('masukkin soal dulu')
                    if lanjut2 == 4:
                        mula2(pilih, lanjut, lanjut2, mmenus, menu_trap, m21)
                        f = open('Hasil Metoda Trapezoid polinom pangkat 4.txt', 'w+')
                        f.write('Persamaan : %.2fx^4 + %.2fx^3 +%.2fx^2 + %.2fx + %.2f' % (xvar[0], xvar[1], xvar[2], xvar[3], xvar[4]))
                        f.write('\nrentang bawah (a)\t= ' + str(a))
                        f.write('\nrentang atas (b)\t= ' + str(b))
                        f.write('\njumlah grid \t\t= ' + str(grd))
                        f.write('\nI\t\t\t= ' + str(solusi))
                        f.close()
                        print('Solusi berhasil di simpan kedalam file (Hasil Metoda Trapezoid polinom pangkat 4.txt)!')

                    if lanjut2 == 5:
                        main_menus2 = False
                        main_menus1 = True
                    elif lanjut2 == 6:
                        main_menus = True
                        main_menus2 = False
                        main_menus1 = False
            elif lanjut == 4:
                main_menus2 = False
                main_menus1 = False
                main_menus = True
                break
            else:
                print("Input salah! silahkan masukkan angka sesuai pilihan yang ada.")
                main_menus1 = True
            while main_menus2 ==True:
                mula1(pilih, lanjut, mmenus, menu_trap)
                menu2()
                lanjut2 = int(input("Masukkan menu untuk melanjutkan : "))
                if lanjut2 == 5:
                    main_menus2 = False
                    main_menus1 = True
                elif lanjut2 == 6:
                    main_menus = True
                    main_menus2 = False
                    main_menus1 = False

    elif pilih ==3:
        main_menus = False
        main_menus2 = True
        x = []
        y = []
        while main_menus2 == True:
            mula(pilih, mmenus)
            menu2()
            lanjut2 = int(input("Masukkan menu untuk melanjutkan : "))
            if lanjut2 == 1:
                mula1(pilih, lanjut2,mmenus, m21)
                x,y = input_reg()
            if lanjut2 == 2:
                mula1(pilih, lanjut2, mmenus, m21)
                x,y = reg_input_file()
            if lanjut2 == 3:
                mula1(pilih, lanjut2, mmenus, m21)
                a,b = least_square(x,y)
                y2 = plot_LQ(a,b,x,y)
                plt.show()
            if lanjut2 == 4:
                mula1(pilih, lanjut2, mmenus, m21)
                r1 = pd.Series(x)
                r2 = pd.Series(y)
                r3 = pd.Series(y2)
                datasave = pd.concat([r1,r2,r3], axis= 1)
                df = pd.DataFrame(datasave).rename(columns={ 0: 'x', 1 : 'y orig', 2 : 'y new'})
                df.to_csv('Hasil Metoda Regresi Least Square.csv')
                print('Solusi berhasil di save ke file : Hasil Metoda Regresi Least Square.csv ')
                y2 = plot_LQ(a, b, x, y)
                plt.savefig('Regresi Least Square - grafik.png')
            if lanjut2 == 5:
                main_menus2 = False
                main_menus = True
            elif lanjut2 == 6:
                main_menus = True
                main_menus2 = False

    elif pilih == 4:
        main_menus = False
        main_menus2 = True
        x = []
        y = []
        while main_menus2 == True:
            mula(pilih, mmenus)
            menu2()
            lanjut2 = int(input("Masukkan menu untuk melanjutkan : "))
            if lanjut2 == 1:
                mula1(pilih, lanjut2, mmenus, m21)
                x, y, N = input_newt()
            if lanjut2 == 2:
                mula1(pilih, lanjut2, mmenus, m21)
                x, y, xsoal, N = newt_input_file()

            if lanjut2 == 3:
                mula1(pilih, lanjut2, mmenus, m21)
                if len(x) == 0 :
                    print('Soal belum di input!')
                else:
                    solusi = inter_newton(x, y, N, xsoal)
                    print(solusi)
                    plt.show()
            if lanjut2 == 4:
                mula1(pilih, lanjut2, mmenus, m21)
                r1 = pd.Series(x)
                r2 = pd.Series(y)
                r3 = pd.Series(N)
                r4 = pd.Series(xsoal)
                r5 = pd.Series(solusi)
                datasave = pd.concat([r1, r2, r3, r4, r5], axis=1)
                df = pd.DataFrame(datasave).rename(columns={0: 'x', 1: 'y ', 2: 'Orde Polinom', 3 : 'x hitung', 4 : 'y hitung'})
                df.to_csv('Hasil Interpolasi Newton.csv')
                print('Solusi berhasil di save ke file : Hasil Interpolasi Newton.csv ')
                solusi = inter_newton(x, y, N, xsoal)
                plt.savefig('Interpolasi Newton - grafik.png')
            if lanjut2 == 5:
                main_menus2 = False
                main_menus = True
            elif lanjut2 == 6:
                main_menus = True
                main_menus2 = False
    elif pilih ==5:
        mula(pilih, mmenus)
        punyakita()


    elif pilih == 0:

        loop = False
    else :
        print("Input salah! silahkan masukkan angka sesuai pilihan yang ada.")
        main_menus = True








