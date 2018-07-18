import discord
import youtube_dl
from discord.ext import commands


bundy = commands.Bot(command_prefix= '>')
bundy.remove_command('help')


@bundy.event
async def on_ready(): 
	await bundy.change_presence(game=discord.Game(name='Killing Weeaboos | >help', type=1))
	print("Bundy v1 ONLINE")

#-----BASIC COMMANDS-------#

@bundy.command()
async def vin():
	await bundy.say('anime is fucking gay')

@bundy.command()
async def say(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await bundy.say(output)

@bundy.command()
async def info():
        embed = discord.Embed(title="Info about Patton-Bot", description="Patton-Bot is a bot written by Patton#6790", color=0x164084)
        embed.add_field(name="Website", value="https://repo.vinlark.info/patton-bot", inline=False)
        embed.add_field(name="Github", value="https://github.com/VinLark/Patton-Bot", inline=False)
        await bundy.say(embed=embed)

@bundy.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author

	embed = discord.Embed(
		colour = discord.Colour.red()
	)
	embed.set_author(name='Help')
	embed.add_field(name='>clear', value='Clears a specific amount of messages', inline=False)
	embed.add_field(name='>info', value='Shows Info About Bundy', inline=False)
	embed.add_field(name='>say', value='Tell the Bot what to Say!', inline=False)
	embed.add_field(name='>shutdown', value='Shutdown Bundy', inline=False)
	embed.add_field(name='>vin', value='Eternal Virtue', inline=False)
	await bundy.say(embed=embed)

@bundy.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = []
	async for message in bundy.logs_from(channel, limit=int(amount)):
		messages.append(message)
	await bundy.delete_messages(messages)
	await bundy.say("Messages deleted.")

@bundy.command(pass_context=True)
async def shutdown(ctx):
	if ctx.message.author.id == "186703562053648384":
		await bundy.say("Shutting Down...")
		await bundy.logout()
	else:
		await bundy.say("You Do Not Have Permission To Do This")


#-----VOICE/MUSIC COMMANDS-----------#

@bundy.command(pass_context=True)
async def join(ctx):
	channel = ctx.message.author.voice.voice_channel
	await bundy.join_voice_channel(channel)

@bundy.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = bundy.voice_client_in(server)
	await voice_client.disconnect()


players = {}
@bundy.command(pass_context=True)
async def play(ctx, url):
	server = ctx.message.server
	voice_client = bundy.voice_client_in(server)
	player = await voice_client.create_ytdl_player(url)
	players[server.id] = player
	player.start()


bundy.run(:^)
