from automaton import bidim

import random

def rules(v):
	c = v(0,0)
	if c == 0:
		nv = v(-1, 0) + v(1, 0)
		nv += v(0, 1) + v(0, -1)
		if nv:
			if not random.randint(0,4*4/nv):
				return 1
			else:
				return 0
		else:
			return 0		
	elif c==7:
		return 7
	else:
		return c+1

def str_cell(i):
	return (" .-+*******")[i]+" "

if __name__ == '__main__':
	a = bidim(rules, 50, 40, str_cell = str_cell)
	a.setcell(22,20,7)
	#a.setcell(12,13,1)
	#a.setcell(12,14,1)
	#a.setcell(11,14,1)
	#a.setcell(10,13,1)

	for i in xrange(100):
		a.display()
		a.step()





