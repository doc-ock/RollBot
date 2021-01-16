import discord
import random
import credentials
import asyncio
import string
from awaken import awaken

from discord.ext import commands
from discord.utils import get

#variable names
bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

#messages on startup
@bot.event
async def on_ready():
    print("RollBot is awake!")
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print('------------------')
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("Roll For Initiative"))

# Globals for message removal
messageHistory = set()
computemessageHistory = set()
previousQuery = ''

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='Add two numbers together.')
async def add(ctx, a: int, b: int):
    """Add two numbers together."""
    await ctx.send(a+b)

@bot.command(description='Multiply two numbers together.')
async def multiply(ctx, a: int, b: int, type = None):
    """Multiply two numbers together."""
    if type == None:
        await ctx.send(a*b)
    # Add conversion to binary or whatever to both add and multiply 
     
# TODO: Add a math function

@bot.command()
async def ping(ctx):
    """Pings the bot and tests the latency of the response."""
    # Get the latency of the bot
    latency = bot.latency
    # Send it to the user
    await ctx.send('Pong!')
    await ctx.send('%.3d ms' %(latency * 100))

@bot.command()
async def eightball(ctx, *, question = None):
    """Get some answers."""
    if question == None:
        msg = 'You need to ask me a question first.'
        await ctx.send(msg)
        return

    answerList = [  "It is certain",
                    "It is decidedly so",
                    "Without a doubt",
                    "Yes, definitely",
                    "You may rely on it",
                    "As I see it, yes",
                    "Most likely",
                    "Outlook good",
                    "Yes",
                    "Signs point to yes",
                    "Reply hazy try again",
                    "Ask again later",
                    "Better not tell you now",
                    "Cannot predict now",
                    "Concentrate and ask again",
                    "Don't count on it",
                    "My reply is no",
                    "My sources say no",
                    "Outlook not so good",
                    "Very doubtful"    ]

    await ctx.send(random.choice(answerList))

@bot.command()
async def hello(ctx):
    """Say hello."""
    response = [":sparkles: :wave: Hello, " + ctx.message.author.mention , ctx.message.author.mention + ", nice to meet you."]
    await ctx.send(random.choice(response))

@bot.command(description='The bot chooses between multiple options for you.')
async def choose(ctx, *choices: str):
    """DianaBot chooses between multiple options for you."""
    await ctx.send(random.choice(choices))

@bot.command(description='Information about RollBot.')
async def info(ctx):
    embed = discord.Embed(title="About RollBot", description="Ping the bot using the prefix '.'", color=0xadd8e6)
    # give info about you here
    embed.add_field(name="Author", value="Quantum#0648")
    embed.set_thumbnail(url=bot.user.avatar_url)
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Developer information", value="Version 1.0.1. | Built with Python 3.7.2.")

    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title=":sparkles: You asked for help? :sparkles:", description="RollBot is a multipurpose bot coded by Quantum. Now in Python flavor!", color=0xadd8e6)

    embed.add_field(name=".add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name=".ping", value="Returns latency of request.", inline=False)
    embed.add_field(name=".roll XdY :game_die:", value="Rolls **X** amount of random dice in NdN format, **Y**", inline=False)
    embed.add_field(name=".eightball `query`", value="Ask for help, and perhaps receive a helpful answer.", inline=False)
    embed.add_field(name=".multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name=".hello", value="RollBot will tell you hello.", inline=False)
    embed.add_field(name=".info", value="Gives a little information about the bot:\nThe bot maker, and the number of servers RollBot is currently in.", inline=False)
    embed.add_field(name=".help", value="List of commands that RollBot is currently capable of completing.", inline=False)
    embed.add_field(name=".wa `query`", value="RollBot will try and answer any question you may have. (Uses Wolfram|Alpha API to find smart answers to questions.)\nStill in progress.", inline=False)

    await ctx.send(embed=embed)

awaken()
bot.run(credentials.secretpassword)