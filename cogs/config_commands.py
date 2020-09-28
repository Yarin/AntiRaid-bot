import discord
from discord.ext import commands
from cogs.configer import Config

class ConfigCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def getStartHour(self, ctx):
        config = Config("config", str(ctx.guild.id))
        await ctx.send(f"Start hour is {config.getStartHour()}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def getEndHour(self, ctx):
        config = Config("config", str(ctx.guild.id))
        await ctx.send(f"End hour is {config.getEndHour()}")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def getChannels(self, ctx):
        config = Config("config", str(ctx.guild.id))
        await ctx.send(f"Channels are {config.getChannels()}")

def setup(bot):
    bot.add_cog(ConfigCommands(bot))