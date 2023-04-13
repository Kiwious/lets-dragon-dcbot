import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(
    command_prefix='.',
    intents=discord.Intents.all()
)

client.remove_command('help')

@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.getenv('TOKEN'))