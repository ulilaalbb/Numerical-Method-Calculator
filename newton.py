import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def inter_newton(x,y, N, x_soal):

    n_polinom = N
    ST = [[0 for j in range(n_polinom)]for i in range(N)]
    for i in range (N):
        ST[i][0]=y[i]
    for j in range (1,n_polinom):
        for i in range(N-j):
            ST[i][j] = (ST[i+1][j-1] - ST[i][j-1])/(x[i+j]-x[i])
    solusi = ST[0][0]

    for i in range(1,n_polinom):
        suku=ST[0][i]
        for j in range(i):
            suku = suku*(x_soal-x[j])
        solusi=solusi+suku

    N = 100
    x_min = x[0] - 5
    x_max = x[-1] + 5
    y_min = y[0]
    y_max = y[-1]
    x_plot = [0 for i in range(N)]
    y_plot = [0 for i in range(N)]
    for ii in range(N):
        x_plot[ii] = ((x_max - x_min) / N) * ii + x_min
        jumlah = ST[0][0]
        for i in range(1, n_polinom):
            suku = ST[0][i]
            for j in range(i):
                suku = suku * (x_plot[ii] - x[j])
            jumlah = jumlah + suku
        y_plot[ii] = jumlah

    fig, ax = plt.subplots()
    ax.plot(x, y, 'ro', label='data')
    ax.plot(x_soal, solusi, 'bs', label='titik yang diestimasi')
    ax.plot(x_plot, y_plot, "g", label='garis interpolasi derajat %d'%n_polinom)
    legend = ax.legend()
    plt.xlabel("x")
    plt.ylabel("f(x) = y")
    plt.axis([x_min, x_max, y_min, y_max])
    plt.show()
    return solusi


def input_newt():
    N = int(input('Input Orde Interpolasi Newton yang anda inginkan : '))
    print('untuk orde %d, maka dibutuhkan %d input data x dan f(x)! /n'%(N, N+1))
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    for i in range(N):
        x[i] = float(input('Masukkan nilai x ke-%d : ' % (i + 1)))
        y[i] = float(input('Masukkan nilai f(x) ke-%d : ' % (i + 1)))
        print('-----------------------------------------')
    xsoal = float(input('masukkan nilai x yang ingin dicari f(x) : '))
    print("Data berhasil di input!")
    for i in range(len(datax)):
        if i == 0:
            print('Data X : %.2f, ' % datax[i], end=" ")
        else:
            print('%.2f, '%datax[i], end=" ")

    print(' ')
    for i in range(len(datax)):
        if i == 0:
            print('Data Y : %.2f, ' % datay[i], end=" ")
        else:
            print('%.2f, '%datay[i], end=" ")
    print(' ')
    print('orde polinom : %d' % N)
    print('titik yang ingin dicari %.2f' % xsoal)
    return x,y,xsoal, N

def newt_input_file():
    data = pd.read_csv('INPUT NEWTON.csv', header = None)
    datax = np.array(data.iloc[0,1:])
    datay = np.array(data.iloc[1, 1:])
    N = int(data.iloc[2, 1])
    xsoal = np.array(data.iloc[3, 1])
    for i in range(len(datax)):
        if i == 0:
            print('Data X : %.2f, ' % datax[i], end=" ")
        else:
            print('%.2f, '%datax[i], end=" ")

    print(' ')
    for i in range(len(datax)):
        if i == 0:
            print('Data Y : %.2f, ' % datay[i], end=" ")
        else:
            print('%.2f, '%datay[i], end=" ")
    print(' ')
    print('orde polinom : %d' % N)
    print('titik yang ingin dicari %.2f' % xsoal)
    return datax,datay, xsoal, N


