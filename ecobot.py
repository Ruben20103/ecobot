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
async def start(ctx):
    await ctx.send('Hi, my name is EcoBot. Im an environmental bot. Please type info with prefix ? to know info about this bot')

@bot.command()
async def ecology(ctx):
    await ctx.send('Ecology is the study of the relationships between living organisms, including humans, and their physical environment; it seeks to understand the vital connections between plants and animals and the world around them.')

@bot.command()
async def clean(ctx):
    await ctx.send('please throw the trash into the trash can and teach people to do this and be kind)')

@bot.command()
async def info(ctx):
    await ctx.send('This is an environmental bot wich makes you kind, teaches people how to sort the garbage, talkes about global warming and ecology. Says how to keep the planet clean. Also type commandinfo with prefix ?, to know every commands')

@bot.command()
async def commandinfo(ctx):
    await ctx.send('This bot has many commands. The commands are: start sort, ecology, clean, info, commandinfo, meme, ecopic, globalwarming, instruction, bonus, base, tcanvariations, battery, funfact, stopglobalwarming, . Type every command with prefix ? to make the bot react to your command')

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
async def funfact(ctx):
    await ctx.send('It is possible to make clothes with waste plastics. There are various ways to repurpose waste plastic into clothing materials, including melting down and spinning the plastic into fibers to be woven into fabric, or using shredded plastic as a filling for insulation in outdoor clothing')

@bot.command()
async def tcanvariations(ctx):
    await ctx.send('Trere are different trash canes for different type of garbage such as plastic and glass botles, paper, and more')

@bot.command()
async def battery(ctx):
    await ctx.send('Never throw the battery inside the trash can, there are special factories that deal with batteries ')

@bot.command()
async def globalwarming(ctx):
    await ctx.send('Global warming is the unusually rapid increase in Earths average surface temperature over the past century primarily due to the greenhouse gases released by people burning fossil fuels')

@bot.command()
async def instruction(ctx):
    await ctx.send('Throw the paper into the trash can for only the paper, throw the plastic into the trash can for only the plastic, and other stuff throw into the trash can for other stuff)')

@bot.command()
async def bonus(ctx):
    await ctx.send('if you throw the plastic bottle into the trash can for only the plastic, workers in the recycling company will recycle the plastic bottle into the clothes. Awesome right? :)')

@bot.command()
async def stopglobalwarming(ctx):
    await ctx.send('We can stop global warming with these steps: Renewable energy, Plant trees, Save water, Adjust your thermostat, Avoid wasting food, Recycle right, Spread awareness, Use less hot water, Buy energy-efficient products, Change your lightbulbs, Conserve energy, Turn off electronic devices.(Few examples taken from Google)')

@bot.command()
async def base(ctx):
    await ctx.send('Place a small trash bin in your house for trash)')

bot.run('')
