#!/usr/bin/env python3
"""
    Aman Bot
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

class Admin(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot    

bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

class Admin(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot    

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send("Cogs working")

    @commands.command()
    async def help(self, ctx):
        embeds = []

        # embeds.append(EmbedGenerator())

        allEmbeds = ReturnEmbed()

        for v in allEmbeds.values():
            embeds.append(v)

        paginator = pg.Paginator(bot, embeds, ctx)
        # paginator.default_pagination()
        paginator.add_button("prev", emoji = "◀")
        paginator.add_button("goto")
        paginator.add_button("next", emoji = "▶")
        await paginator.start()
        
