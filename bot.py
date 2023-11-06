import discord

from discord.ext import commands
from bot_logic import gen_pass, gen_nintendo, gen_meme

#print(gen_pass(10))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Ha iniciado sesión como {bot.user}")

@bot.command(name="meme")
async def meme(ctx):
    await ctx.send(file=gen_meme())

@bot.command(name="nintendo")
async def nintendo(ctx):
    await ctx.send(gen_nintendo())

bot.run("MTE2MDU5MTYyMjQyMjE0MzAzNg.GwI70i.nfRi7xyO3kBpcppt7NaL8j-BG_b-_b--M215LY")