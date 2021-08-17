import discord
from discord.ext import commands
import database as db

class admin(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command(name='purge', alias=['delete'])
  @commands.has_permissions(manage_messages=True)
  async def deletemax(self, ctx, num=None):
    if num == None:
      await ctx.send("Please send a valid number between 1 and 100, or `max`.")
    elif num == "max":
      await ctx.channel.purge(limit=100)
    elif isinstance(num, int):
      if 1 <= num <= 100:
        await ctx.channel.purge(limit=num)
      else:
        await ctx.send("Please send a valid number between 1 and 100, or `max`.")

  @commands.command(name='kick')
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx, member: discord.Member, *, reason='chuck\'d'):
      try:
          await member.kick(reason=reason)
          await ctx.send(f'{member.mention} was kicked')
      except:
        await ctx.send('Error')

  @commands.command(name='ban')
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason='chuck\'d'):
      await member.ban(reason=reason)

  @commands.command(name='prefix', alias=['changeprefix'])
  @commands.has_permissions(administrator = True)
  async def prefix(self, ctx, prefix):
    prefix = str(prefix).strip()
    if len(prefix) <= 2:
      db.db_update_prefix(ctx.guild.id, prefix)
      await ctx.send(f"Your server's prefix has been set to {prefix}")
      self.bot.prefixes[ctx.guild.id] = prefix
    else:
      await ctx.send("Please send a valid prefix with maximum 2 charecters.")

  @commands.group(name="welcome_message", alias=['wmessage', 'Wmessage'])
  @commands.has_permissions(administrator=True)
  async def welcome_message(self, ctx):
    pass
  
  @welcome_message.command()
  async def set(self, ctx, message, channel):
    contentList = (str(message), channel.replace("<", "").replace("#", "").replace(">", ""))
    db.db_set_welcome_message(ctx.guild.id, contentList[0], contentList[1])
    self.bot.welcome_messages[ctx.guild.id] = contentList
    await ctx.send("Welcome message successfully set.")

  @welcome_message.command()
  async def remove(self, ctx):
    try:
      db.db_delete_welcome_message(ctx.guild.id)
      await ctx.send("Successfully deleted the message.")
      del self.bot.welcome_messages[ctx.guild.id]
    except db.DoesNotExist:
      await ctx.send("You do not have a welcome message.")



def setup(bot):
    bot.add_cog(admin(bot))