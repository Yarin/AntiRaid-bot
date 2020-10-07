import discord
from discord.ext import commands

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role("Management", "admin", "administrator", "Meow", "*")
    async def ban(self, ctx, member_id):
        member = self.bot.get_user(int(member_id))
        await ctx.guild.ban(member, reason=f"Banned by AntiRaid, command executed by {ctx.message.author.name}")
        embed=discord.Embed(title="Banned User", description=f"<@{member.id}> has been banned by <@{ctx.message.author.id}>", color=0x1bee65)
        embed.set_author(name="AntiRaider ban command", icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="AntiRaider | Bot by xYarin#2280")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ModCommands(bot))