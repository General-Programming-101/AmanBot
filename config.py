"""
    Important imports
"""
import discord, random, datetime, sys, os

sys.path.append(os.path.abspath(os.path.join('..', 'gifs')))

"""
    Basic String Configurations
"""

COLORS: list = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

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
    )

    [embed.add_field(name=k, value=v, inline=False) for k, v in embedDict.items()]

    return embed

def ReturnEmbed():
    output = {}

    for k, v in OUTPUT_COMS.items():
        output[k] = EmbedGenerator(k, v)

    return output


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

def GifEmbedGenerator(title, desc, gif, mes):
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

#### NOTE Gacha Config

startPlayer = [
    "Pity",
    "Count4Star",
    "Guarantee",
    "EventGuarantee"
]

#### NOTE TarotCard Embed Generator

def TarotEmbed(card, cardDesc, cardNo):
    title = ""

    side = random.randint(0, 1)
    imageName = cardDesc[2]

    print(side)

    if side == 1:
        title = "**__Reverse__ **" + title
        cardDesc = cardDesc[1]
    
    else:
        cardDesc = cardDesc[0]

    whichCard = {
        1: "Past",
        2: "Present",
        3: "Future"
    }

    whichColor = {
        1: 0x000000,
        2: 0x808080,
        3: 0xFFFFFF
    }

    embed = discord.Embed(
        title = "{}".format(whichCard[int(cardNo)]),
        description = title + card,
        color = whichColor[int(cardNo)]
    )

    file = discord.File("images/tarot/{}".format(imageName), filename="{}".format(imageName))
    embed.set_thumbnail(url="attachment://{}".format(imageName))

    embed.add_field(name=f"Here are the values associated with this card", value=f"{cardDesc}")

    embed.set_footer(text="Note: Reverse cards mean the opposite! This generally isn't a good thing...")

    return [file, embed]

RANDOM_FOOTER_MESSAGE = [
    "***Is this your destiny?***",
    "I wonder what this means?",
    "Not happy with your reading? Run it again!",
    "I think your future is doomed"
]
        
################################# HELP COMMAND CONFIG #################################
 
"""
    Help Command Configs
    ############################## NOTE ##############################
    Please, if you're going to add a command, do it here.
    I've already made sure that the help command will run properly, just edit it here
"""

AVAILABLE_CATEGORIES: list = [
    "fun",
    "admin"
]

ADMIN_COMS: dict = {
    "help" : "Self explanatory - Sample use ```seb help```",
    "Kick" : "Self explanatory - Sample use ```seb kick @user```",
}

FUN_COMS: dict = {
    "Kiss" : "Kiss a user - Sample use ```seb kiss @user```",
    "Tarot" : "Returns a Tarot card reading (Major Arcana) - Sample use ```seb tarot```",
}

ALL_COMMANDS: dict = {
    ##### ADMIN COMMANDS
    "help" : "Self explanatory - Sample use ```seb help```",
    "kick" : "Self explanatory - Sample use ```seb kick @user```",

    ##### FUN COMMANDS
    "kiss" : "Kiss a user - Sample use ```seb kiss @user```",
    "tarot" : "Returns a Tarot card reading (Major Arcana) - Sample use ```seb tarot```",
}

RANDOM_FOOTER: list = [
    "Try other commands!",
    "G'day to you sire",
    "Wuthering waves > Genshit",
    "Don't watch **My Happy Sugar Life**"
]

"""
    Help Command Embed Generator
    ############################## NOTE ##############################

    If you're going to edit these, let me know first
"""

OUTPUT_COMS: dict = {
    "Admin Commands" : ADMIN_COMS,
    "Fun Commands" : FUN_COMS,
}

def CommandHelpGenerator(cName, cDescription):

    embed = discord.Embed(
        title = "{} command".format(cName.capitalize()),
        description = cDescription
    )

    embed.set_footer(text=random.choice(RANDOM_FOOTER))

    return embed

def HelpCategoryGenerator(cName):
    
    if cName.lower() == "fun":
        embed = discord.Embed(
            title = "List of Fun Commands",
            description = "\n\n"
        )

        [embed.add_field(name=k, value=v, inline=False) for k, v in FUN_COMS.items()]

    elif cName.lower() == "admin":
        embed = discord.Embed(
            title = "List of Admin Commands",
            description = "\n\n"
        )

        [embed.add_field(name=k, value=v, inline=False) for k, v in ADMIN_COMS.items()]

    return embed

def EmbedGenerator(nameDict, embedDict): #### Returns a Discord Embed
    embed = discord.Embed(
        title = f"{nameDict}",
    )
    
    [embed.add_field(name=k, value=v, inline=False) for k, v in embedDict.items()]

    return embed

def ReturnMainHelp():
    embed = discord.Embed(
        title = "Welcome to the Sebastian Bot Manual!",
        description = "\nTo see a list of commands, directly access a page\n\nTry `seb help fun`\n\nOr you can access a command for more info\n\nTry `seb help tarot`\n\nBelow are the available commands\n"
    )

    embed.add_field(name="Fun", value="For laughs and giggles", inline=False)
    embed.add_field(name="Admin", value="Moderation", inline=False)

    embed.set_thumbnail(url="https://pbs.twimg.com/media/DAB0513WAAAIQpd.png")

    return embed

def ReturnEmbed():
    output = {}

    for k, v in OUTPUT_COMS.items():
        output[k] = EmbedGenerator(k, v)

    return output