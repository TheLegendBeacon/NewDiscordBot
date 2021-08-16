# Imports
import discord
from discord.ext import commands, tasks
import database as db
import jishaku
import os

prefixes = db.read_all_prefix()

def get_prefix(client, message):
  if client.prefixes:
    return client.prefixes[message.guild.id]
  else:
    if prefixes[message.guild.id]:
        return prefixes[message.guild.id]
    else:
        db.db_set_prefix(message.guild.id, "!")
        return "!"


# Some global vars
token = os.getenv("DISCORD-TOKEN")
my_id = os.getenv("MY-DISCORD-ID")
cogs = [
    'cogs.admin', 'cogs.poll', 'cogs.games', 'cogs.listeners', 'cogs.misc',
    'jishaku'
]

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=get_prefix, intents=intents)
client.prefixes = {}
client.welcome_messages = {}



@client.event
async def on_ready():
  print("on")
  for cog in cogs:
    client.load_extension(cog)
  client.welcome_messages = db.read_all_welcome_messages()
  client.prefixes = db.read_all_prefix()
  
@client.event
async def on_guild_join(guild):
    id = guild.id
    db.db_set_prefix(id, prefix="!")


@client.command()
async def reload(ctx, cog='cogs'):
    if ctx.author.id == int(my_id):
        for precog in cogs:
            await ctx.send(f'Reloaded {precog}')


@client.command()
async def clear(ctx):
    if ctx.author.id == int(my_id):
        os.system('clear')


@client.command()
async def shutdown(ctx):
  """Shuts down the bot. Only to be used with the owner's consent/permission."""
  if ctx.author.id == int(my_id):
    await ctx.send("Shutting down...")
    await client.close()
  else:
    print("Not enough powahh")

@tasks.loop(hours=2)
async def backup():
  db.backup()

client.run(token)
