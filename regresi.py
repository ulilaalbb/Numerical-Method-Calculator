
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def least_square(x,y):
    n = x.size  # jumlah data
    xtot = sum(x)  # jumlah seluruh data x
    ytot = sum(y)  # jumlah selurh data y
    x2tot = sum(x ** 2)  # penjumlahan seluruh data (x^2)
    xytot = sum(x * y)  # penjumlahan seluruh data x*y, sigma(x*y)

    # gradien regresi
    b = (n * xytot - xtot * ytot) / (n * x2tot - (xtot) ** 2)
    # titik potong di x= 0
    a = y.mean() - b * x.mean()
    return (a,b)



def input_reg():
    N = int(input('Masukkan jumlah data yang anda inginkan : '))
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range(N):
        x[i] = float(input('Masukkan nilai x ke-%d : ' % (i + 1 )))
    for j in range(N):
        y[i] = float(input('Masukkan nilai y ke-%d : ' % (j + 1)))

    print("Data berhasil di input!")
    for i in range(len(x)):
        if i == 0:
            print('Data x: %.2f, ' % x[i], end=" ")
        else:
            print('%.2f, '%x[i], end=" ")
    print(' ')
    for i in range(len(x)):
        if i == 0:
            print('Data y: %.2f, ' % y[i], end=" ")
        else:
            print('%.2f, ' % y[i], end=" ")
    print(' ')
    return x,y

def reg_input_file():
    data = pd.read_csv('INPUT REGRESI.csv')
    datax = np.array(data.iloc[:,0])
    datay = np.array(data.iloc[:, 1])

    for i in range(len(datax)):
        if i == 0:
            print('Data x: %.2f, ' % datax[i], end=" ")
        else:
            print('%.2f, '%datax[i], end=" ")
    print(' ')
    for i in range(len(datax)):
        if i == 0:
            print('Data y: %.2f, ' % datay[i], end=" ")
        else:
            print('%.2f, ' % datay[i], end=" ")
    print(' ')
    return datax,datay




def plot_LQ(a,b, x,y):

    ynew = a+ b*x
    plt.plot(x,y,'*g',markersize = 8, label = 'Data Original')
    plt.plot(x,ynew, 'r', linewidth = 3, label = 'Hasil Regresi')
    plt.title('Kurva Regresi Least Square')
    plt.legend()
    plt.xlabel('nilai X')
    plt.ylabel('nilai Y')
    plt.grid()
    plt.show()
    return ynew