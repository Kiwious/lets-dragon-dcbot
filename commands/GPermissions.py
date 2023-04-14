import discord, asyncio
from discord.ext import commands
from DragonSettings import Settings

        
class GriefSystem(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def check(self, ctx):
        permissions_dict = Settings.CLIENT_PERMISSIONS
        permissions_per_page = 10
        pages = []
        for permission, value in permissions_dict.items():
            emoji = '✅' if value else '❌'
            pages.append(f"{permission}: {emoji}")

        num_pages = (len(pages) + permissions_per_page - 1) // permissions_per_page

        page = 1
        embed = discord.Embed(title="Bot Rechte", description="\n".join(pages[(page-1)*permissions_per_page:page*permissions_per_page]), color=Settings.COLOR)
        embed.set_footer(text=f"Seite {page}/{num_pages}")
        message = await ctx.send(embed=embed)

        if num_pages > 1:
            await message.add_reaction('⬅️')
            await message.add_reaction('➡️')

            def check(reaction, user):
                return user == ctx.author and reaction.message == message and (reaction.emoji == '⬅️' or reaction.emoji == '➡️')

            while True:
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                    await message.remove_reaction(reaction, user)

                    if reaction.emoji == '⬅️':
                        page -= 1
                    elif reaction.emoji == '➡️':
                        page += 1

                    if page < 1:
                        page = num_pages
                    elif page > num_pages:
                        page = 1

                    embed = discord.Embed(title="Bot Rechte", description="\n".join(pages[(page-1)*permissions_per_page:page*permissions_per_page]), color=Settings.COLOR)
                    embed.set_footer(text=f"Seite {page}/{num_pages}")
                    await message.edit(embed=embed)
                except asyncio.TimeoutError:
                    break
        else:
            return
async def setup(client):
    await client.add_cog(GriefSystem(client))