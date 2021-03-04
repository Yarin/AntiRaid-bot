import discord
from discord.ext import commands

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 816991044780294216:
            return
        if not message.attachments:
            #print("No image in message tho")
            await message.delete()
            return
        await message.add_reaction('👍')

def setup(bot):
    bot.add_cog(Event(bot))
    