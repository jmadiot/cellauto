from Tkinter import *
from automaton import *
from automaton import bidim
import time


class interface(Tk):
	def __init__(self, rules, w = 10, h = 10, cote=50):
		self.mousedown = 0
		
		self.bidim = bidim(rules, w=w, h=h)
		#initialisation de la fenetre Tk
		Tk.__init__(self)

		#differents attributs de l objet interface
		#tels que la regle utilise la matrice le nombre de ligne,colonne , la largeur,et hauteur de la fenetre
		self.cote = cote

		if self.cote < 3:
			self.width = 0
		else:
			self.width = 1

		#fin attributs
		
		
		#definition d objets		
		self.cadre = Frame(self)
		#definition d une aire ou on peut dessiner
		self.canva = Canvas(self.cadre, width = self.cote*self.bidim.w, height = self.cote*self.bidim.h, bg = "white")
		#definition d un bouton
		self.bouton = Button(self.cadre, text = 'pas a pas', command = self.next)
		#definition d un label
		self.texte = Label(self.cadre, text = 'donnez un nombre puis appuyez sur entree')		
		#definition d une Entry
		self.input = Entry(self.cadre)		


		#Interactivite de l aire de dessin et de l Entry
		self.canva.bind("<ButtonPress-1>", self.mouseDown)
		self.canva.bind("<B1-Motion>", self.mouseB1Motion)
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


	def dessin_cadrillage(self):
	#x,y coordonnees du rectangle (coin haut gauche)
	#i,j coordonnees dans la matrice
		x,y = 0, 0
		i,j = 0, 0
		while i < self.bidim.w:
			j = 0
			y = 0		
			while j < self.bidim.h:
				self.canva.create_rectangle(x, y, x+self.cote, y+self.cote, fill='navy', width = self.width)
				y = y + self.cote
				j = j + 1
			x = x + self.cote
			i = i + 1
	
	#creation des petites bulles de localisation des cellules		
	def cellule(self,i,j,couleur = ''):#i et j le i eme carre de la j eme colonne
		x = i*self.cote
		y = j*self.cote
		if couleur == '':
			if self.bidim.cells[j][i] == 0:
				couleur = 'navy'
			elif self.bidim.cells[j][i] == 1:
				couleur = 'yellow'
			elif self.bidim.cells[j][i] == 2:
				couleur = 'red'
			else: 
				pass
		self.canva.create_rectangle(x,y,x+self.cote,y+self.cote,fill=couleur, width = self.width)

	#fonction appelee lorsque l on clique sur la fenetre
	def mouseDown(self,event):
		i,j = event.x/self.cote, event.y/self.cote
		if i<self.bidim.w and j<self.bidim.h and i>=0 and j>=0:			self.laststate = (self.bidim.cells[j][i] + 1)%3			self.bidim.cells[j][i] = (self.bidim.cells[j][i] + 1)%3
			self.cellule(i, j)
		
	#pareil
	def mouseB1Motion(self,event):
		i, j = event.x/self.cote, event.y/self.cote
		if i<self.bidim.w and j<self.bidim.h and i>=0 and j>=0:			self.bidim.cells[j][i] = self.laststate
			self.cellule(i, j)
	

	#fonction servant a avancer d un pas (est aussi appelee par le bouton)
	def next(self):
		self.canva.delete(ALL)#acceleration de l interface.ecrire les cases les unes sur les autres le ralentissait 
		self.dessin_cadrillage()
		self.bidim.step()
		self.remplir()
	
	def remplir(self):
		j = 0
		while j < self.bidim.h:
			i = 0
			while i < self.bidim.w:
				a = self.bidim.cells[j][i]
				if a == 0:#0 => rien
					pass
				elif a ==1:# 1 => cellule
					self.cellule(i,j,'yellow')
				elif a==2:# 2 => squelette
					self.cellule(i,j,'red')
				else:#rien 
					pass
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

	
		
interface(rules = rules, w=20, h=10)
