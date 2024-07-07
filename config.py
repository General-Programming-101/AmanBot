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

HATE_MESSAGE: list = [
    "Feeling violent today aren't we?",
    "Bro might just be the antagonist",
    "Who made you angry today :skull:",
    "womp womp...?",
    "INNER PEACE!! INNER PEACE!!!!"
]

################################# FUN COMMAND CONFIG #################################

with open("gifs/kissGifs.txt", "r") as f:
    kiss = f.readlines()

f.close()
KISS_GIFS: list = [s.strip() for s in kiss]

with open("gifs/hugGifs.txt", "r") as f:
    hug = f.readlines()

f.close()
HUG_GIFS: list = [s.strip() for s in hug]

with open("gifs/shootGifs.txt", "r") as f:
    shoot = f.readlines()

f.close()
SHOOT_GIFS: list = [s.strip() for s in shoot]

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

ADMIN_COMS: dict = {
    "help" : "Self explanatory - Sample use ```seb help```",
    "Kick" : "Self explanatory - Sample use ```seb kick @user```",
}

FUN_COMS: dict = {
    "Kiss" : "Kiss a user - Sample use ```seb kiss @user```"
}

MUSIC_COMS: dict = {
    "play" : "Plays a song - Sample use ```seb play Never gonna give you up```",
    "pause" : "Pauses the song that is ***currently*** playing - Sample use ```seb pause```",
    "resume" : "Resumes the song that was ***currently*** playing - Sample use ```seb resumme```",
    "skip" : "Skips the song that is ***currently*** playing and moves to the next one in the queue ```seb skip```",
    "queue" : "Queues the song and adds it to the queue ```seb queue Never gonna give you up```",
    "clearq" : "Clears the queue ```seb clearq```",
}

OUTPUT_COMS: dict = {
    "Admin Commands" : ADMIN_COMS,
    "Fun Commands" : FUN_COMS,
    "Music Commands" : MUSIC_COMS
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

AVAILABLE_CATEGORIES: list = [
    "fun",
    "admin",
    "music"
]

ALL_COMMANDS: dict = {
    ##### ADMIN COMMANDS
    "help" : "Self explanatory - Sample use ```seb help```",
    "kick" : "Self explanatory - Sample use ```seb kick @user```",

    ##### FUN COMMANDS
    "kiss" : "Kiss a user - Sample use ```seb kiss @user```",
    "tarot" : "Returns a Tarot card reading (Major Arcana) - Sample use ```seb tarot```",

    ##### MUSIC COMMANDS
    "play" : "Plays a song - Sample use ```seb play Never gonna give you up```",
    "pause" : "Pauses the song that is ***currently*** playing - Sample use ```seb pause```",
    "resume" : "Resumes the song that was ***currently*** playing - Sample use ```seb resumme```",
    "skip" : "Skips the song that is ***currently*** playing and moves to the next one in the queue ```seb skip```",
    "queue" : "Queues the song and adds it to the queue ```seb queue Never gonna give you up```",
    "clearq" : "Clears the queue ```seb clearq```",
}

RANDOM_FOOTER: list = [
    "Try other commands!",
    "G'day to you sire",
    "Wuthering waves > Genshit",
    "Don't watch **My Happy Sugar Life**"
]

"""
    Embed Generators
    ############################## NOTE ##############################

    If you're going to edit these, let me know first
"""

OUTPUT_COMS: dict = {
    "Admin Commands" : ADMIN_COMS,
    "Fun Commands" : FUN_COMS,
}

def EmbedAPIGenerator(desc, footer):
    # title = "Title" if title == False else title
    desc = "Description" if desc  == False else desc
    footer = "Footer" if footer == False else footer

    embed = discord.Embed(
        description = desc
    )

    embed.set_footer(text=footer)

    return embed

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

    elif cName.lower() == "music":
        embed = discord.Embed(
            title = "List of Music Commands",
            description = "\n\n"
        )

        [embed.add_field(name=k, value=v, inline=False) for k, v in MUSIC_COMS.items()]

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
    embed.add_field(name="Music", value="For Grooving and Moving", inline=False)

    embed.set_thumbnail(url="https://pbs.twimg.com/media/DAB0513WAAAIQpd.png")

    return embed

def ReturnEmbed():
    output = {}

    for k, v in OUTPUT_COMS.items():
        output[k] = EmbedGenerator(k, v)

    return output

def ClipThatEmbed(messages, member):

    output = {}
    outputList = []
    i = 1

    for line in messages:
        message = line.strip().split("{$.^")

        if str(member) in message:
            output[member] = message
        
        for v in output.values():
            if i == 10:
                outputList.append(f"**{str(i)}.** " + v[0])
            else:
                outputList.append(f"**{str(i)}.** " + " " + v[0])
            i = i + 1

    print(outputList)

    desc = ["**Your favourite moments from <@{}>**".format(member), "\n"]
    embed = discord.Embed(
        title = "Clipped moments",
        description = "\n".join(desc + outputList)
    )

    # [embed.add_field(name=f"<@{member}>", value=v, inline=False) for k, v in output.items()]

    return embed