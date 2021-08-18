import discord
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
  async def choose(self, ctx, args):
    await ctx.send(f"I Choose: {args[random.randrange(0, len(args))]}")

  @commands.command()
  async def toss(self, ctx, choice):
    if choice.strip().lower() == "heads" or choice.strip().lower() == "tails":
      userChoice = 0
      if choice.strip().lower() == "tails":
        userChoice = userChoice + 1
      result = random.randrange(0, 2)
      if result == 1:
        if userChoice == 1:
          await ctx.send("You won the toss.")
        else:
          await ctx.sen("You lost the toss.")
      elif result == 0:
        if userChoice == 0:
          await ctx.send("You won the toss.")
        else:
          await ctx.send("You lost the toss.")



def setup(bot):
    bot.add_cog(games(bot))