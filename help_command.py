import discord
from discord.ext import commands
import pandas as pandas
import datetime
import os
import requests
import json
from dotenv import load_dotenv
from discord.utils import get


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    client = commands.Bot(command_prefix='--')
    #Group command help
    client.remove_command("help")  
    #@client.command(pass_context=True)
    
    #Help command
    @client.group(invoke_without_command=True)
    async def help(self,context):
        embed= discord.Embed(title="Help", description= "Use --help <command> for extended information on a command.",color=0x00ff00)
        embed.add_field(name= "Admin", value="new_proyect")
        embed.add_field(name= "All Users", value="version, test, inspire")
        embed.set_author(name="ITAM4Code")
        await context.channel.send(embed=embed)

    @help.command()
    async def new_proyect(self,context):
        embed= discord.Embed(title="Create Proyect", description= "Crea nuevos roles para un nuevo proyecto y su respectivo canal de texto",color=0x00ff00)
        embed.add_field(name="**Syntax**", value="--new_proyect [nombre_proyecto]")
        embed.add_field(name="Permissions", value="Admin")
        embed.set_author(name="ITAM4Code")
        await context.channel.send(embed=embed)

    @help.command()
    async def version(self,context):
        embed= discord.Embed(title="Version", description= "Escribe la versión actual del bot en formato Embed",color=0x00ff00)
        embed.add_field(name="**Syntax**", value="--version")
        embed.add_field(name="Permissions", value="All Users")
        embed.set_author(name="ITAM4Code")
        await context.channel.send(embed=embed)

    @help.command()
    async def test(self,context):
        embed= discord.Embed(title="test", description= "Contesta con el mensaje enviado",color=0x00ff00)
        embed.add_field(name="**Syntax**", value="--test [mensaje]")
        embed.add_field(name="Permissions", value="All Users")
        embed.set_author(name="ITAM4Code")
        await context.channel.send(embed=embed)

    @help.command()
    async def inspire(self,context):
        embed= discord.Embed(title="inspire", description= "Envia un mensaje aleatorio de https://zenquotes.io/api/random",color=0x00ff00)
        embed.add_field(name="**Syntax**", value="--inspire")
        embed.add_field(name="Permissions", value="All Users")
        embed.set_author(name="ITAM4Code")
        await context.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))