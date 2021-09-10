import discord
import random

from discord.ext import commands

intents = discord.Intents().all()

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_member_join(member):
    await member.guild.channels[1].send(f"{member} has joined!")


@client.event
async def on_member_remove(member):
    await member.guild.channels[1].send(f"{member} has left!")


@client.command()
async def ping(ctx):
    await ctx.send(f"I'm busy bro") # what the bot says when you type .ping in the chat xP


@client.command(aliases=['8ball', 'test'])  # this command can be accessed by ._8ball, .8ball, .test
async def _8ball(ctx, *, question):
    responses = ['doubtful', 'definitely', 'indeed', 'no lmao', 'stop wasting my time'] # bunch of randomized responses whenever you ask the bot a question using .8ball
    await ctx.send(f"{random.choice(responses)}")


client.run("ODQ4MjMxNDgyMTA2ODM5MDQw.YLJnIA.U4WRSO5LPPNEN8IdKGHpo9lhH4g") # Regenerated my bot token, this token here is just for reference
