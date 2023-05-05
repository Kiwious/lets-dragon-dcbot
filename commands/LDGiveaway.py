import discord, asyncio
from discord.ext import commands
from DragonSettings import Settings

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client
            
    @commands.command()
    async def giveaway(self, ctx):
        giveaway_embed = discord.Embed(
            color=Settings.COLOR,
            title="🎉Let's Dragon Nitro Giveaway",
            description="Reagiere mit '🐲' auf diese Nachricht, um am Giveaway teilzunehmen!",
        )
        giveaway_embed.set_footer(text='Eine Teilnahme am Giveaway erfordert das Zuschauen vom Lets Dragon Event.')
        msg = await ctx.send(embed=giveaway_embed)
        await msg.add_reaction('🐲')
        await asyncio.sleep(Settings.GIVEAWAY_TIME)
        
        winner_embed = discord.Embed(
            color=Settings.COLOR,
            title="🎉 Herzlichen Glückwunsch!",
            description=f"Herzlichen Glückwunsch <@{Settings.GIVEAWAY_WINNER}>.\nDu hast soeben **{Settings.GIVEAWAY_PRICE}** gewonnen!",  
        )
        await ctx.send(embed=winner_embed)

async def setup(client):
    await client.add_cog(Giveaway(client))