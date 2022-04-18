#function to determine if a number is prime

def isPrime(num):
    i = 2
    factors = []
    while i < num:
        if (num % i == 0):
            factors.append(i)
            i+=1
        else:
            i+=1
    if len(factors) != 0:
        print('{} is not prime'.format(num))
    else:
        print('{} is prime'.format(num))

isPrime(6)
