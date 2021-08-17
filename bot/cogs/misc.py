import discord
from discord.ext import commands
from cogs import text


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # Sends a Direct Message to the member
    async def DM(self, ctx, user: discord.Member, *args):
        await user.send(''.join(args))

    @commands.command()
    # For testing purposes. Says Hi when executed
    async def hi(self,ctx):
        await ctx.send('hi')

    @commands.command()
    async def say(self,ctx, message):
        await ctx.channel.send(message)

    @commands.command()
    async def users(self,ctx):
        await ctx.channel.send(
            f"""Number of Members: {ctx.guild.member_count}""")

    @commands.command()
    async def hello(self,ctx):
        await ctx.channel.send(f"Hi, {ctx.author.mention}!")

    @commands.command()
    async def commands(self,ctx):
        await ctx.channel.send(text.Botcommands)

def setup(bot):
    bot.add_cog(misc(bot))