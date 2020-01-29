import numpy as np



def pol2():

    x2 = float(input("masukkan koefisien x^2 : "))
    x1 = float(input("masukkan koefisien x^1 : "))
    x0 = float(input("masukkan koefisien x^0 : "))
    xvar =[x2,x1,x0]

    return xvar

def pol3():
    x3 = float(input("masukkan koefisien x^3 : "))
    x2 = float(input("masukkan koefisien x^2 : "))
    x1 = float(input("masukkan koefisien x^1 : "))
    x0 = float(input("masukkan koefisien x^0 : "))
    xvar =[x3, x2,x1,x0]
    print('f(x) = %.2fx^3 + %.2fx^2 + %.2fx + %.2f' % (x3, x2, x1, x0))
    return xvar

def pol4():
    x4 = float(input("masukkan koefisien x^4 : " ))
    x3 = float(input("masukkan koefisien x^3 : "))
    x2 = float(input("masukkan koefisien x^2  : "))
    x1 = float(input("masukkan koefisien x^1 : "))
    x0 = float(input("masukkan koefisien x^0 : "))
    print('f(x) = %.2fx^4 + %.2fx^3 + %.2fx^2 + %.2fx + %.2f' % (x4, x3, x2, x1, x0))
    xvar = [x4, x3, x2, x1, x0]
    return xvar










def rentang():
    a = float(input('Masukkan nilai rentang bawah (a) : '))
    b = float(input('Masukkan nilai rentang atas (b) : '))
    grd = int(input('masukkan jumlah grid yang anda inginkan : '))
    return a,b,grd


def integral2(bwh, ats, grd,xvar):
    def f2(xvar, x):
        x2 = xvar[0]
        x1 = xvar[1]
        x0 = xvar[2]
        return x2 * (x ** 2) + x1 * x + x0

    hasil = np.zeros(1)

    a = bwh
    b = ats
    h = (b-a)/grd
    hasil = 0.5*f2(xvar,a)
    for j in range(1,grd):
        xj = a+h*j
        hasil = hasil + f2(xvar, xj)
    hasil= (hasil+0.5*f2(xvar,b))*h
    return hasil

def integral3(bwh, ats, grd,xvar):
    def f3(xvar, x):
        x3 = xvar[0]
        x2 = xvar[1]
        x1 = xvar[2]
        x0 = xvar[3]
        return x3 * (x ** 3) + x2 * (x ** 2) + x1 * x + x0

    hasil = np.zeros(1)

    a = bwh
    b = ats
    h = (b-a)/grd
    hasil = 0.5*f3(xvar,a)
    for j in range(1,grd):
        xj = a+h*j
        hasil = hasil + f3(xvar, xj)
    hasil= (hasil+0.5*f3(xvar,b))*h
    return hasil

def integral4(bwh, ats, grd,xvar):
    def f4(xvar, x):
        x4 = xvar[0]
        x3 = xvar[1]
        x2 = xvar[2]
        x1 = xvar[3]
        x0 = xvar[4]
        return x4 * (x ** 4) + x3 * (x ** 3) + x2 * (x ** 2) + x1 * x + x0

    hasil = np.zeros(1)

    a = bwh
    b = ats
    h = (b-a)/grd
    hasil = 0.5*f4(xvar,a)
    for j in range(1,grd):
        xj = a+h*j
        hasil = hasil + f4(xvar, xj)
    hasil= (hasil+0.5*f4(xvar,b))*h
    return hasil
