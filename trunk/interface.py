from Tkinter import *
from random import *


t = []
i = 0
while i < 48:
    t = t+[int(random()*10)%3]
    i=i+1




class autres(Tk):
    def __init__(self, cote=100, largeur = 800, hauteur = 600, t=[]):
        Tk.__init__(self)
        #definition des machins
        
        self.cote = cote
        print(self.cote)
        self.ligne = hauteur/self.cote
        self.colonne = largeur/self.cote
        self.jeu = t
        
        
        self.cadre = Frame(self)
        self.cadre.grid(row=1,column=1)

        
        self.canva = Canvas(self.cadre, width = largeur, height = hauteur, bg = "white")
        self.canva.grid(row = 0, column = 0)
        self.canva.bind("<ButtonPress-1>", self.mouseDown)
        self.bouton = Button(self.cadre, text = 'pas a pas', command = self.next)
        self.bouton.grid(row = 1, column = 0)
        self.dessin_cadrillage()
        self.cellule(2, 2, 'black')
        self.mainloop()

    def dessin_cadrillage(self):
#c est le cote d un carre, ligne le nombre de ligne et... 
        x,y = 0, 0
        i,j = 0, 0
        while i < self.colonne:
            j = 0
            y = 0        
            while j < self.ligne:
                self.canva.create_rectangle(x, y, x+self.cote, y+self.cote, fill='navy')
                y = y + self.cote
                j = j + 1
            x = x + self.cote
            i = i + 1
            
    def cellule(self,i,j,couleur):#i et j le i eme carre de la j eme colonne
        x = i*self.cote + self.cote/2
        y = j*self.cote + self.cote/2
        self.canva.create_oval(x-self.cote/3,y-self.cote/3,x+self.cote/3,y+self.cote/3,fill=couleur)

    def mouseDown(self,event):
        self.cellule(event.x/100, event.y/100, 'black')
        
    def next(self):
        self.dessin_cadrillage()
        #self.jeu = automate.next(self.jeu)
        self.remplir()
    
    def remplir(self):
        i = 0
        while i < len(self.jeu):
            a = self.jeu[i]
            if a == 0:#0 => cellule
                self.cellule(i%self.colonne,i/self.colonne,'red')
            elif a ==1:# 1 => squelette
                self.cellule(i%self.colonne,i/self.colonne,'yellow')
            else:#rien 
                pass
            i=i+1
        
        

                    
            
                
        
        
    
        
autres(t = t)
