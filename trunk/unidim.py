
#it est le nombre d iterations par defaut a 10
#regle est un entier < 256 qui donne la regle a utiliser(inutile si regle_bin)
#regle_bin est un texte (nombre binaire sur 8bits) qui donne la regle .(inutile si regle) 
#regle_bin sert seulement si l'on veut voir ce qui se passe  
#taille est la taille du jeu (sous forme de tore unidimensionnel) par defaut a 30

class unidim(object):
	def __init__(self, it = 10, regle_bin = '', taille = 30, regle = 0):
		if regle_bin == '':
			regle_bin = self.bin_8_bits(regle)
		self.init_jeu(taille)
		for i in range(it):
			self.next(self.jeu, regle_bin, taille)	  
	
	#prend un entier et renvoie un nombre binaire sur 8bits		
	def bin_8_bits(self,n):
		res = ''
		a = n
		while a:
			res = str(a%2) + res
			a=a/2
		while len(res) < 8:
			res = '0' + res
		return(res)
			
	def init_jeu(self, taille):
		self.jeu = ''
		for i in range(taille):
			if i ==taille/2:
				self.jeu = self.jeu + '1'
			else:
				self.jeu = self.jeu + '0'
		print "".join([int(x) and "O" or " " for x in self.jeu])

	def next(self,t,regle_bin,taille):
		self.jeu = ''
		for i in range(taille):
			a = int(t[(i-1)%taille]+t[i%taille]+t[(i+1)%taille],2) #t[-1:1] ne renvoie pas ce qu'on veut
			for k in range(8):
				if a == k:
					self.jeu = self.jeu + (regle_bin[(7-k)])
		print "".join([int(x) and "O" or " " for x in self.jeu])


if __name__ == "__main__":
	unidim(regle = 126, taille=50, it=30)	

