


def next_step(source, but):
	w = len(source)
	for x in xrange(w):
		c = source[(x-1)%w] + source[x] + source[(x+1)%w]
		if c>0 and c<3:
			but[x] = 1
		else:
			but[x] = 0

def printline(tab):
	print "".join([x and "O" or " " for x in tab])



if __name__ == "__main__" :
	
	w=150
	
	a = range(w)
	for i in range(w):
		a[i]=0
	
	a[w/2]=1
	b=range(w)
	
	printline(a)
	for i in range(w/2):
		next_step(a, b)
		printline(b)
		next_step(b, a)
		printline(a)

