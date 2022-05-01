import numpy as np

def bul_matrix(rw, cl):
    c = rw*cl
    M1 = np.zeros(c, dtype = 'float64')
    M1 = M1.reshape(rw, cl)
    return M1

def fill_matrix(M, list1):
    cl = len(M[0])
    rw = len(M)
    M2 = M.reshape(1, rw*cl)
    i = 0
    while i < (rw*cl):
        for x in list1:
            M2[0,i] = x
            i+=1
    M2 = M2.reshape(rw, cl)
    return M2

def mult_matrix(n, M):
    cl = len(M[0])
    rw = len(M)
    M3 = M.reshape(1, rw*cl)
    i = 0
    while i < (rw*cl):
        M3[0,i] = n * M3[0,i]
        i+=1
    M3 = M3.reshape(rw, cl)
    return M3

def matrix_add(M1, M2):
    cl = len(M1[0])
    rw = len(M2)
    M3 = bul_matrix(rw, cl)
    for i in range(rw):
        for j in range(cl):
            M3[i][j] = M1[i][j] + M2[i][j]
    return M3
