import random

def _a_b_c():
	a = random.randint(1,99)
	b = random.randint(1,99)
	c = random.randint(1,99)
	print (a,"  ",b,"  ",c)
	if a <= b and b <= c:
		print (a,"  ",b,"  ",c)
	elif a <= c and c <= b:
		print (a,"  ",c,"  ",b)
	elif b <= a and a <= c:
		print (b,"  ",a,"  ",c)
	elif b <= c and c <= a:
		print (b,"  ",c,"  ",a)
	elif c <= a and a <= b:
		print (c,"  ",a,"  ",b)
	else:
		print (c,"  ",b,"  ",a)

_a_b_c()
