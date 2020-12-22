import os, sys
from .startup import client, start
from .load_cogs import load_cogs
from dotenv import load_dotenv

load_dotenv() # get environmental elements from .env

if not os.getenv('TOKEN'): # exit if TOKEN is not found
    print('Could not get token, exiting')
    sys.exit()

# start loading cogs and start the bot
load_cogs(client)
start(os.getenv('TOKEN'))
