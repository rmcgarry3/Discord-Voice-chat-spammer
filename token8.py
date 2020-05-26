import discord
import asyncio
import youtube_dl
import os
from discord import VoiceClient
from main import chanid

client8 = discord.Client()

t = open("tokens.txt", "r")

tokie = t.readlines()
voice_id = chanid
token1 = tokie[8].rstrip()


@client8.event
async def on_ready():
    print('Token 2: Logged in!')
    await client8.loop.create_task(main())


async def main():
    voice_channel1 = client8.get_channel(voice_id)
    vc1 = await voice_channel1.connect()
    vc1.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="alert.mp3"),
             after=lambda e: print('done', e))
