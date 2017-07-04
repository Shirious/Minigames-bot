import random

class player :
	def __init__(self,sym,name) :
		self.name = name
		self.sym = sym
		self.mvs = []
		self.win = [['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]
	def move(self,mv,brd) :
		if mv not in brd.left :
			return False
		self.mvs.append(mv)
		(brd.left).remove(mv)
	def is_win(self) :
		w = self.win 
		mvs =  self.mvs
		for i in range(len(w)) :
			if (w[i][0] in mvs) and (w[i][1] in mvs) and (w[i][2] in mvs) :
				return True
		return False

class board :
	def __init__(self) :
		self.design = '( 1 | 2 | 3 )\n( 4 | 5 | 6 )\n( 7 | 8 | 9 )'
		self.left = ['1','2','3','4','5','6','7','8','9']
	def drawbrd(self,plyr1,plyr2) :
		brd = str(self.design)
		for i in range(len(plyr1.mvs)) :
			brd = brd.replace(plyr1.mvs[i],plyr1.sym)
		for i in range(len(plyr2.mvs)) :
			brd = brd.replace(plyr2.mvs[i],plyr2.sym)
		return brd

def play(plyr,brd) :
	w = [['1','5','9'],['3','5','7'],['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9']]
	mvs = plyr.mvs
	for i in range(len(w)) :
		k = w[i]
		a , b , c = w[i][0] , w[i][1] , w[i][2]
		if a in mvs and b in mvs :
			k.remove(a)
			k.remove(b)
			
			if c in brd.left :
				return c
		elif c in mvs and b in mvs :
			k.remove(c)
			k.remove(b)
			if a in brd.left :
				return a
		elif a in mvs and c in mvs :
			k.remove(a)
			k.remove(c)
			if b in brd.left :
				return b							
	return random.choice(brd.left)
def start() :
	plyr1 = player('X','Ahri')
	plyr2 = player('O','Fox')
	brrd = board()
	print(brrd.design)
	while brrd.left != [] :
		mv = str(input('{} move :\n'.format(plyr1.name)))
		while mv not in brrd.left :
			mv = str(input('{} move :\n'.format(plyr1.name)))
		plyr1.move(mv,brrd)
		if plyr1.is_win() :
			return plyr1.name
		if brrd.left == [] :
			break
		mv = play(plyr1,brrd)
		plyr2.move(mv,brrd)
		if plyr2.is_win() :
			return plyr2.name
		print(brrd.left)
		print(brrd.drawbrd(plyr1,plyr2))
	
#print('Winner is {}'.format(start()))
'''
'|----------------------------------|',
'|           M A N C A L A          |',
'|----------------------------------|',
'|[    ](l)(k)(j) || (i)(h)(g)[ <- ]|',
'|[    ]_L__K__J__||__I__H__G_[ p2 ]|',
'|[ p1 ] A  B  C  ||  D  E  F [    ]|',
'|[ -> ](a)(b)(c) || (d)(e)(f)[    ]|',
'|----------------------------------|',
'''
