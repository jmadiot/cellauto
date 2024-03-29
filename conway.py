# fichier pour une optimisation de l'automate du jeu de la vie

#AFFICHAGE CONSOLE D'UNE CELLULE
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
			for y in xrange(hm):
				for x in xrange(wm):
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


examples = [

("empty", [[0]]),

("cyclicbenzene", [[0,0,1,0,0,0,0,1,0,0],[1,1,0,1,1,1,1,0,1,1],[0,0,1,0,0,0,0,1,0,0]]),

("glider", [[0,0,1],[1,0,1],[0,1,1]]),

("launcher",
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
),

("toad", [[0,0,0,1,0,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),

("jardindeden",
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
 [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
 [0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
 [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0],
 [1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
),

("circus", [[0,0,0,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,1,0,1,0],[0,0,0,0,0]]),

("lightweight ship", [[1,0,0,1,0],[0,0,0,0,1],[1,0,0,0,1],[0,1,1,1,1]]),

("pulsar", [[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1]]),
 
]










