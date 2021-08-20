import discord
from discord.ext import commands
import json
import os




# Intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="v.", intents = intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"yo bitch"))



bot.run(os.environ["TOKEN"])