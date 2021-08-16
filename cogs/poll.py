import discord
from discord.ext import commands
from cogs import text

class poll(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.group(name='poll')
  @commands.has_permissions(manage_messages=True)
  async def poll(self,ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send(f"Run `!poll help` (replace ! with prefix) for poll help")

  @poll.command()
  async def YesOrNo(self,ctx, question, description="A Yes/No question"):
    embed=discord.Embed(title=f"{question}", description=f'{description} - by {ctx.author.mention}', color=0x04ff00)
    embed.add_field(name="Yes", value=":green_circle:", inline=True)
    embed.add_field(name="No", value=":red_circle:", inline=True)
    embed.set_footer(text="React with the corresponding emoji.")
    message = await ctx.send(embed=embed)
    await message.add_reaction('🟢')
    await message.add_reaction('🔴')

  @poll.command()
  async def MCQ(self,ctx, question, optionsString, description='An MCQ Question.'):
    '''
    Creates an embed with question and the options. Usage: !poll MCQ <question here in double quotes> <options seperated by '/'> <optional description>
    '''
    options = [x for x in optionsString.split('/')]
    if 0 < len(options) <= 9:
      embed=discord.Embed(title=f"{question}", description=f"{description}  - by {ctx.author.mention}", color=0x04ff00)
      emojiCheck = 0
      for option in options:
        emoji = text.listOfEmojis[emojiCheck]
        embed.add_field(name=f"{emoji}  {option}", value="-------------------------", inline=True)
        emojiCheck = emojiCheck + 1
      embed.set_footer(text="React with the corresponding emoji's to vote.")
      message = await ctx.send(embed=embed)
      reactionCheck = 0
      while reactionCheck < emojiCheck:
        await message.add_reaction(text.listOfEmojis[reactionCheck])
        reactionCheck = reactionCheck + 1
    else:
      await ctx.send('Send between 0 and 11 options, or I will explode and kill you.')

  @poll.command()
  async def help(self,ctx):
    embed = discord.Embed(title="!poll Usage and Help", description="This command creates an embed that helps get users' opinions about a subject.", color=0x04ff00)
    embed.add_field(name='Yes or No question', value='''
    Usage: ```!poll YesOrNo "Question_Here" "Optional_Description_Here" ```
    Example: ```!poll YesOrNo "Do you like pizza" "I hate everybody who doesn't"```
    ''', inline=False)
    embed.add_field(name='MCQ\'s', value='''Upto 26 options.
    Usage: ```!poll MCQ "Question_Here" "Options_Here_Seperated_by_Forward_slashes(/)" "Optional_Description_Here"```
    Example: ```!poll MCQ "What food do you like?" "Pizza/Pasta/Burgers" "Go choose your favourite food, my friends!"```
    ''', inline=False)
    embed.add_field(name='**NOTE**', value='''**THE DESCRIPTION IS OPTIONAL.**
    Example with description: ```!poll YesOrNo "Are you alive?" "Please answer truthfully"```
    Example without description: ```!poll YesOrNo "Are you alive?" ```
    ''')
    embed.set_footer(text="By TheLegendBeacon")
    await ctx.send(embed=embed)


def setup(bot):
     bot.add_cog(poll(bot))