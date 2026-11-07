import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def geri_donusum(ctx,*,malzeme):
    atiklar={
        "domates kabukları":"organik.jpg",
        "cam şişe":"glass.jpg",
        "muz kabuğu":"organik.jpg",
        "gazete":"kağıt.jpg",
        "konserve kutusu":"metal.jpg",
        "plastik şişe":"plastik.png"
    }
    if malzeme in atiklar:
        resim= atiklar[malzeme]
        await ctx.send("Bu malzeme için uygun kutu:")
        with open(f"images/{resim}","rb") as f:
            await ctx.send(file=discord.File(f))
    else:
        await ctx.send("Bu malzemeyi tanımıyorum")
bot.run('Çakaal tokenimi göremessin çalamassıssınn kendinikini giğrr')
