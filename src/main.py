import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
prefix = '!'

@client.event
async def on_ready():
    print(f'{client.user} is now online.')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == f"{prefix}ping":
        await message.channel.send(f"Latency is {client.latency}")
        return


client.run(os.getenv('TOKEN'))
