# Largest Prime Factor
# 
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29
# 
# What is the largest prime factor of the number 600851475143?

import math

def factors(num):
    factor = []
    
    for x in range(1,num+1):
        if num % x == 0:
            factor.append(x)

    return factor

def prime(arr):
    primes = []

    for x in arr:
        pfactor = factors(x)
        print("num:{} | factor: {}".format(x, pfactor))
        if len(pfactor) == 2:
            primes.append(pfactor[1])

    return primes

def main():
    # factor_arr = factors(600851475143)
    # print(factor_arr)
    # prime_factors = prime(factor_arr)
    # print(prime_factors)
    # print("Greatest prime factor: {}".format(prime_factors[-1]))
    num, aux = 600851475143, 2
    while num != 1:
        if not num % aux:
            num /= aux
        else:
            aux+=1
    print(aux)

if __name__ == "__main__":
    main()