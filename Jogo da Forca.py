# Jogo da Forca Dlc 

import random

board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class jogo_forca :
		def __init__(self,palavra):
			self.palavra = palavra
			self.forca_encontra = []
			self.forca_erra = []

		def adivinhar (self,letra):
			if letra in self.palavra and letra  not in  self.forca_encontra   :
				self.forca_encontra.append(letra)
			elif letra not in self.palavra and letra not in self.forca_erra  :
				self.forca_erra.append(letra)
			else :
				return False
			return True


		def forca_over (self):
			return self.forca_ganha()  or (len(self.forca_erra) ==6 )

		def forca_ganha (self):
			if '_' not in self.esconder ():
				return True 
			return False


		def esconder (self) :
			rtn = ' '
			for letra  in self.palavra :
				if letra not in self.forca_encontra :
					rtn+= "_"
				else :
					rtn += letra
			return rtn

		def print_board (self) :

			print(board[len(self.forca_erra)])
			print('\n Palavra : ' +self.esconder())
			print('\n Letras erradas : ' ,)
			for letra in self.forca_erra :
				print(letra,)
			print()
			print('\n Letras Corretas . ' ,)
			for letra in self.forca_encontra :
				print(letra,)
			print()


def ler_palavra () :
		with open('palavras.txt','rt') as f :
			banco = f.readlines ()
		return banco[random.randint(0,len(banco))].strip()

def main() :

	game= jogo_forca (ler_palavra())
	
	while not game.forca_over () :
		game.print_board ()
		digite_letra = input ('\n Digite uma Letra :  ')
		game.adivinhar(digite_letra)

	game.print_board ()


	if game.forca_ganha () :
		print ('Você venceu !!!')
	else :
		print('Game Over , Você perde ')
		print(' A palavra era '+ game.palavra)

if __name__ =='__main__' :
	main ()
