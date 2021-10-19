
import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='?')
#bot.remove_command('help')
bot.load_extension('cogs.math') #Imports math.py inside cogs folder 
bot.load_extension('cogs.fun')  #Imports fun.py inside cogs folder


@bot.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  print("Bot init complete")
  print("-------------------------------------------")
    
@bot.event
async def on_message(message):
  await bot.process_commands(message) 

  if message.author == bot.user:
    return

  #if message.content.startswith('hello'):
    #await message.channel.send('Henlo :D')

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
