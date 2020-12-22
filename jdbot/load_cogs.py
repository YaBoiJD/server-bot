import os

def load_cogs(client):
    for filename in os.listdir(f'{os.getcwd()}/jdbot/events'):
        if filename.endswith('.py'):
            print(f'loading event {filename[:-3]}')
            client.load_extension(f'jdbot.events.{filename[:-3]}')

    for filename in os.listdir(f'{os.getcwd()}/jdbot/commands'):
        if filename.endswith('.py'):
            print(f'loading command {filename[:-3]}')
            client.load_extension(f'jdbot.commands.{filename[:-3]}')
