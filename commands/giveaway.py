import discord
from discord.ext import commands
from dragonUtils import Utils

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giveaway(self, ctx):
        giveaway_embed = discord.Embed(
            color=Utils.COLOR,
            title="🎉Let's Dragon Nitro Giveaway",
            description="Reagiere mit '🐲' auf diese Nachricht, um am Giveaway teilzunehmen!",
        )
        msg = await ctx.send(embed=giveaway_embed)
        await msg.add_reaction('🐲')

async def setup(client):
    await client.add_cog(Giveaway(client))