#!/usr/bin/env python3
"""
    Aman Bot
    Fun Commands
"""

import sys, asyncio, functools, itertools, math, random, os, discord, aiohttp, io, json, pickle, string, random
from config import *
from dotenv import load_dotenv, find_dotenv
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from itertools import cycle

#### Paginator
import button_paginator as pg
bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kiss(self, ctx, arg=""):

        if arg == "":
            await ctx.send("You can't kiss yourself, degenerate")
        
        else:
            embed = discord.Embed(
                title="{} kisses {}".format(ctx.author.mention, arg)
            )
            embed.set_image(random.choice(KISS_GIFS))
        await ctx.send("Cogs working")