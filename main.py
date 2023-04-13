import discord, os, asyncio
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

async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await client.load_extension(f"commands.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start(os.getenv('TOKEN'))

asyncio.run(main())