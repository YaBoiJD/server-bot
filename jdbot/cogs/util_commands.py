import discord
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!\nLatency is {self.client.latency}')

def setup(client):
    client.add_cog(Utils(client))