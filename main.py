import os
import discord

from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

client = discord.Client()
voice_clients = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('we have loged in n as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello! ")
    if message.content.startswith("$how are you"):
        await message.channel.send("I AM Good ,thank you for asking! ")


@voice_clients.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()


#from line 28 to 35 is the code for bot to join the voice channel if its not in it and if bot is already in the channel stay in it


@voice_clients.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }
    voice = get(client.voice_clients, guild=ctx.guild)


client.run(os.environ['TOKEN'])
