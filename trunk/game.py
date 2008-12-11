


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



if __name__ == "__main__" and False :
	
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


from automaton import bidim

def rules(neig):
	c = 0
	c += neig(-1, 0) + neig(1, 0)
	c += neig(-1, 1) + neig(0, 1) + neig(1, 1)
	c += neig(-1, -1) + neig(0, -1) + neig(1, -1)
	if c == 3:
		return 1
	elif c == 2:
		return neig(0, 0)
	else:
		return 0


a = bidim(rules)
a.setcell(2,2,1)
a.setcell(2,3,1)
a.setcell(2,4,1)
a.setcell(1,4,1)
a.setcell(0,3,1)

a.display()
a.step()
a.display()
a.step()
a.display()
a.step()
a.display()
a.step()
a.display()
a.step()
a.display()
a.step()
a.display()
a.step()
a.display()
a.step()
a.display()
a.step()
a.display()
a.step()
a.display()














