import discord
from discord.ext import commands
from cogs.configer import Config
from datetime import datetime, timedelta

class Notifier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"member joined {member.guild.name}")
        server_id = member.guild.id
        config = Config('config', str(server_id))
        if config.isCheckingAge():
            age = member.created_at
            now = datetime.now()
            now -= timedelta(days=7)
            if age >= now:
                days = datetime.now() - age
                print(f"[DETECTED] New User in {member.guild.name}")
                staff_chat = discord.utils.get(member.guild.text_channels, id=config.getNotifyChat())
                embed=discord.Embed(title="New User Notify", description=f"<@{member.id}> has joined", color=0xe11414)
                embed.add_field(name="Creation date:", value=f"{days.days if days.days > 0 else 0} days ago, {days.seconds // 3600} hours ago, {days.seconds // 60 % 60} minutes ago", inline=True)
                embed.set_author(name="AntiRaider Notifier", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=member.avatar_url)
                await staff_chat.send(embed=embed)
                role = config.getRoleNotifierId()
                if role != 0:
                    if type(role) == list:
                        msg = ""
                        for r in role:
                            msg += f" <@&{r}> "
                        await staff_chat.send(msg)
                    else:
                        await staff_chat.send(f"<@&{role}>")
                else:
                    await staff_chat.send(member.guild.default_role)


def setup(bot):
    bot.add_cog(Notifier(bot))


        
