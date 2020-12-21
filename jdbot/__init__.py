import os, sys
from .startup import client, start
from dotenv import load_dotenv

load_dotenv()

# print(f'{os.getcwd()}')

if not os.getenv('TOKEN'):
    print('Could not get token, exiting')
    sys.exit()

for filename in os.listdir(f'{os.getcwd()}/jdbot/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'jdbot.cogs.{filename[:-3]}')

start(os.getenv('TOKEN'))
