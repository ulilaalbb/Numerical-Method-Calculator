import numpy as np



def gauss_3spl(a,b):
    [m, n] = a.shape
    a1 = np.zeros((m, n))
    b1 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a1[i, j] = a[i, j] * a[0, 0] * a[1, 0] * a[2, 0] / a[i, 0]
    b1[i] = b[i] * a[0, 0] * a[1, 0] * a[2, 0] / a[i, 0]
    # langkah 2
    for i in range(1, m):
        for j in range(0, n):
            a1[i, j] = a1[i, j] - a1[0, j]
    b1[i] = b1[i] - b1[0]
    # langkah 3
    a2 = np.zeros((m, n))
    b2 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a2[i, j] = a1[i, j]
            b2[i] = b1[i]

    for i in range(1, m):
        for j in range(0, n):
            a2[i, j] = a1[i, j] * a1[1, 1] * a1[2, 1] / a1[i, 1]
        b2[i] = b1[i] * a1[1, 1] * a1[2, 1] / a1[i, 1]
    # langkah 4
    for i in range(2, m):
        for j in range(0, n):
            a2[i, j] = a2[i, j] - a2[1, j]
        b2[i] = b2[i] - b2[1]
    # langkah 5
    x = np.zeros(m)
    x[2] = b2[2] / a2[2, 2]
    x[1] = [b2[1] - a2[1, 2] * x[2]] / a2[1, 1]
    x[0] = [b2[0] - a2[0, 2] * x[2] - a2[0, 1] * x[1]] / a2[0, 0]

    return x





def gauss_4spl(a,b):
    [m, n] = a.shape
    a1 = np.zeros((m, n))
    b1 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a1[i, :] = a[i, :] * a[0, 0] * a[1, 0] * a[2, 0] * a[3, 0] / a[i, 0]
        b1[i] = b[i] * a[0, 0] * a[1, 0] * a[2, 0] * a[3, 0] / a[i, 0]
    1
    # langkah 2
    for i in range(1, m):
        a1[i, :] = a1[i, :] - a1[0, :]
        b1[i] = b1[i] - b1[0]

    a2 = np.zeros((m, n))
    b2 = np.zeros(m)
    for i in range(0, m):
        a2[i, :] = a1[i, :]
        b2[i] = b1[i]

    for i in range(1, m):
        a2[i, :] = a1[i, :] * a1[1, 1] * a1[2, 1] * a[3, 1] / a1[i, 1]
        b2[i] = b1[i] * a1[1, 1] * a1[2, 1] * a[3, 1] / a1[i, 1]

    # langkah 2
    for i in range(2, m):
        a2[i, :] = a2[i, :] - a2[1, :]
        b2[i] = b2[i] - b2[1]

    a3 = np.zeros((m, n))
    b3 = np.zeros(m)
    for i in range(0, m):
        a3[i, :] = a2[i, :]
        b3[i] = b2[i]

    for i in range(2, m):
        a3[i, :] = a2[i, :] * a2[2, 2] * a2[3, 2] / a2[i, 2]
        b3[i] = b2[i] * a2[2, 2] * a2[3, 2] / a2[i, 2]

    # langkah 2
    for i in range(3, m):
        a3[i, :] = a3[i, :] - a3[2, :]
        b3[i] = b3[i] - b3[2]

    x = np.zeros(m)

    x[3] = b3[3] / a3[3, 3]
    x[2] = (b3[2] - a3[2, 3] * x[3]) / a3[2, 2]
    x[1] = (b3[1] - a3[1, 3] * x[3] - a3[1, 2] * x[2]) / a3[1, 1]
    x[0] = (b3[0] - a3[0, 3] * x[3] - a3[0, 2] * x[2] - a3[0, 1] * x[1]) / a3[0, 0]

    return x

def gauss_5spl(a,b):
    [m, n] = a.shape
    a1 = np.zeros((m, n))
    b1 = np.zeros(m)
    for i in range(0, m):
        for j in range(0, n):
            a1[i, :] = a[i, :] * a[0, 0] * a[1, 0] * a[2, 0] * a[3, 0] *a[4,0]/ a[i, 0]
        b1[i] = b[i] * a[0, 0] * a[1, 0] * a[2, 0] * a[3, 0]*a[4,0] / a[i, 0]
    1
    # langkah 2
    for i in range(1, m):
        a1[i, :] = a1[i, :] - a1[0, :]
        b1[i] = b1[i] - b1[0]

    a2 = np.zeros((m, n))
    b2 = np.zeros(m)
    for i in range(0, m):
        a2[i, :] = a1[i, :]
        b2[i] = b1[i]

    for i in range(1, m):
        a2[i, :] = a1[i, :] * a1[1, 1] * a1[2, 1] * a1[3, 1]*a1[4,1] / a1[i, 1]
        b2[i] = b1[i] * a1[1, 1] * a1[2, 1] * a1[3, 1]*a1[4,1] / a1[i, 1]


    for i in range(2, m):
        a2[i, :] = a2[i, :] - a2[1, :]
        b2[i] = b2[i] - b2[1]

    a3 = np.zeros((m, n))
    b3 = np.zeros(m)
    for i in range(0, m):
        a3[i, :] = a2[i, :]
        b3[i] = b2[i]

    for i in range(2, m):
        a3[i, :] = a2[i, :] * a2[2, 2] * a2[3, 2]*a2[4,2] / a2[i, 2]
        b3[i] = b2[i] * a2[2, 2] * a2[3, 2] *a2[4,2]/ a2[i, 2]


    for i in range(3, m):
        a3[i, :] = a3[i, :] - a3[2, :]
        b3[i] = b3[i] - b3[2]

    a4 = np.zeros((m, n))
    b4 = np.zeros(m)
    for i in range(0, m):
        a4[i, :] = a3[i, :]
        b4[i] = b3[i]

    for i in range(3, m):
        a4[i, :] = a3[i, :] *  a3[3, 3] * a3[4, 3]*a3[4,3] / a3[i, 3]
        b4[i] = b3[i] * a3[3, 3] * a3[4, 3]* a3[4,3] / a3[i, 3]

    for i in range(4, m):
        a4[i, :] = a4[i, :] - a4[2, :]
        b4[i] = b4[i] - b4[3]


    x = np.zeros(m)
    x[4] = b4[4] / a4[4,4]
    x[3] = b4[3] - a4[3,4] * x[4]  / a4[3, 3]
    x[2] = (b4[2] - a4[2,4] * x[4] -a4[2, 3] * x[3]) / a4[2, 2]
    x[1] = (b4[1] - a4[1,4] * x[4] -a4[1, 3] * x[3] - a4[1, 2] * x[2]) / a4[1, 1]
    x[0] = (b4[0] - a4[0,4] * x[4] - a4[0, 3] * x[3] - a4[0, 2] * x[2] - a4[0, 1] * x[1]) / a4[0, 0]

    return x



def input3_gauss():
    a = np.zeros((3,3))
    b = np.zeros(3)
    for i in range(3):
        for l in range(3):
            tmp = float(input('masukkan angka persamaan %d untuk x%d : '%(i+1,l)))
            a[i,l] = tmp
        b[i] = float(input('masukkan hasil dari persamaan %d : ' %(i+1)))
        b = b.transpose()

    return a,b


def input4_gauss():
    a = np.zeros((4, 4))
    b = np.zeros(4)
    for i in range(4):
        for l in range(4):
            tmp = float(input('masukkan angka persamaan %d untuk x%d : ' % (i + 1, l)))
            a[i, l] = tmp
        b[i] = float(input('masukkan hasil dari persamaan %d : ' % (i + 1)))

    b = b.transpose()
    return a,b


def input5_gauss():
    a = np.zeros((5, 5))
    b = np.zeros(5)
    for i in range(5):
        for l in range(5):
            tmp = float(input('masukkan angka persamaan %d untuk x%d : ' % (i + 1, l)))
            a[i, l] = tmp
        b[i] = float(input('masukkan hasil dari persamaan %d : ' % (i + 1)))
        b = b.transpose()
    return a,b

def print_gauss3(a,b):
    m,n = a.shape
    for i in range(m):
            print('%dx0 + %dx1 + %dx2  = '%(a[i,0], a[i,1], a[i,2]), end= " ")
            print(b[i])


def print_gauss4(a,b):
    m,n = a.shape
    for i in range(m):
            print('%dx0 + %dx1 + %dx2 + %dx3 + = '%(a[i,0], a[i,1], a[i,2], a[i,3]), end= " ")
            print(b[i])

def print_gauss5(a,b):
    m,n = a.shape
    for i in range(m):
            print('%dx0 + %dx1 + %dx2 + %dx3 + %dx4 = '%(a[i,0], a[i,1], a[i,2], a[i,3], a[i,4]), end= " ")
            print(b[i])