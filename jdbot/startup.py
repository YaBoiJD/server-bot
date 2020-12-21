import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

def start(token):
    client.run(token)
