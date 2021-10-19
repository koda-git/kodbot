import discord
from discord.ext import commands
import random

class FunCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def pick(ctx, first: str, second: str):
   r = random.randint(1,2) #python moment
   if r ==1:
    await ctx.send(first)  # done
   else:
    await ctx.send(second)

  @commands.command()
  async def embed(self,ctx):
    embed=discord.Embed(title="Click here!!", url="https://kodev.xyz", description="My website is here lol",color=discord.Color.blue(), 
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730675910130270229/899890276267589652/Shime_pixel.png")
    embed.set_footer(text="qweqwe")


    embed.add_field(name="This is a field", value="Who? Who asked", inline=False) # Fields are set by how they are arranged in order / idk what inline does.
    embed.add_field(name="I am bored", value="yes", inline=True)
    
    await ctx.send(embed=embed)
  
  
  @commands.command()
  async def secret(self, ctx):  
    with open('./images/squid.jpg', 'rb') as f:
      picture = discord.File(f)
    await ctx.send(file=picture)
  

 
  @commands.command(aliases=['8ball'])
  async def _8ball(self, ctx, *, question):
  
  
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
  

def setup(bot):
    bot.add_cog(FunCommands(bot))







