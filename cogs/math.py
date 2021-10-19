import discord
from discord.ext import commands
import random

class MathCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    

  @commands.command()
  async def roll(self, ctx, arg): #no touch
    await ctx.send(random.randint(1,int(arg)))

  @commands.command()
  async def add(self, ctx, left: int, right: int):        # adds two integers (?add arg arg)
    await ctx.send(left + right)

  @commands.command()
  async def subtract(self, ctx, left:int, right: int):  # subtracts two integers
    await ctx.send(left - right)

  @commands.command()
  async def multiply(self, ctx, left:int, right: int):  # multiplies two integers
    await ctx.send(left * right)

  @commands.command()
  async def divide(self, ctx, left:int, right:int):
    await ctx.send(left / right)

def setup(bot):
    bot.add_cog(MathCommands(bot))







