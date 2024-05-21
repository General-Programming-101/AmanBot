#!/usr/bin/env python3
"""
    Aman Bot
"""

import sys, asyncio, functools, itertools, math, random, os, discord, aiohttp, io, json, pickle, string, random

from config import *
from cogs.admin import *
from dotenv import load_dotenv, find_dotenv
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from itertools import cycle

bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

load_dotenv("token.env")

TOKEN = os.getenv("TOKEN")
ids = set()

@bot.event
async def on_ready():

    await bot.add_cog(Admin(bot))

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
