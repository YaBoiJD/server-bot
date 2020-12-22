import os

def load_cogs(client):
    for filename in os.listdir(f'{os.getcwd()}/jdbot/cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'jdbot.cogs.{filename[:-3]}')