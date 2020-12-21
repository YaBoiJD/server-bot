import discord
from discord.ext import commands
from datetime import datetime

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.client.user} is online.')
        self.client.launch_time = datetime.utcnow()

def setup(client):
    client.add_cog(Events(client))