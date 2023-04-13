import discord, random, asyncio
from discord.ext import commands
from dragonUtils import Utils

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def get_winner(self):
        return random.choice(Utils.WINNERS)

    @commands.command()
    async def giveaway(self, ctx):
        giveaway_embed = discord.Embed(
            color=Utils.COLOR,
            title="🎉Let's Dragon Nitro Giveaway",
            description="Reagiere mit '🐲' auf diese Nachricht, um am Giveaway teilzunehmen!",
        )
        msg = await ctx.send(embed=giveaway_embed)
        reaction = await msg.add_reaction('🐲')

        users = [user async for user in reaction.users()]
        await ctx.send(users)

async def setup(client):
    await client.add_cog(Giveaway(client))