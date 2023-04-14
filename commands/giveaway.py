import discord, random, asyncio
from discord.ext import commands
from DragonSettings import Settings

async def get_winner(winner_list):
    for i in winner_list:
        if i not in Settings.WINNERS:
            winner_list.remove(i)
    return random.choice(winner_list)
        
class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client
            
    @commands.command()
    async def giveaway(self, ctx):

        reaction_users = []

        giveaway_embed = discord.Embed(
            color=Settings.COLOR,
            title="🎉Let's Dragon Nitro Giveaway",
            description="Reagiere mit '🐲' auf diese Nachricht, um am Giveaway teilzunehmen!",
        )
        msg = await ctx.send(embed=giveaway_embed)
        await msg.add_reaction('🐲')
        await asyncio.sleep(Settings.GIVEAWAY_TIME)
        
        msg = await ctx.fetch_message(msg.id)

        for reaction in msg.reactions:
            if reaction.emoji == '🐲':
                async for user in reaction.users():
                    if user != self.client.user:
                        reaction_users.append(user.id)
        
        winner = await get_winner(reaction_users)
        await ctx.send(f'Nitro gewonnen hat: <@{winner}>')

async def setup(client):
    await client.add_cog(Giveaway(client))