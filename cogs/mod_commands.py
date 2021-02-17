import discord
from discord.ext import commands

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role("Management", "admin", "administrator", "Meow", "*")
    async def ban(self, ctx, member_id):
        member = await self.bot.fetch_user(int(member_id))
        await ctx.guild.ban(member, reason=f"Banned by AntiRaid, command executed by {ctx.message.author.name}")
        embed=discord.Embed(title="Banned User", description=f"<@{member.id}> has been banned by <@{ctx.message.author.id}>", color=0x1bee65)
        embed.set_author(name="AntiRaider ban command", icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="AntiRaider | Bot by xYarin#2280")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, num: int):  
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f"Cleared {num} messages")
        
            
        

    @commands.command()
    @commands.has_any_role("Management", "Meow")
    async def members(self, ctx, role_id : int):
        role = discord.utils.get(
             ctx.guild.roles, id=role_id
         )
        if role == None:
            await ctx.send("Can't find the role in this server")
            return
        members = ""
        for member in role.members:
            members += f'{member.mention}\n'
        await ctx.send(members)


def setup(bot):
    bot.add_cog(ModCommands(bot))