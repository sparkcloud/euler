import math

k = 20
N = 1
i = 1

p = {1}
a = {1}

check = True
limit = math.sqrt(k)

while p[i] <= k:
	a[i] = 1
	if (check):
		if p[i] <= limit:
			a[i] = math.floor(math.log(k)/math.log(p[i]))
		else:
			check = false
	N = N * math.exp(p[i],a[i])
	i = i+1

print (N)