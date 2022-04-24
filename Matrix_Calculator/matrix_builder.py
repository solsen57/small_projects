import numpy as np

def bul_matrix(rw, cl):
    c = rw*cl
    M1 = np.arange(c)
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
