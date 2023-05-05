import discord
from discord.ext import commands
from DragonSettings import Settings


class GriefChannel(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def channel(self, ctx):
        channel_name = Settings.CHANNEL_SPAM_NAME
        channel_amt = Settings.CHANNEL_SPAM_AMOUNT
        channel_message = Settings.CHANNEL_SPAM_MESSAGE
        guild = self.client.get_guild(Settings.TEST_SERVER)

        # embed = discord.Embed(title='Channel Spamming', color=Settings.COLOR)

        progress = 0

        if channel_amt == None:
            channel_amt = 500 - len(guild.channels)

        msg = await ctx.send('Initialisiere das Erstellen von Channels')

        for _ in range(channel_amt):
            channel = await guild.create_text_channel(channel_name)
            await channel.send(channel_message)
            await msg.edit(content=f'Erstelle Channel mit dem Namen **{channel_name}**... ({progress}/{channel_amt})')
            progress += 1


async def setup(client):
    await client.add_cog(GriefChannel(client))
