# ========================= IMPORTS ============================ #

import discord
from discord.ext import commands, tasks

import os
from decouple import config

# ========================= BOT CREATION ============================ #

bot = commands.Bot(command_prefix='play ', intents=discord.Intents.all())

# ========================= LOAD EXTENSIONS ============================ #

async def load_cogs(bot):
    for filename in os.listdir("Scripts"):
        if filename.endswith(".py"):
            await bot.load_extension(f"Scripts.{filename[:-3]}")
@bot.event
async def on_ready():
    await load_cogs(bot)

    print(bot.application.name, "iniciado com sucesso!")

# ========================= BOT EXECUTION ============================ #

TOKEN = config("TOKEN")
bot.run(TOKEN)

