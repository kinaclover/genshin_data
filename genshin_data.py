import genshinstats
import discord
from discord.ext import commands
# from PIL import Image ::::: 이미지 생성을 위한 라이브러리(pip install Pillow)

intents = discord.Intents.all()
intents.members = True
bot_activity = discord.Game(name='원신 데이터 수집')
bot = commands.Bot(command_prefix="!", activity=bot_activity, intents=intents)


@bot.event
async def on_ready():
    print("I'm ready, sir.")


@bot.command()
async def chat(ctx):
    # embed sample code
    embed = discord.Embed(title="Test Title", colour=discord.Colour.blue())
    embed.set_author(name="Embeded Message Test")
    embed.set_footer(text="from 원붕이의 원신생활")
    # embed.set_thumbnail(url="")
    out = "{}, plz do something!".format(ctx.author.mention)
    embed.add_field(name="sample1", value=out)
    embed.add_field(name="sample2", value="")
    await ctx.send(embed=embed)


@bot.command()
async def spiral_check(ctx):
    uid = ctx.author.nick.split('|')[2].strip()
    if len(uid) < 9:
        ctx.send('uid error ::::: {}'.format(ctx.author.mention))
        return
    result = await get_spiral_data(uid)
    await ctx.send("check result ::::: {}".format(result))


# get genshinstats data
async def get_spiral_data(uid):
    genshinstats.set_cookie_auto()
    data = genshinstats.get_spiral_abyss(uid)
    print(data["stats"]["max_floor"])
    print(data["stats"]["total_stars"])
    return data["stats"]
    # return (("12-3" == data["stats"]["max_floor"]) and (36 == data["stats"]["total_stars"]))

    # cookies = {"ltuid": 10743016, "ltoken": "WEyiYcd6J7XEv8zJ2ZA2gtkSRYlU4iooXvAuk4Ly"}
    # client = genshin.Client(cookies)

    # data = await client.get_genshin_user(801936571)
    # print(f"Uset has a total of {len(data.characters)} characters")

    # data = await client.get_spiral_abyss(833296875)
    # print("spiral abyss data ::::: ", data.max_floor, data.total_stars)W


bot.run("")
