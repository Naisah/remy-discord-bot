import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix='!')

TOKEN = os.getenv('DISCORD_TOKEN')


@client.event
async def on_ready():
    print('Remy is ready!')


@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong: pong!')


@client.command()
async def say(ctx, *, message=None):
    if message == None:
        await ctx.send('Please provide a message!')
        return

    await ctx.send(message)


@client.command()
async def userinfo(ctx, user: discord.User):
    await ctx.send(user.id)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
