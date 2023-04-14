import discord, random, asyncio
from discord.ext import commands
from DragonSettings import Settings

        
class GriefSystem(commands.Cog):
    def __init__(self, client):
        self.client = client
            
    @commands.command()
    async def check(self, ctx):
        pass

async def setup(client):
    await client.add_cog(GriefSystem(client))