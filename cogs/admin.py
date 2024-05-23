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

bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

class Admin(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot    

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send("Cogs working")
