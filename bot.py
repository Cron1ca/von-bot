import discord
from discord import client
from discord.ext import commands, tasks
import json
import os
import random




# Intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="v.", intents = intents)
bot.time = random.randint(10, 15)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"yo bitch"))
    play_m.start()


@tasks.loop(minutes=bot.time)
async def play_m():
    bot.time = random.randint(10, 15)
    channel = bot.get_channel(878423065149726764)
    await channel.connect()



bot.run(os.environ["TOKEN"])