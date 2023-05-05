import discord
from discord.ext import commands
from DragonSettings import Settings


class GriefRemoveChannels(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remove(self, ctx):
        guild = self.client.get_guild(Settings.TEST_SERVER)
        channels = guild.channels
        channel_amt = len(channels) - len(Settings.TEST_SERVER_DEFAULT_CHANNELS)

        progress = 0

        for channel in channels:
            if channel.id in Settings.TEST_SERVER_DEFAULT_CHANNELS:
                print('Community channel wird übersprungen...')
                continue

            await channel.delete()
            print(f'Channel gelöscht: {channel.name}\nGelöschte Channel: {progress}/{channel_amt}\n-----------------------------')
            progress += 1

            if progress == channel_amt:
                print('Channel löschen erfolgreich! Lang lebe Patrick der I., Führer der MGA!')
                break


async def setup(client):
    await client.add_cog(GriefRemoveChannels(client))
