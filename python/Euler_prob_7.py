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

def prime(num):

    for x in range(2,num):
        if num % x != 0:
            return False
    
    return True

def main():
    print(prime(5))
    return

if __name__ == "__main__":
    main()