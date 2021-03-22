import discord
import traceback
import sys
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.Cog.listener()
    async def on_command_error(self, context, error):
        #Activador cuando se registra un error al trabajar con comandos
        if hasattr(context.command,'on_error'):
            return
        
        cog=context.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        
        error=getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            await context.message.channel.send('Ese comando no está registrado, usa el comando --help')

        if isinstance(error, commands.DisabledCommand):
            await context.message.channel.send('Este comando fue deshabilitado')

        if isinstance(error, commands.MissingRequiredArgument):
            await context.message.channel.send('Se espera un argumento, la sintaxis del comando se encuentra en --help')
        
        if isinstance(error, commands.BadArgument):
            await context.message.channel.send('El argumento no tiene el formato esperado, la sintaxis del comando se encuentra en --help')
        
        if isinstance(error, commands.BotMissingPermissions):
            await context.message.channel.send('El bot no cuenta con los permisos para realizar la acción')
        
        if isinstance(error, commands.BotMissingRole):
            await context.message.channel.send('El bot no cuenta con el rol')
        
        if isinstance(error, commands.CommandRegistrationError):
            await context.message.channel.send('Ya existe un comando con ese nombre')
        
        if isinstance(error, commands.MemberNotFound):
            await context.message.channel.send('No se encontró al usuario')

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))