import discord
from discord.ext import commands
import time
from datetime import datetime, timedelta
import os
import aioschedule as schedule
from cogs.configer import Config, getConfigs, get_channels
import asyncio

client = commands.Bot(command_prefix="a!")


configs = getConfigs()


def get_ctx_config(server_id):
    for config in configs:
        print(f"ITER ID {config.serverId}")
        print(f"SERVER ID {server_id}")
        if config.serverId == str(server_id):
            return configs.index(config)

@client.command()
@commands.has_permissions(administrator=True)
async def slowmode(ctx):
    server_id = ctx.guild.id
    config_index = get_ctx_config(server_id)
    await set_slowmode(config=configs[config_index])
    embed=discord.Embed(title="Slowmode Command", description="Slowmode started from now until end hour in config", color=0xca591c)
    embed.set_author(name=f"Requested by {ctx.message.author.name}", icon_url=ctx.message.author.avatar_url)
    embed.set_footer(text="Bot by xYarin#2880 (yeah yeah I take credit stfu)")
    await ctx.send(embed=embed)

@client.command()
async def time(ctx):
    time = datetime.now()
    time = time.strftime("%H:%M")
    await ctx.send(f"TIME NOW IN SERVER - {time}")
    await ctx.send(f"UTC TIME - {toUTC(time)}")

async def remove_slowmode(config):
    channels_utils = get_channels(client, config)
    for channel in channels_utils:
        await channel.edit(slowmode_delay = 0)
        print(f"Unslowmoded {channel.name}")

async def set_slowmode(config):
    channels_utils = get_channels(client, config)
    for channel in channels_utils:
        await channel.edit(slowmode_delay = config.getSeconds())
        print(f"Slowmoded {channel.name}")

def toUTC(hour):
    date_object = datetime.strptime(hour, "%H:%M")
    date_object -= timedelta(hours=3)
    return date_object.strftime("%H:%M")



@client.event
async def on_ready():
    print("Bot is ready")
    for config in configs:
        utc_startHour = toUTC(config.getStartHour())
        utc_endHour = toUTC(config.getEndHour())
        schedule.every().day.at(utc_startHour).do(set_slowmode, config)
        print(f"[START HOUR SET] Server {config.serverId} start hour set to {utc_startHour}")

    for config in configs:
        utc_startHour = toUTC(config.getStartHour())
        utc_endHour = toUTC(config.getEndHour())
        schedule.every().day.at(utc_endHour).do(remove_slowmode, config)
        print(f"[END HOUR SET] Server {config.serverId} start hour set to {utc_endHour}")
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)
    
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != "configer.py": 
        client.load_extension(f'cogs.{filename[:-3]}')
client.run(os.environ['ANTIRAID_TOKEN'])

