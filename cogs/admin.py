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

class Admin(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot    


    def randomiser_color(self):
        return discord.Color(random.randint(0, 0xffffff))

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
            await ctx.send(f'{ctx.author.mention} has banned {member.mention}, no reason was given...')
        else:
            await ctx.send(f'{ctx.author.mention} has banned {member.mention}, Reason: {reason}')

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
                embed = discord.Embed(title="Member Unbanned", color=self.randomiser_color())
                embed.add_field(name="Moderator", value=ctx.author.mention, inline=True)
                embed.add_field(name="Member", value=user.mention, inline=True)
                await ctx.send(embed=embed)
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

        if mute_role in member.roles:
            await ctx.send(f"{member.mention} is already Muted")
            return    
        await member.add_roles(mute_role, reason=reason)
        embed = discord.Embed(title="Member Muted", color=self.randomiser_color())
        embed.add_field(name="Moderator", value=ctx.author.mention, inline=True)
        embed.add_field(name="Member", value=member.mention, inline=True)
        embed.add_field(name="Reason", value=reason if reason else "No reason provided", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        mute_role = get(ctx.guild.roles, name="Muted")
        print("Seb is Muting")
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            embed = discord.Embed(title="Member Unmuted", color=self.randomiser_color())
            embed.add_field(name="Moderator", value=ctx.author.mention, inline=True)
            embed.add_field(name="Member", value=member.mention, inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.mention}, the user {member.mention} is not muted')


    @commands.command()
    @has_permissions(create_instant_invite=True)
    async def invite(self, ctx, max_age: int = 3600, max_uses: int = 1):
        if max_uses > 100: 
            embed = discord.Embed(title=f"Warning❗❗❗", description="Max invite uses cannot be over 100 uses", color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        invite = await ctx.channel.create_invite(max_age=max_age, max_uses=max_uses)
        embed = discord.Embed(
            title="Server Invite",
            description=f"Here is your invite link: [Invite Link]({invite.url})",
            color=self.randomiser_color()
        )
        embed.add_field(name="Expires In", value=f"{max_age // 60} minutes {max_age % 60} seconds", inline=True)
        embed.add_field(name="Max Uses", value=f"{max_uses} use(s)", inline=True)
        message = await ctx.send(embed=embed)

        async def update_countdown():
            remaining = max_age
            while remaining > 0:
                await asyncio.sleep(1)
                remaining -= 1
                minutes, seconds = divmod(remaining, 60)
                embed.set_field_at(0, name="Expires In", value=f"{minutes} minutes {seconds} seconds", inline=True)
                await message.edit(embed=embed)
            embed.set_field_at(0, name="Expires In", value="Expired", inline=True)
            await message.edit(embed=embed)

        self.bot.loop.create_task(update_countdown())



    @kick.error
    @ban.error
    @mute.error
    @unmute.error
    async def missing_permissions_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("You do not have permission to use this command")
    
