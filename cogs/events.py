import discord
from discord.ext import commands

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 816991044780294216:
            return
        if not message.attachments and message.author.id not in [185711883460935680, 325538130860048404, 213949213409673216, 692868292133650604, 139867121327800321, 140414127880404992]:
            #print("No image in message tho")
            await message.delete()
            return
        await message.add_reaction('👍')

def setup(bot):
    bot.add_cog(Event(bot))
    