import discord
from discord.ext import commands
import pandas as pandas

client = commands.Bot(command_prefix='--')
token="TOKEN DEL CANAL"

#Connect discord server
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ITAM4Code'))

#Run client
#Token
client.run(token)