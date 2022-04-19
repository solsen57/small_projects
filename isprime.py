#determine if a number is prime
def main():
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
        i = 2
        primes = []
        while i <= num:
            if isPrime(i) == 1:
                primes.append(i)
                i+=1
            else:
                i+=1
        print('There are {} prime numbers between 1 and {}'.format(len(primes),num))
        print(primes)

    #only accept positive integers
    while True:
        gn = int(input('What number do you want to look at? '))
        if gn <= 0:
            print('Please input a positive integer. \n')
            continue
        elif gn == 1:
            print('1 is not a prime number and there are no prime numbers before 1. \n')
            continue
        else:
            break

    print('')

    while True:
        gn_choice = int(input('Would you like to: \n[1] State if your number is prime \n[2] State list of prime numbers up to/including your number \n[3] State both if your number is a prime and a list of prime numbers \n\n'))
        print('')

        if gn_choice == 1:
            if isPrime(gn) == 1:
                print('{} is a prime number!'.format(gn))
            else:
                print('{} is not a prime number'.format(gn))
            break
        elif gn_choice == 2:
            listPrime(gn)
            break
        elif gn_choice == 3:
            if isPrime(gn) == 1:
                print('{} is a prime number!'.format(gn))
            else:
                print('{} is not a prime number'.format(gn))
            listPrime(gn)
            break
        else:
            print('Invalid input. \n')
            continue

main()
