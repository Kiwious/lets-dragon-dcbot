import discord
from discord.ext import commands
from DragonSettings import Settings

class BanSystem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx):
        guild = self.client.get_guild(Settings.TEST_SERVER)

        banned = []

        embed = discord.Embed(
            color=Settings.COLOR,
            title='Lets Dragon Member Ban System',
            description='Starte das Member-Bannen, dies kann einige Minuten zur vollständigen Ratifizierung dauern.'
        )

        embed_banned = discord.Embed(
            color=Settings.COLOR,
            title='Lets Dragon Member Ban System',
        )

        await ctx.send(embed=embed)

        for member in guild.members:
            try:
                await member.ban(reason=f'{Settings.BAN_REASON}')
                embed_banned.description = f'{member} wurde gebannt'
                await ctx.send(embed=embed_banned)
                banned.append(member)
            except discord.errors.Forbidden: # Keine Rechte Error
                embed_banned.description = f'{member} konnte nicht gebannt werden; keine Rechte, setze Member-Bannen fort...'
                await ctx.send(embed=embed_banned)
                continue
        
        await ctx.send('✅ Member Bannen abgeschlossen. Lang lebe Patrick der I., Führer der MGA!')

async def setup(client):
    await client.add_cog(BanSystem(client))
