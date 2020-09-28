import discord
from discord.ext import commands
from cogs.configer import Config

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    def get_channel_ids(self):
        channels = []
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                channels.append(channel.id)
        print(f"Channel id's = {channels}")
        return channels


    @commands.command(aliases = ['ss'])
    @commands.has_permissions(administrator=True)
    async def setslowmode(self, ctx, seconds : int):
        serverId = ctx.guild.id
        config = Config("config", str(serverId))
        config.setSeconds(seconds)
        embed=discord.Embed(title=f"Set Slowmode to {seconds} seconds", description=f"Slowmode seconds has been changed to {seconds} seconds", color=0x27ca1c)
        embed.set_author(name=f"Requested by {ctx.message.author.name}", icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Bot by xYarin#2880 (yeah yeah I take credit stfu)")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Setup(bot))
        