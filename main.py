#!/usr/bin/env python3
"""
    Aman Bot
"""

import sys, os, discord
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'cogs')))
# print(sys.path)  # To verify the path has been added
    
##### Configuration and Cogs
from config import *

from cogs.admin import *
from cogs.fun import *
from cogs.gacha import *


from dotenv import load_dotenv, find_dotenv

bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

load_dotenv("token.env")

TOKEN = os.getenv("TOKEN")
ids = set()

@bot.event
async def on_ready():

    await bot.add_cog(Admin(bot))
    await bot.add_cog(Fun(bot))
    await bot.add_cog(Music(bot))
    await bot.add_cog(Gacha(bot))


    print(START_UP)

@bot.event
async def on_message(message):
    print(f"{message.guild}/{message.channel}/{message.author.name}> Message: {message.content}")
    await bot.process_commands(message)

"""
    Bot Run
"""

@bot.command()
@commands.has_permissions(kick_members=True)
async def quit(ctx):
    sys.exit()

bot.run(TOKEN)
