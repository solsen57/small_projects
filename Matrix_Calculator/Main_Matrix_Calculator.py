import matrix_builder as mb
import numpy as np

while True:
    try:
        u_rw = int(input('How many rows are there? '))
        if u_rw <= 0:
            print('Invalid input. Please input a positive integer.')
        else:
            break
    except ValueError:
        print('Invalid input. Please input a positive integer.')

while True:
    try:
        u_cl = int(input('How many columns are there? '))
        if u_cl <= 0:
            print('Invalid input. Please input a positive integer.')
        else:
            break
    except ValueError:
        print('Invalid input. Please input a positive integer.')



A = mb.bul_matrix(u_rw, u_cl)

list = np.arange(u_rw * u_cl)
entires = [input('Entry? ') for x in list]

A1 = mb.fill_matrix(A, entires)
print(A1)

mul_ch = input('Is there a multiplier for your matrix? ').lower()
if mul_ch.startswith('y'):
    while True:
        try:
            mul = float(input('Please enter multiplier: '))
            break
        except ValueError:
            print('Invalid input.')
    A2 = mb.mult_matrix(mul, A1)
    print(A2)
