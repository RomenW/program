import os
from os.path import join,dirname
from dotenv import load_dotenv

import discord
from discord.ext import commands

dotenv_path=join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(os.environ.get("token"))
