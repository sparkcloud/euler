# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1
# to 20?

import math

max = 20
num = 1
check = 0
valid = True

while valid:
	for x in range(max,0,-1):
		if num % x != 0:
			check = 0
			break
		else:
			check += 1
	
	if check == max:
		break
	else:
		num += 1	
    
print("Final num: {}".format(num))