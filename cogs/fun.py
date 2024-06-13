#!/usr/bin/env python3
"""
    Aman Bot
    Fun Commands
"""

import random, discord
from config import *
from discord.ext import commands, tasks
from itertools import cycle

#### Tarot Card Reading
from libraries.tarot import *

#### Paginator

bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def habibi(self, ctx):
        await ctx.send(random.choice(RANDOM_HALAL))

    @commands.command()
    async def kiss(self, ctx, arg=""):

        if arg == "" or arg == ctx.author.mention:
            await ctx.send("You can't kiss yourself you degenerate. Well go on don't be shy, choose someone")
        
        else:
            await ctx.send(embed=GifEmbedGenerator(
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

        await ctx.send(random.choice(RANDOM_FOOTER_MESSAGE))