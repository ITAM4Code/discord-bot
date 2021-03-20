import discord
from discord.ext import commands
import pandas as pandas
import datetime
import os
from dotenv import load_dotenv
        
#Load TOKEN
load_dotenv()
token=os.getenv('BOT_TOKEN')

#Prefix
client = commands.Bot(command_prefix='--')


#Event when connected
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('ITAM4Code'))

#Version command
@client.command(name='version')
async def version(context):
    embed=discord.Embed(title="Current Version", description= "Version of Colmillo is 1.0", color=0x00ff00)
    embed.add_field(name="Version: ", value="v1.0.0",inline=False)
    embed.add_field(name="Date Released: ", value="18-03-2021", inline=False)
    embed.set_footer(text="Version")
    embed.set_author(name="ITAM4Code")
    await context.message.channel.send(embed=embed)

@client.command(name='assign')
async def assign_proyect(context,args):
    user=context.message.author
    #if(args in user.guild.roles.name)
    roles=user.guild.roles
    if args in roles
    await context.message.channel.send(user.guild.roles)
    #role=discord.utils.get(user.server.roles, name=args)
        
#Run client
client.run(token)
    