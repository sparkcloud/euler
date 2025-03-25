# The sum of the squares of the first ten natural numbers is,
#   1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import logging

#Configure logging
logging.basicConfig(
    filename="Ep6.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

def squareOfSum(n):

    sum = 0

    for x in range(1,n+1):
        sum += x

    val = pow(sum,2)
    
    logger.debug(f"The square of sum is {val}")

    return val

def sumOfSquares(n):

    sum = 0

    for x in range(1,n+1):
        sum += pow(x,2)

    logger.debug(f"The sum of all the squares is {sum}")

    return sum

def main():
    print("Quit at anytime by entering a non-numeric key")
    try:
        num = int(input("Enter a integer number for the sum of squares and square of sums: "))
        total = squareOfSum(num) - sumOfSquares(num)
        print("The difference between the sum of squares and the square of the sum is: {}".format(total))
    except ValueError as e:
        print(f"Detected {num}, Ending program...")

if __name__ == "__main__":
    main()