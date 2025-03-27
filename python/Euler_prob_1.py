# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000

import math

sum = 0
limit = 1000

for x in range(1,limit):
    if x % 3 == 0 or x % 5 == 0:
        sum += x
    
print("The sum is {}".format(sum))

    