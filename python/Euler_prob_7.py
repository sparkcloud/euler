# 10,001st prime
#
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13
#
# What is the 10001st prime number?

import logging

#configure logger
logging.basicConfig(
    filename="Ep7.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def prime(amt):
    primes = [2]
    num = 3

    while amt > len(primes):
        sqrtNum = num ** 0.5
        for factor in primes:
            if num % factor == 0:
                break
            if factor > sqrtNum:
                primes.append(num)
                break
        num += 1
    
    return primes

def main():
    try:
        amt = int(input("Enter an amount of primes to return:"))
        primes = prime(amt)
        print(primes.pop())
    except Exception as e:
        logging.debug(f"exception occurred {e}")
    return

if __name__ == "__main__":
    main()