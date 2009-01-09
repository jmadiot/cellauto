#!/usr/bin/python

from Tkinter import *
import time

from conway import gameoflife
from recif import rules as reef_rules
from automaton import bidim


class commande(Tk):
	def __init__(self, rules):
		Tk.__init__(self)
		
		#definition d'objets
		self.geometry("%dx%d%+d%+d" % (300, 200, 20, 20))
		self.cadre = Frame(self)
		
		#definition d'un label
		self.texte1 = Label(self.cadre, text = 'Cote')
		self.texte2 = Label(self.cadre, text = 'Largeur')
		self.texte3 = Label(self.cadre, text = 'Hauteur')
		
		self.bind("<Return>", self.commande)
		
		self.mode = IntVar()
		self.mode.set(1)
		
		#Bouton OK
		self.button = Button(self.cadre, text = 'OK', command = self.commande)
		
		#definition d'Entries
		self.input1 = Entry(self.cadre)
		self.input2 = Entry(self.cadre)
		self.input3 = Entry(self.cadre)
		#Valeurs par defaut
		self.input1.insert(0, "15")
		self.input2.insert(0, "20")
		self.input3.insert(0, "20")
		
		#binding
		self.bind("<Return>", self.commande)
		
		#Affichage des objets sur la fenetre	
		self.cadre.pack(fill=X)
		
		Radiobutton(self.cadre, text="Conway's Game of Life", variable=self.mode, value=1, command=self.changemode).pack(anchor=W)
		Radiobutton(self.cadre, text="Coral reef",            variable=self.mode, value=2, command=self.changemode).pack(anchor=W)
		self.title("Commande")
		self.texte1.pack(anchor=W)
		self.input1.pack(anchor=W)
		self.texte2.pack(anchor=W)
		self.input2.pack(anchor=W)
		self.texte3.pack(anchor=W)
		self.input3.pack(anchor=W)
		self.button.pack(fill=None, anchor=W)
		
		self.busy=False		
		
		self.mainloop()
	
	def changemode(self):
		self.input1.delete(0, END)
		self.input2.delete(0, END)
		self.input3.delete(0, END)
		if self.mode.get() == 1:
			self.input1.insert(0, "15")
			self.input2.insert(0, "20")
			self.input3.insert(0, "20")
		else:
			self.input1.insert(0, "5")
			self.input2.insert(0, "70")
			self.input3.insert(0, "70")

			

	def commande(self,event=None):
		cote = int(self.input1.get())
		w = int(self.input2.get())
		h = int(self.input3.get())
		if not self.busy:
			#self.busy=True
			print(self.mode.get())
			if self.mode.get() == 1:
				self.fenetre = interface(conway=True, w=w, h=h, cote=cote)
			else:
				self.fenetre = interface(rules=reef_rules, w=w, h=h, cote=cote)
			
		

class interface(Tk):
	def __init__(self, rules=None, w=10, h=10, cote=15, conway=False, colors=None):
		self.mousedown = 0
		
		if conway:
			self.bidim = gameoflife(w=w, h=h)
			self.colors = ["black", "yellow"] 
		else:
			self.bidim = bidim(rules, w, h)
			self.colors = ['navy', 'green', 'green', 'yellow', 'orange', 'red', 'purple', 'black']
		
		#initialisation de la fenetre Tk
		Tk.__init__(self)

		#differents attributs de l objet interface
		#tels que la regle utilise la matrice le nombre de ligne,colonne , la largeur,et hauteur de la fenetre
		self.cote = cote
		self.grille = self.cote >= 3
		
		
		#fin attributs
		
		
		#definition d objets		
		self.cadre = Frame(self)
		#definition d une aire ou on peut dessiner
		self.canva = Canvas(self.cadre, width = self.cote*self.bidim.w, height = self.cote*self.bidim.h, bg = self.colors[0])
		#definition d un bouton
		self.bouton = Button(self.cadre, text = 'pas a pas', command = self.next)
		#definition d un label
		self.texte = Label(self.cadre, text = 'donnez un nombre puis appuyez sur entree')		
		#definition d une Entry
		self.input = Entry(self.cadre)	


		#Interactivite de l aire de dessin et de l Entry
		self.canva.bind("<ButtonPress-1>", self.mouseDown)
		self.canva.bind("<B1-Motion>", self.mouseB1Motion)
		self.bind("<Key-space>", self.startstop)

		self.anim=False
		self.input.bind("<Return>", self.animation)

		#Affichage des objets sur la fenetre
		self.cadre.grid(row=1,column=1)		self.canva.grid(row = 0, column = 0)
		self.bouton.grid(row = 1, column = 0)
		self.input.grid(row = 3, column = 0)
		self.texte.grid(row = 2, column = 0)

		#dessin du cadrillage bleu
		self.dessin_cadrillage()

		#remplissage selon le tableau par defaut
		self.remplir()
		
		#boucle d attente d evenements graphiques		
		self.mainloop()

	def startstop(self, event):
		self.anim=not self.anim
		if self.anim:
			self.animate()
	
	def animate(self):
		if(self.anim):
			self.next()
			self.after(10, self.animate)

	def dessin_cadrillage(self):
		if self.grille:
			for i in xrange(self.bidim.w):
				self.canva.create_line(i*self.cote, 0, i*self.cote, self.bidim.h*self.cote)
			for j in xrange(self.bidim.h):
				self.canva.create_line(0, j*self.cote, self.bidim.w*self.cote, j*self.cote)
	
	#creation des petites bulles de localisation des cellules		
	def cellule(self,i,j,couleur = ''):#i et j le i eme carre de la j eme colonne
		x = i*self.cote
		y = j*self.cote
		if couleur == '':
			couleur = self.colors[self.bidim.cells[j][i]]
		self.canva.create_rectangle(x,y,x+self.cote,y+self.cote,fill=couleur, width = int(self.grille))

	#fonction appelee lorsque l on clique sur la fenetre
	def mouseDown(self,event):
		i,j = event.x/self.cote, event.y/self.cote
		if i<self.bidim.w and j<self.bidim.h and i>=0 and j>=0:			self.laststate = (self.bidim.cells[j][i] + 1)%2			self.bidim.cells[j][i] = (self.bidim.cells[j][i] + 1)%3
			self.cellule(i, j)
		
	#pareil
	def mouseB1Motion(self,event):
		i, j = event.x/self.cote, event.y/self.cote
		if i<self.bidim.w and j<self.bidim.h and i>=0 and j>=0:			self.bidim.cells[j][i] = self.laststate
			self.cellule(i, j)
	
	#fonction servant a avancer d un pas (est aussi appelee par le bouton)
	def next(self):
		self.canva.delete(ALL)
		self.dessin_cadrillage()
		self.bidim.step()
		self.remplir()
	
	def remplir(self):
		j = 0
		while j < self.bidim.h:
			i = 0
			while i < self.bidim.w:
				a = self.bidim.cells[j][i]
				couleur = self.colors[a]
				if a == 0:
					pass
				else:
					self.cellule(i,j,couleur)
				i+=1
			j+=1

	#truc appele quand on appuie sur entree dans entry 
	def animation(self,event):
		a = int(self.input.get())
		i = 0
		while i < a:
			self.after(0)
			self.update_idletasks()
			self.next()
			i = i + 1

			
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

	
commande(rules)		

