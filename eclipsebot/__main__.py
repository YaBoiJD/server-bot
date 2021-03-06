"""
Bot initialization
"""
import os
import sys
from eclipsebot import cogs
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv() # Get environment vars from .env file if any

# Get Token
token = os.getenv("TOKEN")
if not (token):
    print("Error:  Token not found.")
    sys.exit() # quit if token is not found

# Get Prefix
prefix = os.getenv("PREFIX")
if not (prefix):
    prefix = "!" # set prefix to ! if not found

# Setup bot
client = commands.Bot(command_prefix=prefix)

# Load Cogs
for cog in cogs.cogs:
    try:
        client.load_extension(f"eclipsebot.cogs.{cog}")
    except Exception as e:
        print(f"Failed to load cog: {cog}")
        print(f"Error:  {e}")

client.run(token)
