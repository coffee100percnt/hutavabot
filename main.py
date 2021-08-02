import discord
from discord.ext import commands
from discord.permissions import Permissions

bot = commands.Bot(command_prefix='*')
guild = discord.Guild

token = 'ODYxNTc0MzIwNjgxMzg1OTg0.YOLxnQ.B8TE2Fscdf4ftCw9IjNOOh2u3QM'

@bot.command()
async def ban(ctx, usr=None, *, reason='пошёл нахуй'):
    if ctx.user.permissions != Permissions.ban_members or ctx.user.permissions != Permissions.administrator:
        pass
    else:
        message = f"Вы были забанены с {ctx.guild.name} по причине {reason}"
        usr.send(message)
        guild.ban(user=usr)
        ctx.send('Ок, забанила')

bot.run(token)