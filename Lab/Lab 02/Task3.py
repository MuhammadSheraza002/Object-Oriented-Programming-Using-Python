import random

def a_b_c_d():
	a = random.randint(1,99)
	b = random.randint(1,99)
	c = random.randint(1,99)
	d = random.randint(1,99)
	print (a," ",b," ",c," ",d)
	if a <= b:#first level
		if b <= c:#second level
			if c <= d:#a b c d-
				print (a,"  ",b,"  ",c,"  ",d)
			#a <= b and b <= c and d < c means a <= b <= c and d < c, how about a, b & d
			elif b <= d:#a b d c-
				print (a,"  ",b,"  ",d,"  ",c)
			#a <= b and b <= c and d < c and d < b, means a <= b <= c, how about a & d
			elif d <= a:#d a b c-
				print (d,"  ",a,"  ",b,"  ",c)
			#a <= b and b <= c and d < c and d < b and a < d 
			else:#a d b c-
				print (a,"  ",d,"  ",b,"  ",c)
		#a <= b and c < b, how about a and c
		elif a <= c:#second level
			#a <= b and c < b and a <= c means a<=c<b, how about d
			if b <= d:#a c b d-
				print (a,"  ",c,"  ",b,"  ",d)
			#a <= b and c < b and a <= c and d < b means a<=c<b, how about a,c,d
			elif d <= a:#d a c b-
				print (d,"  ",a,"  ",c,"  ",b)
			#a <= b and c < b and a <= c and d < b and a < d means a<=c<b, how about d & c
			elif c <= d:#a c d b
				print (a,"  ",c,"  ",d,"  ",b)
			#a <= b and c < b and a <= c and d < b and a < d and d < c means a<d<c<=b
			else:#a d c b-
				print (a,"  ",d,"  ",c,"  ",b)
		else:#second level
			#a <= b and c < b and c < a means c < a <= b, how about d
			if b <= d:#c a b d
				print (c,"  ",a,"  ",b,"  ",d)
			#a <= b and c < b and c < a and d < b means c < a <= b, how about a,c & d
			elif a <= d:#c a d b-
				print (c,"  ",a,"  ",d,"  ",b)
			#a <= b and c < b and c < a and d < b and d < a means c < a <= b, how about c & d
			elif c <= d:#c d a b
				print (c,"  ",d,"  ",a,"  ",b)
			else:#d c a b
				print (d,"  ",c,"  ",a,"  ",b)
	else:#first level
	    #b < a 
		if a <= c:#second level
		    #b < a <= c, how about d
			if c <= d:#b a c d-
				print (b,"  ",a,"  ",c,"  ",d)
			#b < a <= c and d < c,  
			elif d <= b:#d b a c-
				print (d,"  ",b,"  ",a,"  ",c)
			#b < a <= c and d < c and b < d, how about a & d
			elif d <= a:#b d a c-
				print (b,"  ",d,"  ",a,"  ",c)
			#b < a <= c and d < c and b < d and a < d means b < a <= d < c 
			else:#b a d c-
				print (a,"  ",d,"  ",d,"  ",c)
		#b < a and c < a
		elif c <= b:#second level
		    #b < a and c < a and c <= b means c <= b < a, how about d	
			if a <= d:#c b a d-
				print (c,"  ",b,"  ",a,"  ",d)
			#b < a and c < a and c <= b and d < a means c <= b < a, how about c & d
			elif d <= c:#d c b a-
				print (d,"  ",c,"  ",b,"  ",a)
			#b < a and c < a and c <= b and d < a and c < d means c <= b  < a, how about b & d
			elif b <= d:#c b d a-
				print (c,"  ",b,"  ",d,"  ",a)
			#b < a and c < a and c <= b and d < a and c < d and d < b means c < d < b < a
			else:#c d b a-
				print (c,"  ",d,"  ",b,"  ",a)
		#b < a and c < a and b < c
		else:#second level
		    #b < a and c < a and b < c means b < c < a, how about d	
			if a <= d:#b c a d-
				print (b,"  ",c,"  ",a,"  ",d)
		    #b < a and c < a and b < c and d < a means b < c < a, how about c & d	
			elif c <= d:#b c d a-
				print (b,"  ",c,"  ",d,"  ",a)
	        #b < a and c < a and b < c and d < a and d < c means b < c < a, how about b & d	
			elif d <= b:#d b c a-
				print (d,"  ",b,"  ",c,"  ",a)
			#b < a and c < a and b < c and d < a and d < c and b < d means b < d < c < a
			else:
			    print (b,"  ",d,"  ",c,"  ",a)

a_b_c_d()
