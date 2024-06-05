#!/usr/bin/env python3
"""
    Aman Bot
    Admin Commands
"""

import sys, asyncio, functools, itertools, math, random, os, discord, aiohttp, io, json, pickle, string, random
from config import *
from dotenv import load_dotenv, find_dotenv
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
from itertools import cycle
from discord.utils import get

#### Paginator
import button_paginator as pg
bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

class Admin(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot    

bot = commands.Bot(command_prefix="seb ", intents=discord.Intents.all(), description=DESCRIPTION, help_command=None)

class Admin(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot    

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send("Cogs working")

    @commands.command()
    async def help(self, ctx, *, message=""):

        print(message.lower())


        if message == "":
            await ctx.send(embed=ReturnMainHelp())

        else:
            if message in AVAILABLE_CATEGORIES: #### If it is a valid category
                await ctx.send(embed=HelpCategoryGenerator(message))

            elif message.lower() in ALL_COMMANDS.keys():
                await ctx.send(embed=CommandHelpGenerator(message, ALL_COMMANDS[message.lower()]))

            else:
                await ctx.send("I don't think that command exists yet")
    
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        if reason == None:
            await ctx.send(f'{ctx.author.mention} has kicked {member.mention}, no reason was given...')
        else:
            await ctx.send(f'{ctx.author.mention} has kicked {member.mention}, Reason: {reason}')

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        if reason is None:
            await ctx.send(f'{ctx.author.mention} has kicked {member.mention}, no reason was given...')
        else:
            await ctx.send(f'{ctx.author.mention} has kicked {member.mention}, Reason: {reason}')

    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member: str):
        banned_users = await ctx.guild.bans()
        try:
            name, discriminator = member.split('#')
        except ValueError:
            await ctx.send(f'{ctx.author.mention}, provide a valid username in the format: username#1234')

        for entry in banned_users:
            user = entry.user
            if (user.name, user.discriminator) == (name, discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{ctx.author.mention} unbanned {user.mention}')
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("You do not have permission to use this command.")
        elif isinstance(error, ValueError):
            await ctx.send("Please provide the username and discriminator in the format: username#1234.")
        else:
            raise error
        return

    @commands.command()
    @has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        mute_role = get(ctx.guild.roles, name='Muted')
        
        if mute_role is None:
            mute_role = await ctx.guild.create_role(name='Muted')

            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False)
            
        await member.add_roles(mute_role, reason=reason)

        if reason is None:
            await ctx.send(f'{ctx.author.mention} muted {member.mention}, no reason was given...')
        else:
            await ctx.send(f'{ctx.author.mention} muted {member.mention}, Reason: {reason}')

    @commands.command()
    @has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        mute_role = get(ctx.guild.roles, name="Muted")

        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            await ctx.send(f'{ctx.author.mention} unmuted {member.mention}')
        else:
            await ctx.send(f'{ctx.author.mention}, the user {member.mention} is not muted')


    @kick.error
    @ban.error
    @mute.error
    @unmute.error
    async def missing_permissions_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("You do not have permission to use this command")
    
