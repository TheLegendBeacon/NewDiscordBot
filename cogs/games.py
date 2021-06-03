from discord.ext import commands
import random
from cogs import text
import asyncio


class games(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def fact(self,ctx):
      num = [1]
      for x in num:
          length = len(text.facts)
          randomInt = random.randrange(0, length, 1)
          fact = text.facts[randomInt]
          await ctx.channel.send(fact)

  @commands.command()
  async def riddle(self,ctx):
      num = [1]
      for x in num:
          length = len(text.riddles)
          randomInt = random.randrange(0, length, 1)
          riddle = text.riddles[randomInt]
          answer = text.riddleAnswers[randomInt]
          message = await ctx.send(riddle)
          await asyncio.sleep(5)
          await message.reply(f"Answer to this riddle: {answer}")

  @commands.command()
  async def tictactoe:
    


def setup(bot):
    bot.add_cog(games(bot))