import discord
from discord.ext import commands
import pandas as pandas
import datetime
import os
import requests
import json
from dotenv import load_dotenv
from discord.utils import get

#Load TOKEN
load_dotenv()
token=os.getenv('BOT_TOKEN')

#Prefix
client = commands.Bot(command_prefix='--')

#Approved roles to make few changes
approved_roles=['admin','mesa']

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

#Create proyect command
@client.command(name='new_proyect')
async def create_proyect(context, args):
    user=context.message.author
    if any(role.name in approved_roles for role in user.roles):
        if any(args in role.name for role in context.guild.roles):
            await context.message.channel.send('El proyecto '+args+' ya existe en el servidor')
            return
        perms=discord.Permissions(send_messages=True, read_messages=True, embed_links=True, external_emojis=True, 
            read_message_history=True, speak=True, use_external_emojis=True, use_voice_activation=True, view_channel=True, change_nickname=True,
            attach_files=True, add_reactions=True,mention_everyone=True, connect=True, stream=True)
        await context.message.channel.send('Creando nuevo rol con nombre: '+args+' con permisos: '+str(perms))
        await context.guild.create_role(name=args,permissions=perms)
        await context.message.channel.send('Creando nuevo canal para el rol: '+args)
        await make_channel(context,args)
        await context.message.channel.send('Canal creado exitosamente')
    else:
        await context.message.channel.send('No eres administrador del servidor, no puedes crear nuevos proyectos')

async def make_channel(context,name):
    guild=context.guild
    admin=get(guild.roles,name=approved_roles[0]) #mesa en caso de usar el server de la OE
    rol=get(guild.roles,name=name)
    overwrites={
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        admin: discord.PermissionOverwrite(read_messages=True),
        rol: discord.PermissionOverwrite(read_messages=True),
    }
    await guild.create_text_channel(name,overwrites=overwrites)

#Test command
@client.command(name='test')
async def test(ctx, arg):
    await ctx.send(arg)

#Inspire command
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.command(name='inspire')
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)

#Run client
client.run(token)
    