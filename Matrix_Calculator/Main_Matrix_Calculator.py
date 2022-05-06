import matrix_builder as mb
import numpy as np

def bul_matrix_input():
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
    return A1

def mult_matrix_input(A):
    mul_ch = input('Is there a multiplier for your matrix? ').lower()
    if mul_ch.startswith('y'):
        while True:
            try:
                mul = float(input('Please enter multiplier: '))
                break
            except ValueError:
                print('Invalid input.')
        A2 = mb.mult_matrix(mul, A)
        return A2
    else:
        return A

def matrix_add_sub_input(M1,M2):
    while True:
        try:
            if (len(M1[0]) != len(M2[0])) or (len(M1) != len(M2)):
                print('Matricies incompadible. Matricies must be the same dimensions')
                break
            else:
                add_sub_in = input('Are you adding (+) or subtracting (-) the matricies? ').lower()
                if (add_sub_in == '+') or (add_sub_in.startswith('a')):
                    M3 = mb.matrix_add(M1,M2)
                    return M3
                elif (add_sub_in == '-') or (add_sub_in.startswith('s')):
                    M3 = mb.matrix_sub(M1,M2)
                    return M3
                break
        except:
            pass

def matrix_mul_input(M1,M2):
    while True:
        try:
            if (len(M1[0]) != len(M2)):
                print('Matricies incompadible. Number of columns of first matrix must equal number of rows of second matrix')
                break
            else:
                M3 = mb.matrix_mul(M1,M2)
                return M3
                break
        except:
            pass

def main():
    print('Calculations are currently only able to handle 2 matricies.')
    print('Please input your first matrix.')
    M1 = bul_matrix_input()
    A1 = mult_matrix_input(M1)
    print(A1)
    print('Please input your second matrix.')
    M2 = bul_matrix_input()
    A2 = mult_matrix_input(M2)
    print(A2)
    funct_in = input('Are you adding (+), subtracting (-), or multiplying (*) the matricies? ').lower()
    if (funct_in == '+') or (funct_in.startswith('a')) or (funct_in == '-') or (funct_in.startswith('s')):
        A3 = matrix_add_sub_input(A1,A2)
        print(A3)
        return A3
    elif (funct_in == '*') or (funct_in.startswith('m')):
        A3 = matrix_mul_input(A1,A2)
        print(A3)
        return A3

if __name__ == '__main__':
    main()
    while True:
        answer = input('\nWould you like to do another calculation? (y/n) ').lower()
        if answer.startswith('y'):
            main()
        elif answer.startswith('n'):
            print('Goodbye!')
            exit()
        else:
            print('Invalid input. \n')
            continue
