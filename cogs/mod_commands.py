import discord
from discord.ext import commands

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member_id):
        member = self.bot.get_user(int(member_id))
        await member.ban(reason=f"Banned by AntiRaid, command executed by {ctx.message.author.name}")

def setup(bot):
    bot.add_cog(ModCommands(bot))