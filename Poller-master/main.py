import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=["p-", "-"])
bot.remove_command("help")
with open("token.txt") as f:
    token = f.read()


@bot.event
async def on_ready():
    inv = "https://discordapp.com/oauth2/authorize?&client_id={}&scope=bot&permissions=0"
    print(inv.format(bot.user.id))


@bot.command(pass_context=True)
async def test(ctx):
    await bot.say("ff")

bot.run(token)
