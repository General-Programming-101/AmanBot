#!/usr/bin/env python3
"""
    Aman Bot
    Fun Commands
"""

import random, discord
from config import *
from discord.ext import commands, tasks
from itertools import cycle
import json
import requests

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
    async def hug(self, ctx, arg=""):

        if arg == "" or arg == ctx.author.mention:
            await ctx.send("You can't hug yourself you degenerate. Well go on don't be shy, choose someone")
        
        else:
            await ctx.send(embed=GifEmbedGenerator(
                None, 
                "{} hugs {}".format(ctx.author.mention, arg),
                    random.choice(HUG_GIFS),
                    random.choice(LOVE_MESSAGE)
                ))
            
    @commands.command()
    async def shoot(self, ctx, arg=""):

        if arg == ctx.author.mention:
            await ctx.send("You can't hug yourself you degenerate. Well go on don't be shy, choose someone")
        elif arg == "":
            await ctx.send(embed=GifEmbedGenerator(
                None, 
                "<@1242217847099359324> shoots {}".format(ctx.author.mention, arg),
                    random.choice(SHOOT_GIFS),
                    random.choice(HATE_MESSAGE)
                ))
        else:
            await ctx.send(embed=GifEmbedGenerator(
                None, 
                "{} shoots {}".format(ctx.author.mention, arg),
                    random.choice(SHOOT_GIFS),
                    random.choice(HATE_MESSAGE)
                ))
            
    @commands.command()
    async def tarot(self, ctx):

        output = []
        i = 1

        tarot = Tarot() #### Return a list, with lists

        contents = tarot.getHand()

        for k, v in contents.items():
            outputEmbed = TarotEmbed(k, v, i)

            await ctx.send(file=outputEmbed[0], embed=outputEmbed[1])
            i = i + 1

        await ctx.send(random.choice(RANDOM_FOOTER_MESSAGE))

    @commands.command()
    async def inspire(self, ctx):

        res = requests.get("https://zenquotes.io/api/random")

        if res.status_code == 200:
            res = res.json()[0] ### Here is where we receive the 
            await ctx.send(embed=EmbedAPIGenerator(f"***{res['q']}***", res["a"]))

        else:
            await ctx.send("There seems to be some error with the API, developers have been informed")
            channel = self.bot.get_channel(1253423525516021842)
            await channel.send("API Error!")