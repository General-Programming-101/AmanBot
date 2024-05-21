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


################################# HELP COMMAND CONFIG #################################
 
"""
    Help Command Configs
    ############################## NOTE ##############################
    Please, if you're going to add a command, do it here.
    I've already made sure that the help command will run properly, just edit it here
"""

ADMIN_COMS: dict = {
    "help" : "Self explanatory - Sample use `seb help`"
}

"""
    Help Command Embed Generator
    ############################## NOTE ##############################

    If you're going to edit these, let me know first
"""

def AdminEmbedGenerator():
    embed = discord.Embed(
        title="Admin Commands",
        description="Admin commands"
    )
    
    for k, v in ADMIN_COMS.items():
        embed.add_field(name=k, value=v, inline=False)

    return embed