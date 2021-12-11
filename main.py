import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions, MissingRequiredArgument
import asyncio

bot = commands.Bot(command_prefix='*')
guild = discord.Guild

token = 'ODYxNTc0MzIwNjgxMzg1OTg0.YOLxnQ.LTsffwXW2bWhzIZagq7hHgYmTdM'

@bot.event()
async def on_command_error(ctx, error):
    async with ctx.typing():
        asyncio.sleep(1)
    if isinstance(error, MissingPermissions):
        ctx.send("фемка не имеешь права🤣🤣")
    if isinstance(error, MissingRequiredArgument):
        ctx.send("а аргументы.")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, usr=None, *, reason='пошёл нахуй'):
    if usr != None:
        async with ctx.typing():
            asyncio.sleep(1)
        usr.send(f"Вы были забанены с {ctx.guild.name} по причине {reason}")
        await usr.ban(user=usr)
        ctx.send('Ок, забанила')
    else:
        raise(MissingRequiredArgument)

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, usr=None):
    if usr != None:
        async with ctx.typing():
            asyncio.sleep(1)
        usr.send(f"Вы были кикнуты с {ctx.guild.name}")
    else:
        raise(MissingRequiredArgument)

bot.run(token)
