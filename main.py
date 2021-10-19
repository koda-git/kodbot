import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='?')
bot.remove_command('help')
bot.load_extension('cogs.math') #Imports com.py inside cogs folder 
# "We haven't learned about that yet "


@bot.command(aliases=['help'])
async def commands(ctx):
  await ctx.send("Here's the list of commands \n >>> ping: pong! \nadd: adds two integers given \npick: picks between two things\nroll: rolls between 1 and given integer "  #Help template
  )

@bot.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
#check ping?!?!



# is fixed <33333333333333333333333help33333333333333


@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)





@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="Click here!!", url="https://kodev.xyz", description="My website is here lol",color=discord.Color.blue(), 
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730675910130270229/899890276267589652/Shime_pixel.png")
    embed.set_footer(text="qweqwe")


    embed.add_field(name="This is a field", value="Who? Who asked", inline=False) # Fields are set by how they are arranged in order / idk what inline does.
    embed.add_field(name="I am bored", value="yes", inline=True)
    
    await ctx.send(embed=embed)
    

  

#bot.event
#async def on_reminder(channel_id, author_id, text):
    #channel = bot.get_channel(channel_id)
    
    #await channel.send("Hey, <@{0}>, remember to: {1}".format(author_id, text))

# Who added this? 


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  print("Bot initiation complete, if there's messages beyond this you've fucked up something")
  print("-------------------------------------------")
    
@bot.event
async def on_message(message):
  await bot.process_commands(message)

  if message.author == bot.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('Henlo :D')

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
