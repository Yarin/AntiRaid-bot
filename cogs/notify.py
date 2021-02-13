import discord
from discord.ext import commands
from cogs.configer import Config
from datetime import datetime, timedelta
import random

class Notifier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def isNew(self, member):
        """isNew check if a member is a new user in discord (created this week)

        Args:
            member (discord.Member): a member object to find his creation date

        Returns:
            bool: True if he's new, False otherwise
        """
        age = member.created_at
        now = datetime.now()
        now -= timedelta(days=7)
        if age >= now:
            return True
        return False
    
    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def user(self, ctx, id):
        """user check a creation date of a user

        Args:
            ctx (discord.ext.commands.Context): required arguement for a discord command
            id (str): user id, will be converted to string
        """
        member = self.bot.get_user(int(id))
        if member == None:
            await ctx.send("Could not find the user you are looking for.")
            return
        days = datetime.now() - member.created_at
        await ctx.send(f"User <@{member.id}>\nCreation date:\n{days.days if days.days > 0 else 0} days ago, {days.seconds // 3600} hours ago, {days.seconds // 60 % 60} minutes ago")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """on_member_join an event when a member joins a discord server the bot is in

        Args:
            member (discord.Member): the member object who joined the guild
        """
        print(f"member joined {member.guild.name}")
        server_id = member.guild.id
        config = Config('config', str(server_id))
        if config.isCheckingAge() and self.isNew(member):  
            days = datetime.now() - member.created_at
            print(f"[DETECTED] New User in {member.guild.name}")
            staff_chat = discord.utils.get(member.guild.text_channels, id=config.getNotifyChat())
            embed=discord.Embed(title="New User Notify", description=f"{member.mention} has joined", color=0xe11414)
            embed.add_field(name="Creation date:", value=f"{days.days if days.days > 0 else 0} days ago, {days.seconds // 3600} hours ago, {days.seconds // 60 % 60} minutes ago", inline=True)
            embed.set_author(name="AntiRaider Notifier", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="AntiRaider | Bot by xYarin#2280")
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

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def newMembers(self, ctx):
        """newMembers a command to check how many new members (created less than 1 week ago) are in the guild

        Args:
            ctx (discord.ext.commands.Context): required arguement for a discord command
        """
        members = ctx.guild.members
        newMembers = 0
        for member in members:
            if self.isNew(member):
                newMembers += 1
        await ctx.send(f"{newMembers} New Members in {ctx.guild.name}")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def giveaway(self, ctx):
        members = ctx.message.author.voice.channel.members
        await ctx.send(f"{random.choice(members).mention}")



def setup(bot):
    bot.add_cog(Notifier(bot))


        
