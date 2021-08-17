from discord.ext import commands

class listeners(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.Cog.listener('on_message')
  async def on_message(self, message):
    lop = self.bot.prefixes
    if message.content.strip() == "-prefix":
      await message.channel.send(f"Your prefix is `{lop[message.guild.id]}`")

  @commands.Cog.listener('on_member_join')
  async def on_member_join(self, member):
    welcomeList = self.bot.welcome_messages
    guild = welcomeList[str(member.guild.id)]
    message = guild[0]
    channel_id = guild[1]
    message = message.replace("\ping", member.mention)
    channel = member.guild.get_channel(int(channel_id))
    await channel.send(message)

def setup(bot):
    bot.add_cog(listeners(bot)) 