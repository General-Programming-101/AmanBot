
"""
    Gacha Commands!!

"""


import sys, asyncio, functools, itertools, math, random, os, discord, aiohttp, io, json, pickle, string, random
from config import *
from dotenv import load_dotenv, find_dotenv
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from itertools import cycle

from os.path import exists

bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

###### CONFIGURATION FUNCTIONS

def returnPlayerProfile(server, author): 
    data = None

    try:
        f = open(f"servers/{server}/{author}.txt")

        data = f.readlines()

    except FileNotFoundError:
        with open(f"servers/{server}/{author}.txt", "w") as f:
            f.write("Nothing to see here!")
            f.close()

        with open(f"servers/{server}/{author}.txt", "r") as f:
            data = f.readlines()
    
    print(data)

    output = []

    [output.append(("**{}.** {}").format(i, name)) for i, name in enumerate(data)]

    embed = discord.Embed(
        title = f"{author}'s Harem",
        description = "".join(output)
    )

    # [embed.add_field(name=str(i), value=name, inline=False) for i, name in enumerate(data)]

    return embed

class Gacha(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["profile"])
    async def prof(self, ctx):

        self.server = ctx.message.guild.id ### Set the server ID

        ##### First, check if the server is registered in the text file

        if not os.path.exists("servers/{}".format(ctx.message.guild.id)):
            os.makedirs("servers/{}".format(ctx.message.guild.id))

        await ctx.send(embed=returnPlayerProfile(ctx.message.guild.id, ctx.author))
            
        #     print("Already exists!") #### if self.server = True
        #     print(self.server)

        # except FileNotFoundError:
        #     print("Couldn't find it!")

        #     if not os.path.exists("servers/{}".format(ctx.message.guild.id)):
        #         os.makedirs("servers/{}".format(ctx.message.guild.id))

        #     with open(f"servers/{ctx.message.guild.id}/{ctx.author}.txt", "w") as f:
        #         f.write("Testing!")
        #         f.close()
            
        #     self.server = True

        # else:
        #     print("Already exists!")
