from discord.ext import commands
import random

class MainCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    

  @commands.command()
  async def rollin(self, ctx, arg): #no touch
      await ctx.send(random.randint(1,int(arg)))
  

def setup(bot):
    bot.add_cog(MainCommands(bot))







