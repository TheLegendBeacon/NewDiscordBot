from database import get_all_prefixes, set_prefix, delete_prefix
from discord.ext import commands
from discord import Intents, Member
import jishaku
from dotenv import load_dotenv
from os import getenv, path

class MyBot(commands.Bot):
    def __init__(self, dev_ids, cogs, intents, **options):
        self.cog_paths = cogs
        self.devs = dev_ids
        commands.Bot.__init__(self, command_prefix=self.get_prefix, intents=intents, **options)
    
    async def get_prefix(self, message):
        return self.prefixes[message.guild.id]

    async def on_ready(self):

        print("on")

        for cog in self.cog_paths:
            self.load_extension(cog)
        
        self.prefixes = get_all_prefixes()

        for guild in self.guilds:
            if guild.id not in self.prefixes.keys():
                set_prefix(guild.id, '!')
                self.prefixes[guild.id] = '!'

        
    async def on_guild_join(self, guild):
        set_prefix(guild.id, '!')
        self.prefixes[guild.id] = '!'
    
    async def on_guild_leave(self, guild):
        delete_prefix(guild.id, '!')
        del self.prefixes[guild.id]
    
    async def on_message(self, message):
        if message.content == '-prefix':
            await message.channel.send(f"This server's prefix: `{self.prefixes[message.guild.id]}`")
    
        await self.process_commands(message)
    
client = MyBot([627132213875441687], ['jishaku', 'cogs.admin', 'cogs.games', 'cogs.misc', 'cogs.poll'], Intents.default())

# Essential Commands

@client.command()
async def shutdown(ctx):
    if ctx.author.id in client.devs:
        await ctx.send("Shutting down...")
        await client.close()
    else:
        await ctx.send("No")

@client.command()
async def reload(ctx, *args):
    if ctx.author.id in client.devs:
        await ctx.send("Please wait...")

        if bool(args) is False:
            for cog in client.cog_paths:
                client.reload_extension(cog)
            await ctx.send("Reloaded all cogs.")

        elif bool(args) is True:
            for arg in args:
                if arg not in client.cog_paths:
                    await ctx.send(f"{arg} not found.")
                    return
                    
            for arg in args:
                client.reload_extension(arg)
                await ctx.send(f"Reloaded {arg}")

    else:
        await ctx.send("No")
        
@client.group()
async def dev_access(ctx):
    pass

@dev_access.command()
async def give(ctx, *, user: Member):
    if ctx.author.id in client.devs:
        client.devs.append(user.id)
    else:
        await ctx.send("No")

@dev_access.command()
async def remove(ctx, *, user: Member):
    if ctx.author.id in client.devs:
        client.devs.remove(user.id)
    else:
        await ctx.send("No")

@client.command()
async def addcog(ctx, cogpath):
    print('.'.join(list(cogpath.replace('.', '/')).append('.py')))
    if path.exists('.'.join(list(cogpath.replace('.', '/')).append('.py'))):
        client.add_cog(cogpath)
        client.load_extension(cogpath)
        client.cog_paths.append(cogpath)
        await ctx.send(f"Added {cogpath}")
    else:
        await ctx.send("No")

@client.command()
async def removecog(ctx, cog):
    if cog in client.cog_paths:
        client.unload_extension(cog)
        client.remove_cog(cog)
        client.cog_paths.remove(cog)
        await ctx.send(f"Removed {cog}")

@client.command()
async def listcogs(ctx):
    x = '\n'.join(ctx.cog_paths)
    print(f"```{x}```")

load_dotenv()
token = getenv("DISCORD-TOKEN")
client.run(token)