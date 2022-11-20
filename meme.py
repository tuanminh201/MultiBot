import json
import random
import discord
from discord.ext import commands
import urllib

async def LoadMemes(ctx,bot):
    memeAPI =urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

    memeData= json.load(memeAPI)
    memeUrl =memeData['url']
    memeName = memeData['title']
    memePoster = memeData['author']
    memeSub = memeData['subreddit']
    memeLink = memeData['postLink']

    embed =discord.Embed(title=memeName,colour=discord.Colour.purple())
    embed.set_image(url=memeUrl)
    embed.set_footer(text=f"Nguồn: {memePoster} | Subreddit: {memeSub} | Link: {memeLink}")

    await ctx.send(embed=embed)