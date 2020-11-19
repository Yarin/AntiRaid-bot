import discord
class Embed(discord.Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_footer(text="AntiRaider | Bot by xYarin#2280")