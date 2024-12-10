import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
BOT_API_KEY = os.environ.get("BOT_API_KEY")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='&', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in.')
    await bot.load_extension("cogs.kogcog")
   
bot.run(BOT_API_KEY)

