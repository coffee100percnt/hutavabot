import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*')
guild = discord.Guild

token = 'ODYxNTc0MzIwNjgxMzg1OTg0.YOLxnQ.LTsffwXW2bWhzIZagq7hHgYmTdM'
def check_if_it_is_me(ctx):
    return ctx.message.author.id == 335102389017378818

@bot.event
async def on_command_error(ctx, error):
    async with ctx.typing():
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("фемка не имеешь права🤣🤣")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("а аргументы.")

@bot.event
async def on_ready():
    bot.add_command(name="ban", description="Банит участника. ```*ban <user> [reason]```")
    bot.add_command(name="kick", description="Кикает участника. ```*kick <user>```")


@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, usr: discord.Member, *, reasn='пошёл нахуй'):
    async with ctx.typing():
        await usr.send(f"Вы были забанены с {ctx.guild.name} по причине {reasn}")
        await usr.ban(reason=f"{reasn} ({ctx.author.name})")
        await ctx.send('Ок, забанил')

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, usr):
    async with ctx.typing():
        await usr.send(f"Вы были кикнуты с {ctx.guild.name}")
        await ctx.guild.kick(user=usr)
        await ctx.send('Ок, кикнул')

@bot.command()
@commands.check(check_if_it_is_me)
async def cock(ctx, *, command):
    await eval(command)
    
bot.run(token)
