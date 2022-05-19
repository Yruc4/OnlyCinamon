import discord
from discord.ext import commands
import music

cogs = [music]
  
client = commands.Bot(command_prefix='%', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTY5NDE3MjQzNTY3OTgwNTc0.Gr0TyT.HJDynXGLaypZV6aTyS2-tRbygQ-txlUkJcs78U")

