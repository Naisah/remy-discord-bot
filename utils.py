import discord
from discord.ext import commands


class Utils(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, user: discord.User = None):

        if user is None:
            await ctx.send('Please provide a user to get info on!')
            return

        await ctx.send(user.id)


def setup(client):
    client.add_cog(Utils(client))
