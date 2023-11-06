import random
import discord


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_nintendo():
    datos = ["El nombre completo de Yoshi es T. Yoshisaur Munchakoopas.",
            "El apellido de Mario es Mario",
            "El nombre y apariencia de Bowser están inspirados en un plato de comida coreano.",
            "A Peach se le conoció como Daisy durante un tiempo por error."
            ]
    return random.choice(datos)

def gen_meme():
    memes = ["meme1.jpg", "mem2.jpg", "meme3.jpg"]
    with open(random.choice(memes), 'rb') as f:
        picture = discord.File(f)
    return picture