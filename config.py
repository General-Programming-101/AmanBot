"""
    Important imports
"""
import discord

"""
    Basic String Configurations
"""

START_UP: str = "Sebastian bot, ready for action"
DESCRIPTION: str = "I am the Sebastian bot!"
RANDOM_HALAL: list = [
    "Jazakumullahu khairan habibi",
    "a’oodhu billaahi min al-shaytaan ir-rajeem",
    "Subhanallah look at the ummah today",
    "Kes omak ya khara"
]

################################# FUN COMMAND CONFIG #################################
with open("gifs/kissGifs.txt", "r") as f:
    kiss = f.readlines()

KISS_GIFS: list = [s.strip() for s in kiss]
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
