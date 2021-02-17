"""
uptime command

displays bot uptime
"""

import discord
from discord.ext import commands
from datetime import datetime

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send(f"{days}d, {hours}h, {minutes}m")

def setup(client):
    client.add_cog(Utils(client))
