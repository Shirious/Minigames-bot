from flask import Flask
import discord
import asyncio
from discord.ext import commands
import tictactoe2
import random
import os
#now for the flask
app = Flask(__name__)
#flask events
@app.route("/")
def  robot() :
	  
	bot = commands.Bot(description = 'Mini Games BoT' , command_prefix = '<<')
#########
	#non bot functions :
	def replacenums(s) :
		dic = {
		'1' : ':one:','2':':two:','3':':three:','4':':four:','5':':five:','6':':six:','7':':seven:','8':':eight:','9':':nine:' , 'X':':x:','O':':o:'
		}#'a': ':regional_indicator_a:', 'p2': '  ', 'c': ':regional_indicator_c:', 'p1': '  ', 'e': ':regional_indicator_e:', 'd': ':regional_indicator_d:', 'g': ':regional_indicator_g:', 'f': ':regional_indicator_f:', 'i': ':regional_indicator_i:', 'h': ':regional_indicator_h:', 'k': ':regional_indicator_k:', 'j': ':regional_indicator_j:', 'l': ':regional_indicator_l:', 'b': ':regional_indicator_b:'}
		dicc = ['1','2','3','4','5','6','7','8','9','X','O']#,'p1','a','b','c','d','e','f','p2','g','h','i','j','k','l']
		for i in range(len(dicc)) :
			s = s.replace(dicc[i],dic[dicc[i]])
		return s

#########
	@bot.event
	async def on_ready() :
		print('Ready to Rock ...')
	
	@bot.command(pass_context = True )
	async def ping(pass_context = True) :
		"""I say Pong , BTW I produce sparcles also ^_^"""
		await bot.say(":sparkles:Pong")

	@bot.command()
	async def invite() :
		'''Shoot this command to conduct battles on ur Server'''
		s = 'To conduct Mini Games in your server , Click following link :\nhttps://discordapp.com/api/oauth2/authorize?client_id=321134463675400192&scope=bot&permissions=0'
		await bot.say(':+1:\n'+str(s))

	@bot.command()
	async def servers(pass_context = True):
		"""Counts and lists the amount of servers this bot is in."""
		server_amount = 0
		servers = []
		for server in bot.servers:
			servers.append(server.name)
			server_amount += 1
		await bot.say("I am in **%s** servers!```%s ```" % (server_amount,"\n".join(servers)))

	@bot.command(pass_context = True)
	async def rps(ctx,plyr) :
		'''Lets Play Rock Paper Scissors'''
		rules = 'The further game will occur in bot DM and playground !\nAs soon as u see Game x of y on the playground , you enter \'R\'/\'P\'/\'S\' your option in Bot DM !\nThe result will be in playground !\nHave Fun ^_^!!!'
		botg = False
		plyr = (ctx.message.content).replace('<<rps ','')
		plyr = plyr + ' 1'
		plyr = plyr.split()
		plyrid = str(plyr[0]).replace('<@','').replace('>','')
		if plyrid == '321134463675400192' :
			botg = True
			msg = await bot.say('Lets play !')
		else :
			xx = await bot.say('{} are u ready to Play ? \ntype \'yes\' to confirm !!!'.format(plyr[0]))
			msg = await bot.wait_for_message()
			chh = str(ctx.message.content).lower()
			print(chh)
		while str(msg.author.id) != str(plyrid) or chh != 'yes':
			msg = await bot.wait_for_message(content = 'yes')
		n = int(plyr[1])
		if n >= 15 : n = 15
		await bot.say('Game On!')
		i = 1 ; p1win ,p2win = 0 , 0
		await bot.say(rules)
		while i <= n :
			choices = ['r','p','s']
			await bot.say('***Rock Paper Scissors***')
			if botg == False :
				await bot.send_message(ctx.message.author,'Game {0} of {1} :'.format(i,n))
				ch1 = await bot.wait_for_message(author = ctx.message.author)
				while str(ch1.content).lower() not in choices: 
					bot.send_message(ch1.author,'Again {}'.format(ch1.author.display_name))
					ch1 = await bot.wait_for_message(author = ch1.author)
			if botg == False :
				await bot.send_message(msg.author ,'Game {0} of {1} :'.format(i,n))
				ch2 = await bot.wait_for_message(author = msg.author)
				while str(ch2.content).lower() not in choices :
					bot.send_message(ch2.author,'Again {}'.format(ch2.author.display_name))
					ch2 = await bot.wait_for_message(author = ch2.author)
					ch = (ch2.content).lower()
			else :
				ch = random.choice(choices)		
				cc = (ch1.content).lower()
			wins = {'r':'p','p':'s','s':'r'}
			symbol = {'p':':hand_splayed:','r':':fist:','s':':v:'}
			await bot.say('{0} X {1}'.format(symbol[cc],symbol[ch]))
			if ch == wins[cc] : 
				p2win +=1
			elif cc == wins[ch] : 
				p1win +=1
			i+=1
			await bot.say('Score is :\n\'{0} {1}\' **:** \'{2} {3}\''.format(ctx.message.author.display_name,str(p1win),msg.author.display_name,str(p2win)))
			if p1win > p2win : 
				await bot.say(':boom:**{}** wins!'.format(ctx.message.author.display_name))
				await bot.send_message(ctx.message.author , ':sparkles:Congo! you win !!!!')
				await bot.send_message(msg.author , 'Good Game \nSadly you Lose , Better Luck Next time !!!!')
			elif p2win > p1win : 
				if botg == False :
					await bot.send_message(msg.author , ':sparkles:Congo! you win !!!!')
					await bot.send_message(ctx.message.author , 'Good Game \nSadly you Lose , Better Luck Next time !!!!')
					await bot.say(':boom:**{}** wins!'.format(msg.author.display_name))
			elif p2win == p1win :
				await bot.say('tis a draw !')
			
			await bot.say('XXXGame OverXXX')
			
			
	@bot.command(pass_context = True)
	async def G20questions(ctx) :
		'''Lets Play 20 questions !'''
		await bot.say('Player one is **\'{}\'** \nThink of some word in bot DM'.format(ctx.message.author.display_name))
		await bot.send_message(ctx.message.author ,'Tell the word u would like to get **Guessed!**')
		wrd = await bot.wait_for_message(author = ctx.message.author)
		word = (wrd.content).lower()
		bot.delete_message(ctx.message)
		print(word)
		await bot.say('Who wants to play !\nType \'__P2__\' to play with {}'.format(ctx.message.author.display_name))
		plyr = await bot.wait_for_message(content = 'P2')
		while plyr.author == ctx.message.author :
			await bot.say('Not you !')
			plyr = await bot.wait_for_message(content = 'P2')
		await bot.say('Player 2 is **\'{}\'**:\n*Ready to play!*'.format(plyr.author.display_name))
		await bot.say('{} ,Start asking the questions !'.format(plyr.author.display_name))
		player = 'lose'
		for i in range(20) :
			bb = await bot.say('Question {} :'.format(str(i+1)))
			ques = await bot.wait_for_message(author = plyr.author)
			s = (ques.content).lower()
			if word in s  :
				player = 'win'
				await bot.say(':sparkles:You Win ,{}'.format(plyr.author.display_name))
				break
			bc = await bot.say('{} ,Answer \'Yes\' or \'No\''.format(ctx.message.author.display_name))
		if player == 'lose' :
			await bot.say('You lose ,{0}\n the word is {1}'.format(plyr.author.display_name,word))				
		await bot.say('XXXGame OverXXX')
		
	@bot.command(pass_context = True)	
	async def tictactoe(ctx,plyr) :
		sym = ['X','O'] 
		await bot.say('Player 1 is **{}**:'.format(ctx.message.author.display_name))
		await bot.say('What symbol would you like to choose \'X\' or \'O\' ?')
		sym1 = await bot.wait_for_message(author = ctx.message.author)
		while (sym1.content).upper() not in sym :
			await bot.say('Choose \'X\' or \'O\' !!!')
			sym1 = await bot.wait_for_message(author = ctx.message.author)
		sym1 = (sym1.content).upper()
		sym.remove(sym1)
		plyr1 = tictactoe2.player(str(sym1),ctx.message.author.display_name)
		botg = False
		mssg = str(ctx.message.content)
		plyr = mssg.replace('<<tictactoe ','')
		plyr = plyr.split()
		plyrid = str(plyr[0]).replace('<@','').replace('>','')
		if plyrid == '321134463675400192' :
			botg = True
			msg = await bot.say('Lets play !')
		else :
			await bot.say('{} are u ready to Play ? \ntype \'yes\' to confirm !!!'.format(plyr))
			msg = await bot.wait_for_message()
			while str(msg.author.id) != str(plyrid) or (msg.content).lower() != 'yes':
				msg = await bot.wait_for_message()
		
		await bot.say('Player 2 is **{0}**:\n{0} you get an \'{1}\'\n*Ready to play!*'.format(msg.author.display_name,sym[0]))
		plyr2 = tictactoe2.player(str(sym[0]),msg.author.display_name)
		brrd = tictactoe2.board()
		new = str(brrd.drawbrd(plyr1,plyr2))
		new = replacenums(new)
		old = await bot.say(new)
		while brrd.left != [] :
			xx = await bot.say('{}\'s move :\n'.format(plyr1.name))
			mv = await bot.wait_for_message(author = ctx.message.author)
			while str(mv.content) not in brrd.left :
				xx = await bot.say('Play valid move :\n'.format(plyr1.name))
				mv = await bot.wait_for_message(author = ctx.message.author)
				await bot.delete_message(mv)
				await bot.delete_message(xx)
			plyr1.move(str(mv.content),brrd)
			await bot.delete_message(mv)
			await bot.delete_message(xx)
			new = str(brrd.drawbrd(plyr1,plyr2))
			new = replacenums(new)
			await bot.delete_message(old)
			old = await bot.say(new)
			if plyr1.is_win() :
				await bot.say(':sparkles:Winner is {}'.format(plyr1.name))
				return 
			if brrd.left == [] :
				await bot.say('Its a draw !!!')
				break
			xx = await bot.say('{}\'s move :\n'.format(plyr2.name))
			if botg == True :
				mv = tictactoe2.play(plyr1,brrd)
				mv = await bot.say(mv)
			else :
				mv = await bot.wait_for_message(author = msg.author)
				while str(mv.content) not in brrd.left :
					xx = await bot.say('Play valid move :\n'.format(plyr2.name))
					mv = await bot.wait_for_message(author = msg.author)
					await bot.delete_message(mv)
					await bot.delete_message(xx)
				plyr2.move(str(mv.content),brrd)
				await bot.delete_message(mv)
				await bot.delete_message(xx)
				new = str(brrd.drawbrd(plyr1,plyr2))
				new = replacenums(new)
				await bot.delete_message(old)
				old = await bot.say(new)
				if plyr2.is_win() :
					await bot.say(':sparkles:Winner is {}'.format(plyr2.name))
					return 
			
	bot.run('token')
	return "exited"      #needed 

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
