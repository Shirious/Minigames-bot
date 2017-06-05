import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(description = 'Mini Games BoT' , command_prefix = '<<')

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
	'''Shoot this command to conduct battles on ur Server'''
	s = 'To conduct Pokemon Battles in your server , Click following link :\nhttps://discordapp.com/api/oauth2/authorize?client_id=321134463675400192&scope=bot&permissions=0'
	await bot.say(':+1:\n'+str(s))


	
bot.run('token')
