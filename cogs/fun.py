from discord.ext import commands
import random

class MainCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    

  @commands.command()
  async def rollin(self, ctx, arg): #no touch
      await ctx.send(random.randint(1,int(arg)))


  @commands.command()
  async def pick(ctx, first: str, second: str):
   r = random.randint(1,2) #python moment
   if r ==1:
    await ctx.send(first)  # done
   else:
    await ctx.send(second)




  @commands.command()
  async def secret(self, ctx):  

   r = random.randint(1,4)
   if r==1 :
    await ctx.send(file=discord.File('./images/squid.jpg'))
   else : 
    await ctx.send("Sorry you don't deserve to know")



  @commands.command()
  @bot.command(aliases=['8ball'])
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
    bot.add_cog(MainCommands(bot))







