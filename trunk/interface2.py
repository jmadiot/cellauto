from Tkinter import *
from automaton import *
from automaton import bidim
import time


class commande(Tk):
	def __init__(self, rules):
		Tk.__init__(self)
		#definition d objets		
		self.cadre = Frame(self)
		#definition d un label
		self.texte1 = Label(self.cadre, text = 'cote d un carre')
		self.texte2 = Label(self.cadre, text = 'largeur')
		self.texte3 = Label(self.cadre, text = 'hauteur')

		#definition d Entries
		self.input1 = Entry(self.cadre)
		self.input2 = Entry(self.cadre)
		self.input3 = Entry(self.cadre)



		#binding
		self.input3.bind("<Return>", self.commande)

		#Affichage des objets sur la fenetre
		self.cadre.grid(row=0,column=0)
		self.input1.grid(row=2,column=0)
		self.texte2.grid(row=3,column=0)
		self.input2.grid(row=4,column=0)
		self.texte3.grid(row=5,column = 0)
		self.input3.grid(row=6,column=0)		
		self.texte1.grid(row=1,column=0)
		self.mainloop()

	def commande(self,event):
		self.cote = int(self.input1.get())
		self.w = int(self.input2.get())
		self.h = int(self.input3.get())
		self.fenetre = interface(rules, w = self.w, h = self.h, cote = self.cote)

		

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

	
commande(rules)		
#<<<<<<< .mine
#interface(rules = rules,w = 20)
#=======
#interface(rules = rules, w=20, h=10)
#>>>>>>> .r10
