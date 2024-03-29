#!/usr/bin/python

from Tkinter import *
import time

from recif import rules as reef_rules

from conway import gameoflife, examples as conway_examples
from automaton import bidim

import lifelikes


#FENETRE DE COMMANDE
class commande(Tk):
	def __init__(self):
		Tk.__init__(self)
		
		#definition d'objets
		self.geometry("%dx%d%+d%+d" % (600, 500, 20, 20))
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
		
		#Conway
		self.conway = Frame(self)
		self.example = IntVar()
		self.example.set(0)
		
		self.examples=[]
		for i in xrange(len(conway_examples)):
			(text, _) = conway_examples[i]
			self.examples.append(
				Radiobutton(self.conway, text=text, variable=self.example,
				value=i))

		#Life-like
		self.lifelikeframe = Frame(self)
		self.lifelikevar = IntVar()
		self.lifelikevar.set(0)
		
		self.lifelikes=[]
		self.lifelikes.append(
			Radiobutton(self.lifelikeframe, text="Custom",
			variable=self.lifelikevar, value=0, command=self.lifelikechange))
		
		for i in xrange(len(lifelikes.lifelikes_examples)):
			(_, text) = lifelikes.lifelikes_examples[i]
			self.lifelikes.append(
				Radiobutton(self.lifelikeframe, text=text,
				variable=self.lifelikevar, value=i+1, command=self.lifelikechange))
		
		self.llcommand = Entry(self.lifelikeframe)
		self.llcommand.insert(0, "1/1")
		self.llcommand.config(state="disabled")
		Label(self.lifelikeframe, text = 'Exemples de life-likes').grid(sticky=NW)
		self.llcommand.grid(sticky=W)
		for radio in self.lifelikes:
			radio.grid(sticky=W)
		
		
		for radio in self.examples:
			radio.grid(sticky=W)
		
		#binding
		self.bind("<Return>", self.commande)
		
		#Affichage des objets sur la fenetre	
		group=Frame(self)
		group.grid(columnspan=2)
		Radiobutton(group, text="Conway's Game of Life", variable=self.mode, value=1, command=self.changemode).grid(sticky=W)#.pack(anchor=W)
		Radiobutton(group, text="Coral",                 variable=self.mode, value=2, command=self.changemode).grid(sticky=W)#.pack(anchor=W)
		Radiobutton(group, text="Life-like",             variable=self.mode, value=3, command=self.changemode).grid(sticky=W)#.pack(anchor=W)
		
		Label(self, text = 'Exemples de grilles').grid(column=1, row=2)
		
		self.cadre.grid(sticky=NW)#(fill=X)
		self.conway.grid(column=1, row=3)
		self.lifelikeframe.grid(column=2, row=0, rowspan=99)
		self.title("Commande")
		self.texte1.grid(row=2, column=0, sticky=W)#anchor=W)
		self.input1.grid(row=2, column=1, sticky=W)#anchor=W)
		self.texte2.grid(row=3, column=0, sticky=W)#anchor=W)
		self.input2.grid(row=3, column=1, sticky=W)#anchor=W)
		self.texte3.grid(row=4, column=0, sticky=W)#anchor=W)
		self.input3.grid(row=4, column=1, sticky=W)#anchor=W)
		self.button.grid(columnspan=2)
		self.changemode()
		
		self.busy=False		
		
		self.mainloop()
	
	#RADIO SUR LE CHOIX DU LIFE-LIKE
	def lifelikechange(self):
		if self.lifelikevar.get()==0 and self.mode.get() == 3:
			self.llcommand.config(state="normal")
		else:
			self.llcommand.config(state="normal")
			self.llcommand.delete(0, END)
			self.llcommand.insert(0, lifelikes.lifelikes_examples[self.lifelikevar.get()-1][0])
			self.llcommand.config(state="disabled")
	
	#RADIO SUR LE CHOIX DE L'AUTOMATE
	def changemode(self):
		self.input1.delete(0, END)
		self.input2.delete(0, END)
		self.input3.delete(0, END)
		self.lifelikechange()
		if self.mode.get() == 1:
			self.input1.insert(0, "5")
			self.input2.insert(0, "100")
			self.input3.insert(0, "50")
			for radio in self.examples:
				radio.config(state="normal")
			for radio in self.lifelikes:
				radio.config(state="disabled")
		elif self.mode.get() == 2:
			self.input1.insert(0, "5")
			self.input2.insert(0, "70")
			self.input3.insert(0, "70")
			for radio in self.examples:
				radio.config(state="disabled")
			for radio in self.lifelikes:
				radio.config(state="disabled")
		elif self.mode.get() == 3:
			self.input1.insert(0, "5")
			self.input2.insert(0, "70")
			self.input3.insert(0, "70")
			for radio in self.examples:
				radio.config(state="disabled")
			for radio in self.lifelikes:
				radio.config(state="normal")
		elif self.mode.get() == 4:
			self.input1.insert(0, "5")
			self.input2.insert(0, "100")
			self.input3.insert(0, "50")
			for radio in self.examples:
				radio.config(state="normal")
			for radio in self.lifelikes:
				radio.config(state="disabled")
	
	
		
	#LANCER UNE INTERFACE FENETREE
	def commande(self,event=None):
		cote = int(self.input1.get())
		w = int(self.input2.get())
		h = int(self.input3.get())
		if not self.busy:
			#self.busy=True
			if self.mode.get() == 1:
				motif=conway_examples[self.example.get()][1]
				self.fenetre = interface(conway=True, w=w, h=h, cote=cote, motif=motif)
			elif self.mode.get() == 2:
				self.fenetre = interface(rules=reef_rules, w=w, h=h, cote=cote)
			elif self.mode.get() == 3:
				num=self.lifelikevar.get()
				if num==0:
					command=self.llcommand.get()
				else:
					command=lifelikes.lifelikes_examples[num-1][0]
				born=[]
				survive=[]
				n=len(command)
				i=0
				while i<n and command[i]!='/':
					survive.append(int(command[i]))
					i+=1
				i+=1
				while i<n and command[i]!='/':
					born.append(int(command[i]))
					i+=1
				self.fenetre = interface(lifelike=True, w=w, h=h, cote=cote, born=born, survive=survive)
			elif self.mode.get() == 4:
				motif=conway_examples[self.example.get()][1]
				self.fenetre = interface(conway=True, w=w, h=h, cote=cote, motif=motif, highlife=True)
			
		
#INTERFACE FENETREE
class interface(Tk):
	def __init__(self, rules=None, w=10, h=10, cote=15, lifelike=False, conway=False, colors=None, motif=False, highlife=False, born=[2], survive=[]):
		self.mousedown = 0
		
		#INSTANCE D'AUTOMATE
		if lifelike:
			self.bidim = lifelikes.lifelike(w=w, h=h, born=born, survive=survive)
			self.colors = ["navy", "yellow"]
		elif conway and not highlife:
			self.bidim = gameoflife(w=w, h=h, motif=motif)
			self.colors = ["navy", "yellow"]
		elif highlife:
			self.bidim = various.highlife(w=w, h=h, motif=motif)
			self.colors = ["navy", "yellow"]
		else:
			self.bidim = bidim(rules, w, h)
			self.colors = ['navy', 'green', 'green', 'yellow', 'orange', 'red', 'purple', 'black']
		
		#initialisation de la fenetre Tk
		Tk.__init__(self)

		#attributs de l objet interface
		self.cote = cote
		self.grille = self.cote >= 3
		
		
		#definition d objets		
		self.cadre = Frame(self)
		self.canva = Canvas(self, width = self.cote*self.bidim.w, height = self.cote*self.bidim.h, bg = self.colors[0])
		#definition d un bouton
		self.bouton = Button(self, text = 'pas a pas', command = self.next)
		#definition d un label
		self.texte = Label(self, text = "Effectuer n etapes : ")
		#definition d une Entry
		self.input = Entry(self)	


		#Interactivite de l aire de dessin et de l Entry
		self.canva.bind("<ButtonPress-1>", self.mouseDown)
		self.canva.bind("<B1-Motion>", self.mouseB1Motion)
		self.bind("<Key-space>", self.startstop)
		self.bind("<Key-p>", self.printc)

		self.anim=False
		self.input.bind("<Return>", self.animation)

		#Affichage des objets sur la fenetre
		self.cadre.grid(row=1,columnspan=2)		self.canva.grid(row = 0, columnspan = 2)
		self.bouton.grid(row = 1, columnspan=2)
		self.input.grid(row = 2, column = 1, sticky=W)
		self.texte.grid(row = 2, column = 0, sticky=E)

		#dessin du cadrillage bleu
		self.dessin_cadrillage()

		#remplissage selon le tableau par defaut
		self.remplir()
		
		#boucle d attente d evenements graphiques		
		self.mainloop()
	
	def printc(self, _):
		print(self.bidim.cells)
	
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
		if i<self.bidim.w and j<self.bidim.h and i>=0 and j>=0:			self.laststate = int(not(bool(self.bidim.cells[j][i])))			self.bidim.cells[j][i] = self.laststate
			self.cellule(i, j)
		
	#pareil
	def mouseB1Motion(self,event):
		i, j = event.x/self.cote, event.y/self.cote
		if i<self.bidim.w and j<self.bidim.h and i>=0 and j>=0:			self.bidim.cells[j][i] = self.laststate
			self.cellule(i, j)
	
	#fonction servant a avancer d un pas (est aussi appelee par le bouton)
	def next(self):
		#print self.bidim.cells
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

	#appele quand on appuie sur entree dans entry 
	def animation(self,event):
		a = int(self.input.get())
		i = 0
		while i < a:
			self.after(0)
			self.update_idletasks()
			self.next()
			i = i + 1	
commande()

