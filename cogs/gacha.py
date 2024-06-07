
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

##### Gacha Config
from gachagacha.banners import *
from gachagacha.wishing import *

from os.path import exists

bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

###### CONFIGURATION FUNCTIONS

def returnPlayerProfile(server, author, authorPic): 
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

    embed.set_thumbnail(url=authorPic)

    return embed

def workWithPlayer(banner, server, author): #### No output
    data = None

    try: #### Try to see if the file exists
        f = open(f"servers/{server}/{author}data.txt")

        # print("Trying to read something!")
        # data = "".join(f.readlines()).split(".")

        # print(data)
        # pity = data[1].split(":")[1]
        # # print(pity)

        # data.pop()

        # data.append("Pity:" + str(int(pity) + 1))

        # with open(f"servers/{server}/{author}data.txt", "w") as f:
        #     f.write(".".join(data))

        #     f.close()

    except FileNotFoundError:
        with open(f"servers/{server}/{author}data.txt", "w") as f:
            content = []

            content.append(startPlayer[0] + ":1")
            content.append(startPlayer[1] + ":1")
            content.append(startPlayer[2] + ":false")
            content.append(startPlayer[3] + ":false")

            f.write(".".join(content))
            f.close()

    ##### NOTE IMPORTANT USER DATA

    ###### Deal with the player data
    
    with open(f"servers/{server}/{author}data.txt", "r") as f:

        contents = f.readlines()

        details = contents[0].split(".")

        pity = int(details[0].split(":")[1])
        fourStar = int(details[1].split(":")[1])
        guarantee = details[2].split(":")[1]
        eventguarantee = details[3].split(":")[1]

        # print(pity)
        # print(fourStar)
        # print(guarantee)

        if pity == 90: ## Guarantee a 5 star
            eventguarantee = "false"
            guarantee = "true"
            
            fiftyFifty = random.choice([0, 1])

            if fiftyFifty == 0 and eventguarantee != "true":
                eventguarantee = "true"


    ##### Wish First

    output = decideWish(banner, fourStar, guarantee, eventguarantee)

    print("This here lies the output output" + output)
    outputOutput = output.split("/")

    print(outputOutput)

    if len(outputOutput[0]) == 3: ### If it's a 3 star
        pity = pity + 1
        fourStar = fourStar + 1
    
    elif outputOutput == banner:
        eventguarantee = "false"
    
    elif outputOutput[1] != banner and len(outputOutput[0]) == 5: ### 5 star not event
        eventguarantee = "true"
        pity = 0
    
    elif len(outputOutput[0]) == 4: ### If 5 star
        fourStar = 0 

    contents = []

    contents.append("Pity:" + str(pity))
    contents.append("Count4Star:" + str(fourStar))
    contents.append("Guarantee:" + guarantee)
    contents.append("EventGuarantee:" + eventguarantee)

    with open(f"servers/{server}/{author}data.txt", "w") as f:
        f.write(".".join(contents))

        f.close()

    # return [pity, fourStar, guarantee, eventguarantee]

    return outputWish(output)

class Gacha(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open("gachagacha/currentBanner.txt", "r") as f:
            self.banner = f.readlines()
            f.close()

    @commands.command(aliases=["profile"])
    async def prof(self, ctx):

        self.server = ctx.message.guild.id ### Set the server ID

        ##### First, check if the server is registered in the text file

        if not os.path.exists("servers/{}".format(ctx.message.guild.id)):
            os.makedirs("servers/{}".format(ctx.message.guild.id))

        with open(f"servers/{ctx.message.guild.id}/{ctx.author}data.txt", "r") as f:
            contents = f.readlines()[0]

        embed = discord.Embed(
            title="Player Data",
            description="\n".join(contents.split("."))
        )

        await ctx.send(embed=returnPlayerProfile(ctx.message.guild.id, ctx.author, ctx.message.author.avatar.url))
        await ctx.send(embed=embed)

    @commands.command()
    async def tenwish(self, ctx):

        for i in range(0, 10):
            self.server = ctx.message.guild.id ### Set the server ID

            ##### First, check if the server is registered in the text file

            if not os.path.exists("servers/{}".format(ctx.message.guild.id)):
                os.makedirs("servers/{}".format(ctx.message.guild.id))

            results = Wishing() ### Creating a wishing object, best way to 
                                ### access a range of commands that I have created

            # output = decideWish(self.banner)

            details = workWithPlayer(self.banner, ctx.message.guild.id, ctx.author)
                    #### Output: [pity, fourStar, guarantee, eventguarantee]

            # if len(output) == 2:
            #     await ctx.send(file=output[0], embed=output[1])
            # else:
            await ctx.send(embed=details)

    @commands.command(aliases=["w"])
    async def wish(self, ctx):

        self.server = ctx.message.guild.id ### Set the server ID

        ##### First, check if the server is registered in the text file

        if not os.path.exists("servers/{}".format(ctx.message.guild.id)):
            os.makedirs("servers/{}".format(ctx.message.guild.id))

        results = Wishing() ### Creating a wishing object, best way to 
                            ### access a range of commands that I have created

        # output = decideWish(self.banner)

        details = workWithPlayer(self.banner, ctx.message.guild.id, ctx.author)
                #### Output: [pity, fourStar, guarantee, eventguarantee]

        # if len(output) == 2:
        #     await ctx.send(file=output[0], embed=output[1])
        # else:
        await ctx.send(embed=details)

    # @commands.command()
    # async def banner(self, ctx):
