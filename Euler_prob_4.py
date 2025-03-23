#	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
#	9009 = 91 X 99
#
#	Find the largest palindrome made from the product of two 3-digit numbers.
#

pal_num = {}
total = ''

largest_num = 0
product1 = 0
product2 = 0

for i in range (999,0,-1):
	for x in range (i,0,-1):
		total = str(i * x)
		if total == total[::-1]:
			print('{} and {}'.format(i,x))
			if i*x > largest_num:
				largest_num = i*x
				product1 = i
				product2 = x

print(largest_num)
print('factors: {},{}'.format(product1,product2)) 