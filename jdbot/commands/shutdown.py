import discord
from discord.ext import commands
from datetime import datetime

class Owner_Only(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await self.client.close()

def setup(client):
    client.add_cog(Owner_Only(client))
