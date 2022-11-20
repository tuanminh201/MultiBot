import datetime
from datetime import datetime
import discord

from config import *
from game import *
from meme import *
command_prefix = PREFIX
bot =commands.Bot(command_prefix=command_prefix, description="Test Bot",intents = discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name=f'{command_prefix}'))


@bot.command(pass_context=True)

async def hello(ctx, *, arg):
    await ctx.send(f'Hello '+ str(arg))

@bot.command(pass_context=True)
async def info(ctx):
    await ctx.message.add_reaction('❤')
    embed =discord.Embed(
        title= "MultiBot",
        description="Multifunctional Bot",
        timestamp=datetime.now(),
        color= 0x11806a

    )
    msg =await ctx.send(embed=embed)
    await msg.add_reaction('❤')


@bot.command(pass_context=True)
async def crush(ctx):
    await ctx.message.add_reaction('❤')
    embed =discord.Embed(
        title= "bbyginger",
        description="Heartbreaker 💔",
        color= 0xad1457
    )
    msg =await ctx.send(embed=embed)
    await msg.add_reaction('💔')


@bot.command(pass_context=True)

async def clear(ctx,amount :str):
    if amount == 'all':
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=(int(amount)+1))


@bot.command(pass_context=True)
async def botngu(ctx):
    await ctx.message.add_reaction('💀')
    await ctx.send("Mày ngu ý")

@bot.command(pass_context=True)
async def game(ctx):
    await LoadGames(ctx,bot)

@bot.command(pass_context =True)
async def meme(ctx):
    await LoadMemes(ctx,bot)


bot.run(TOKEN)

