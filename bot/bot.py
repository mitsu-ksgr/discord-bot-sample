import discord
from discord.ext import commands

import random

import config


bot = commands.Bot(command_prefix='>')

#
# Event Changes
#
@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name} (ID: {bot.user.id})")


#
# Commands
#
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello, {ctx.author.name}.")

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def fortune(ctx):
    """Try a fotune."""
    result = random.choice([
        '🥳 大吉', '😎 吉', '😆 中吉', '😀 小吉', '🙂 末吉', '🤤 凶', '😇 大凶'
    ])
    await ctx.send(result)

@bot.command()
async def quit(ctx):
    await ctx.send('goodbye!')
    await ctx.bot.logout()
    return

bot.run(config.bot_token)

