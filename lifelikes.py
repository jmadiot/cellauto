#optimisation, generalisation et exemples pour les life-likes

#AFFICHAGE CONSOLE D'UNE CELLULE
def default_str_cell(i):
	if int(i):
		return "O"
	else:
		return " "

class lifelike:
	
	def __init__(self, w=10, h=10, born=[3], survive=[2,3], disp=None, motif=False):
		self.disp = bool(disp) and disp or self.display
		self.w = w
		self.h = h
		self.born=born
		self.survive=survive
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
				v = voisins[y][x]
				if v in self.born :
					self.cells[y][x]=1
				elif v in self.survive:
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

#EXEMPLES DE LIFE-LIKES AVEC LEURS REGLES

lifelikes_examples = [
("45678/3", "Coral"),
("34678/3678", "Day & Night"),
("12345/3", "Maze"),
("23/3", "Life"),
("/2", "Seeds"),
("/234", "Serviettes"),
("1357/1357", "Replicator"),
#("012345678/1", "Wolfram Fig. 7(e)"),
("012345678/3", "Flakes, life without death"),
#("012345678/378", "Wolfram Fig. 9(a)"),
#("01356/13456", "Wolfram Fig. 7(d)"),
#("018/018", "Wolfram Fig. 13(c)"),
#("0238/123567", "Wolfram Fig. 13(f)"),
#("03456/34", "Wolfram Fig. 7(g)"),
#("045/0578", "Wolfram Fig. 7(i)"),
#("0468/236", "Wolfram Figs. 7(a), 13(g)"),
#("1/1", "Gnarl"),
#("12456/0578", "Wolfram Fig. 7(h)"),
("125/36", "2x2"),
#("135/135", "Wolfram Fig. 13(h)"),
("1358/357", "Amoeba"),
("23/36", "HighLife"),
#("234/3", "Wolfram Figs. 9(b), 13(b)"),
("2345/45678", "Walled Cities"),
#("2346/367", "Wolfram Fig. 9(c)."),
("235678/3678", "Stains"),
("235678/378", "Coagulations"),
#("238/357", "Pseudo life"),
("245/368", "Move"),
#("27/257", "Wolfram Fig. 7(b)"),
#("34/34", "34 Life"),
("4567/345", "Assimilation"),
#("45678/137", "Wolfram Fig. 7(f)"),
("5/345", "Long life"),
("5678/35678", "Diamoeba")
]



