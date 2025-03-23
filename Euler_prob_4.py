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