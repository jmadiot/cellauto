# automates generiques a deux (ou trois) dimensions

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

class bidim:
	
	def __init__(self, rules, w=10, h=10, default=0, disp=None, str_cell=None):
		self.disp = bool(disp) and disp or self.display
		self.str_cell = bool(str_cell) and str_cell or default_str_cell
		self.w = w
		self.h = h
		self.cells = range(h)
		for y in xrange(h):
			self.cells[y]=range(w)
			for x in xrange(w):
				self.cells[y][x] = default
		self.rules = rules
	
	def step(self):
		next = copy_matrix(self.cells)
		for y in xrange(self.h):
			for x in xrange(self.w):
				next[y][x] = self.rules(lambda dx,dy : self.cells[(y+dy)%self.h][(x+dx)%self.w])
		self.cells = next
	
	def setcell(self, x, y, status):
		self.cells[y][x] = status
	
	def display(self):
		for line in self.cells:
			print "".join([self.str_cell(x) for x in line])
		print
		for i in xrange(1000000):
			i^i%(i+1)


class tridim:
	
	def __init__(self, rules, w=10, h=10, p=10, default=0, disp=None, str_cell=None):
		self.disp = bool(disp) and disp or self.display
		self.str_cell = bool(str_cell) and str_cell or default_str_cell
		self.w = w
		self.h = h
		self.cells = range(p)
		for z in range(p):
			self.cells[z] = range(h)
			for y in xrange(h):
				self.cells[z][y]=range(w)
				for x in xrange(w):
					self.cells[z][y][x] = default
		self.rules = rules
	
	def step(self):
		next = copy_matrix(self.cells)
		for z in xrange(self.p):
			for y in xrange(self.h):
				for x in xrange(self.w):
					next[z][y][x] = self.rules(lambda dx,dy,dz : self.cells[(z+dz)%self.p][(y+dy)%self.h][(x+dx)%self.w])
		self.cells = next
	
	def setcell(self, x, y, z, status):
		self.cells[z][y][x] = status
	
	def display(self):
		for line in self.cells:
			print "".join([self.str_cell(x) for x in line])
		print
		for i in xrange(1000000):
			i^i%(i+1)




















