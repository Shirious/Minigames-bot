import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(description = 'Mini Games BoT' , command_prefix = '<<')
##########
rules = 'The further game will occur in bot DM and playground !\nAs soon as u see Rock Paper Scissors on the playground , you enter \'R\'/\'P\'/\'S\' your option in Bot DM !\nThe result will be in playground !\nHave Fun ^_^!!!'

###########
@bot.event
async def on_ready() :
	print('Ready to Rock ...')
	
@bot.command(pass_context = True , description = 'Pong!')
async def ping() :
	"""I say Pong , BTW I produce sparcles also ^_^"""
	await bot.say(":sparkles:Pong")

@bot.command()
async def servers():
    """Counts and lists the amount of servers this bot is in."""
    server_amount = 0
    servers = []
    for server in bot.servers:
        servers.append(server.name)
        server_amount += 1
    await bot.say("I am in **%s** servers!```%s ```" % (server_amount,"\n".join(servers)))

@bot.command(pass_context = True)
async def invite() :
	"""Invite me !!!(O^O)"""
	s = 'To conduct Pokemon Battles in your server , Click following link :\nhttps://discordapp.com/api/oauth2/authorize?client_id=321134463675400192&scope=bot&permissions=0'
	await bot.say(':+1:\n'+str(s))
	
@bot.command(pass_context = True)
async def rps(ctx,n=1) :
	"""Lets play Rock Paper Scissors"""
	await bot.say('Player 1 is **{}**:\nType \'__P2__\' to play!'.format(ctx.message.author.display_name))
	msg = await bot.wait_for_message(content = 'P2')
	while msg.author == ctx.message.author :
		await bot.say('Not you !')
		msg = await bot.wait_for_message(content = 'P2')
	await bot.say('Player 2 is **{}**:\n*Ready to play!*'.format(msg.author.display_name))
	i = 1 ; p1win ,p2win = 0 , 0
	await bot.send_message(msg.author , rules)
	await bot.send_message(ctx.message.author , rules)
	while i <= n :
		await bot.send_message(msg.author ,'Game {0} of {1} Enter R/P/S :'.format(i,n))
		await bot.send_message(ctx.message.author ,'Game {0} of {1} Enter R/P/S:'.format(i,n))
		await bot.say('***Rock Paper Scissors***')
		ch1 = await bot.wait_for_message(author = ctx.message.author)
		ch2 = await bot.wait_for_message(author = msg.author)
		while ch1.author != ctx.message.author :
			ch1 = await bot.wait_for_message(author = ctx.message.author)
		while ch2.author != msg.author :
			ch2 = await bot.wait_for_message(author = msg.author)
		cc = (ch1.content).lower()
		ch = (ch2.content).lower()
		wins = {'r':'p','p':'s','s':'r'}
		symbol = {'p':':hand_splayed:','r':':fist:','s':':v:'}
		if len(cc) == 1 and len(ch) == 1 :
			await bot.say('{0} X {1}'.format(symbol[cc],symbol[ch]))
			if ch == wins[cc] : 
				await bot.say(':sparkles:**{}** wins!'.format(msg.author.display_name))
				p2win +=1
			elif cc == wins[ch] : 
				await bot.say(':boom:**{}** wins!'.format(ctx.message.author.display_name))
				p1win +=1
			elif cc == ch :
				await bot.say('tis a draw !')
			else :
				await bot.say('/tableflip')
		else :
			await bot.say('Play fair again!')
		i+=1
	if p1win > p2win : 
		await bot.say(':boom:**{}** wins!'.format(ctx.message.author.display_name))
		await bot.send_message(ctx.message.author , ':sparkles:Congo! you win !!!!')
	elif p2win > p1win : 
		await bot.say(':boom:**{}** wins!'.format(msg.author.display_name))
		await bot.send_message(msg.author , ':sparkles:Congo! you win !!!!')
	else : await bot.say('tis a draw !')

	
bot.run('token')
