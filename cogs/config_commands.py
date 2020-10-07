import discord
from discord.ext import commands
from cogs.configer import Config

class ConfigCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def getStartHour(self, ctx):
        """getStartHour get the start hour from the config and send it in the chat

        Args:
            ctx (discord.ext.commands.Context): required argument for a discord command
        """
        config = Config("config", str(ctx.guild.id))
        await ctx.send(f"Start hour is {config.getStartHour()}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def getEndHour(self, ctx):
        """getEndHour get the end hour from config and send it in the chat

        Args:
            ctx (discord.ext.commands.Context): required arguement for a discord command

        """
        config = Config("config", str(ctx.guild.id))
        await ctx.send(f"End hour is {config.getEndHour()}")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def getChannels(self, ctx):
        """getChannels get the channel ID's from the config and send it in the chat

        Args:
            ctx (discord.ext.commands.Context): required arguement for a discord command

        """
        config = Config("config", str(ctx.guild.id))
        await ctx.send(f"Channels are {config.getChannels()}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setNotify(self, ctx, value):
        """setNotify set if you want to get notified about new discord users (look notify.py)

        Args:
            ctx (discord.ext.commands.Context): required arguement for a discord command
            value (bool): the value, must be True / False
        """
        config = Config("config", str(ctx.guild.id))
        value = str(value).capitalize()
        if value != "True" and value != "False":
            await ctx.send("Please enter a valid boolean (True / False)")
            return None
        elif value == "True":
            value = True
        elif value == "False":
            value = False
        config.setCheckingAge(value)
        await ctx.send(f"Changed the value to {config.isCheckingAge()}")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setNotifyChannel(self, ctx, channel : discord.TextChannel):
        """setNotifyChannel set the notify channel to notify a new user

        Args:
            ctx (discord.ext.commands.Context): required arguement for a discord command
            channel (discord.TextChannel): the desired text channel

        Returns:
            False: if no channel found
        """
        config = Config("config", str(ctx.guild.id))
        if discord.utils.get(ctx.guild.text_channels, id=channel.id) == None:
            await ctx.send("Please tag a channel that is in the server...")
            return False
        config.setNotifyChannel(channel.id)
        await ctx.send(f"Updated notify channel to <#{channel.id}>")
        

def setup(bot):
    bot.add_cog(ConfigCommands(bot))