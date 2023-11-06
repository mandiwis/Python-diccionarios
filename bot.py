import discord
import random
import asyncio

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
    print("command = meme")
    await ctx.send(file=gen_meme())

@bot.command(name="nintendo")
async def nintendo(ctx):
    print("command = nintendo")
    await ctx.send(gen_nintendo())

@bot.command(name="highlow")
async def highlow(ctx):
    print("command = highlow")
    numeros = [1,2,3,4,5,6,7,8,9,10]
    num1 = numeros.pop(random.randint(0,9))
    num2 = random.choice(numeros)

    usuario = ctx.message.author.name
    texto_juego1 = f"Hola, {usuario}. Tienes que adivinar si el siguiente número al que voy a poner es mayor o menor que el primero."
    texto_juego2 = f"{usuario}, el primer número es {num1}. El segundo es \"mayor\" o \"menor\"?"
    await ctx.send(texto_juego1)
    await ctx.send(texto_juego2)
    
    def is_correct(m):
        return m.author == ctx.message.author and m.content in ["menor", "mayor"]
    
    try:
        guess = await bot.wait_for('message', check=is_correct, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'Te demoraste mucho. El número era {num2}.')

    if guess.content == "mayor" and num2 > num1:
        await ctx.send(f'¡Adivinaste! El segundo número era {num2}')
    elif guess.content == "menor" and num2 < num1:
        await ctx.send(f'¡Adivinaste! El segundo número era {num2}')       
    else:
        await ctx.send(f'Te equivocaste... El segundo número era {num2} :cry: :sob: :sob:.')


bot.run("MTE2MDU5MTYyMjQyMjE0MzAzNg.GV3eYS.50EVY8-om6Nl-WZV5gJ86AyyeRd-EIK73SY4CQ")