#determine if a number is prime
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
        return 0
    else:
        return 1

#list primes up to/including number
def listPrime(num):
    i = 4
    primes = [2, 3]
    while i <= num:
        if isPrime(i) == 1:
            primes.append(i)
            i+=1
        else:
            i+=1
    print('There are {} prime numbers between 2 and {}'.format(len(primes),num))
    print(primes)

listPrime(14)
