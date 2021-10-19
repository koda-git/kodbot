import discord
import os
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='?')
bot.remove_command('help')
#bot.load_extension('cogs.math') #Imports com.py inside cogs folder 
# "We haven't learned about that yet "


@bot.command(aliases=['help'])
async def commands(ctx):
  await ctx.send("Here's the list of commands \n >>> ping: pong! \nadd: adds two integers given \npick: picks between two things\nroll: rolls between 1 and given integer "  #Help template
  )

@bot.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
#check ping?!?!


@bot.command()
async def roll(ctx, arg): #no touch
  await ctx.send(random.randint(1,int(arg)))


  

@bot.command()
async def add(ctx, left: int, right: int):        # adds two integers (?add arg arg)
    await ctx.send(left + right)

@bot.command()
async def pick(ctx, first: str, second: str):
  r = random.randint(1,2) #python moment
  if r ==1:
    await ctx.send(first)  # done
  else:
    await ctx.send(second)
  
# is fixed <33333333333333333333333help33333333333333
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ['It is certain.',
               'It is decidedly so.',
               'Without a doubt.',
               'Yes - definitely.',
               'You may rely on it.',
               'As I see it, yes.',
               'Most likely.',
               'Outlook good.',
               'Yes.',
               'Signs point to yes.',
               'Reply hazy, try again.',
               'Ask again later.',
               'Better not tell you now.',
               'Cannot predict now.',
               'Concentrate and ask again.',
               "Don't count on it.",
               'My reply is no.',
               'My sources say no.',
               'Outlook not so good.',
               'Very doubtful.']
  await ctx.send(f'{random.choice(responses)}')

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def secret(ctx):  

  r = random.randint(1,4)
  if r==1 :
    await ctx.send(file=discord.File('./images/squid.jpg'))
  else : 
    await ctx.send("Sorry you don't deserve to know")




@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="Click here!!", url="https://kodev.xyz", description="My website is here lol",color=discord.Color.blue(), 
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730675910130270229/899890276267589652/Shime_pixel.png")
    embed.set_footer(text="This is the footer, I don't know what to say here. Shime is gay?")


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



bot.run(os.getenv('token'))
