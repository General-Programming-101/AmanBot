#!/usr/bin/env python3
"""
    Aman Bot
"""

import sys, asyncio, functools, itertools, math, random, os, discord, aiohttp, io, json, pickle, string, random
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'cogs')))
# print(sys.path)  # To verify the path has been added
    
##### Configuration and Cogs
from config import *
from admin import Admin
from fun import Fun
from music import Music

from dotenv import load_dotenv, find_dotenv
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from itertools import cycle

##### Tarot Card Reading
# from import tarot

bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

load_dotenv("token.env")

TOKEN = os.getenv("TOKEN")
ids = set()

@bot.event
async def on_ready():

    await bot.add_cog(Admin(bot))
    await bot.add_cog(Fun(bot))
    await bot.add_cog(Music(bot))

    print(START_UP)

@bot.event
async def on_message(message):
    print(f"{message.guild}/{message.channel}/{message.author.name}> Message: {message.content}")

    await bot.process_commands(message)

"""
    Basic Commands
"""

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def habibi(ctx):
    await ctx.send(random.choice(RANDOM_HALAL))

"""
    Bot Run
"""

@bot.command()
@commands.has_permissions(kick_members=True)
async def quit(ctx):
    sys.exit()

bot.run(TOKEN)
