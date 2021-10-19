from discord.ext import commands
import random

class MainCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    

  @commands.command()
  async def roll(self, ctx, arg): #no touch
    await ctx.send(random.randint(1,int(arg)))


  

  @commands.command()
  async def add(self, ctx, left: int, right: int):        # adds two integers (?add arg arg)
    await ctx.send(left + right)

  

def setup(bot):
    bot.add_cog(MainCommands(bot))







