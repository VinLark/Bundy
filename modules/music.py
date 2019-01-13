import discord
from discord.ext import commands
import youtube_dl

class music:
    def __init__(self, bundy):
        self.bundy = bundy

    @commands.command(pass_context=True)
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.bundy.join_voice_channel(channel)

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.bundy.voice_client_in(server)
        await voice_client.disconnect()

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        players = {}
        server = ctx.message.server
        voice_client = self.bundy.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()


def setup(bundy):
    bundy.add_cog(music(bundy))