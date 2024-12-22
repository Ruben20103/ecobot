import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.command()
async def sort(ctx):
    await ctx.send('https://steemit.com/hive-161155/@rociogomez/teach-children-to-sort-trash')   

@bot.command()
async def clean(ctx):
    await ctx.send('please throw the trash into the trash can and teach people to do this and be kind)')

@bot.command()
async def meme(ctx):
    memes = os.listdir('memes')
    random_img = random.choice(memes)
    with open(f'memes/{random_img}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def ecopic(ctx):
    ecopics = os.listdir('ecopics')
    random_img = random.choice(ecopics)
    with open(f'ecopics/{random_img}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def globalwarming(ctx):
    await ctx.send('Global warming is the unusually rapid increase in Earths average surface temperature over the past century primarily due to the greenhouse gases released by people burning fossil fuels')

@bot.command()
async def instruction(ctx):
    await ctx.send('throw the paper into the trash can for only the paper, throw the plastic into the trash can for only the plastic, and other stuff throw into the trash can for other stuff)')

@bot.command()
async def bonus(ctx):
    await ctx.send('if you throw the plastic bottle into the trash can for only the plastic, workers in the recycling company will recycle the plastic bottle into the clothes. Awesome right? :)')

@bot.command()
async def base(ctx):
    await ctx.send('place a small trash bin in your house for trash)')

bot.run('')
