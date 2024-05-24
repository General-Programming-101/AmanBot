"""
    Important imports
"""
import discord
import random
import datetime

"""
    Basic String Configurations
"""

COLORS: list = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

START_UP: str = "Sebastian bot, ready for action"
DESCRIPTION: str = "I am the Sebastian bot!"

################################# FUN COMMANDS #################################

RANDOM_HALAL: list = [
    "Jazakumullahu khairan habibi",
    "a’oodhu billaahi min al-shaytaan ir-rajeem",
    "Subhanallah look at the ummah today",
    "Kes omak ya khara"
]

LOVE_MESSAGE: list = [
    "Well, feeling romantic today aren't we",
    "Love is in the air!",
    "Couple of the year 2024?",
    "That is so zesty",
    "Zesticious activites",
    "It should've been me!!!"
]

################################# FUN COMMAND CONFIG #################################

with open("gifs/kissGifs.txt", "r") as f:
    kiss = f.readlines()

KISS_GIFS: list = [s.strip() for s in kiss]

def gifEmbedGenerator(title, desc, gif, mes):
    title = title
    desc = desc
    gif = gif
    mes = mes

    embed = discord.Embed(
        title=title,
        description=desc,
        color=random.choice(COLORS),
        timestamp=datetime.datetime.utcnow()

    )
    embed.set_footer(text=f"{mes}")
    embed.set_image(url=gif)

    return embed

################################# HELP COMMAND CONFIG #################################
 
"""
    Help Command Configs
    ############################## NOTE ##############################
    Please, if you're going to add a command, do it here.
    I've already made sure that the help command will run properly, just edit it here
"""

ADMIN_COMS: dict = {
    "help" : "Self explanatory - Sample use ```seb help```",
    "Kick" : "Self explanatory - Sample use ```seb kick @user```",
}

FUN_COMS: dict = {
    "Kiss" : "Kiss a user - Sample use ```seb kiss @user```"
}

"""
    Help Command Embed Generator
    ############################## NOTE ##############################

    If you're going to edit these, let me know first
"""

OUTPUT_COMS: dict = {
    "Admin Commands" : ADMIN_COMS,
    "Fun Commands" : FUN_COMS,
}

def EmbedGenerator(nameDict, embedDict): #### Returns a Discord Embed
    embed = discord.Embed(
        title = f"{nameDict}",
        # description="Admin commands"
    )
    
    # for k, v in embedDict.items():
    [embed.add_field(name=k, value=v, inline=False) for k, v in embedDict.items()]

    return embed

def ReturnEmbed():
    output = {}

    for k, v in OUTPUT_COMS.items():
        output[k] = EmbedGenerator(k, v)

    return output