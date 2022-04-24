import matrix_builder as mb
import numpy as np

u_rw = int(input('How many rows are there? '))
u_cl = int(input('How many columns are there? '))

A = mb.bul_matrix(u_rw, u_cl)

list = np.arange(u_rw * u_cl)
entires = [input('Entry? ') for x in list]

A1 = mb.fill_matrix(A, entires)
print(A1)
