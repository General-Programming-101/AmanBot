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

#### Tarot Card Reading
from libraries.tarot import *

#### Paginator
import button_paginator as pg
bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kiss(self, ctx, arg=""):

        if arg == "" or arg == ctx.author.mention:
            await ctx.send("You can't kiss yourself you degenerate. Well go on don't be shy, choose someone")
        
        else:
            await ctx.send(embed=gifEmbedGenerator(
                None, 
                "{} kisses {}".format(ctx.author.mention, arg),
                random.choice(KISS_GIFS),
                random.choice(LOVE_MESSAGE)
                ))
            
    @commands.command()
    async def tarot(self, ctx):

        output = []
        i = 1

        tarot = Tarot() #### Return a list, with lists

        contents = tarot.getHand()
        print(contents)

        for k, v in contents.items():
            outputEmbed = TarotEmbed(k, v, i)

            await ctx.send(file=outputEmbed[0], embed=outputEmbed[1])
            i = i + 1

        print(output)

        randomFooterMessage = [
            "***Is this your destiny?***",
            "I wonder what this means?",
            "Not happy with your reading? Run it again!",
            "I think your future is doomed"
        ]

        await ctx.send(random.choice(randomFooterMessage))