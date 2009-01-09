	#topologies can be :
# torus    -> specify the size of the automaton
# bounded  -> have to specify the behaviour for an inexistent cell, and the size
# infinite -> have to specify the radius of the rules

#for now, producing bidimensionnal automata only

def copy_matrix(a):
	c=a[:]
	for i in xrange(len(a)):
		c[i]=a[i][:]
	return c

def default_str_cell(i):
	if int(i):
		return "O"
	else:
		return " "

class gameoflife:
	
	def __init__(self, w=10, h=10, disp=None, motif=False):
		self.disp = bool(disp) and disp or self.display
		self.w = w
		self.h = h
		self.cells = range(h)
		for y in xrange(h):
			self.cells[y]=range(w)
			for x in xrange(w):
				self.cells[y][x] = 0
		if motif:
			wm=len(motif[0])
			hm=len(motif)
			print motif
			for y in xrange(hm):
				for x in xrange(wm):
					print "w=%d, wm=%d, x=%d" % (w,wm,x)
					print "h=%d, hm=%d, y=%d" % (h,hm,y)
					print motif[y][x]
					self.cells[h/2-hm/2+y][w/2-wm/2+x] = motif[y][x]
					
	
	def step(self):
		voisins = range(self.h)
		
		for y in xrange(self.h):
			voisins[y]=range(self.w)
			for x in xrange(self.w):
				voisins[y][x] = 0
		
		for y in xrange(self.h):
			for x in xrange(self.w):
				if bool(self.cells[y][x]):
					h=self.h
					w=self.w
					voisins[(y-1)%h][(x-1)%w]+=1
					voisins[(y-1)%h][ x     ]+=1
					voisins[(y-1)%h][(x+1)%w]+=1
					voisins[(y+1)%h][(x-1)%w]+=1
					voisins[(y+1)%h][ x     ]+=1
					voisins[(y+1)%h][(x+1)%w]+=1
					voisins[ y     ][(x-1)%w]+=1
					voisins[ y     ][(x+1)%w]+=1
		
		for y in xrange(self.h):
			for x in xrange(self.w):
				if voisins[y][x] >= 4:
					self.cells[y][x]=0
				elif voisins[y][x] == 3:
					self.cells[y][x]=1
				elif voisins[y][x] == 2:
					pass
				else:
					self.cells[y][x]=0
		
	def setcell(self, x, y, status):
		self.cells[y][x] = status
	
	def display(self):
		for line in self.cells:
			print "".join([self.str_cell(x) for x in line])
		print
		for i in xrange(1000000):
			i^i%(i+1)



cyclicbenzene = [[0,0,1,0,0,0,0,1,0,0],[1,1,0,1,1,1,1,0,1,1],[0,0,1,0,0,0,0,1,0,0]]

glider=[[0,0,1],[1,0,1],[0,1,1]]

launcher=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

examples = [
	([[0]], "Nothing"),
	(cyclicbenzene, "cyclicbenzene"),
	(glider, "glider"),
	(launcher, "launcher")
]
















