import discord
from discord.ext import commands
import os
import datetime
import pandas

bot = discord.Bot()
token = os.getenv('API_TOKEN')

def check_if_it_is_me(ctx):
    return ctx.message.author.id == 335102389017378818
def torelativetime(interval):
    a = interval.replace("d", " днів ")
    b = a.replace("w", " тижнів ")
    c = b.replace("h", " годин ")
    d = c.replace("m", " хвилин ")
    return d

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("лох без прав)))")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("аргументи де")

@bot.event
async def on_ready():
    presence = discord.Game("фурі гей порно без смс і регістрації")
    await bot.change_presence(status=discord.Status.dnd, activity=presence) 
    print("Bot is ready!")

# @bot.event
# async def on_connect():
    # await bot.sync_commands()
    await bot.register_commands()
    print("Commands are ready!")
    # девелоперы ебанулись им лень делать синк 

@bot.slash_command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member:discord.Member, reason='іді нахуй'):
    await member.ban(reason=f"{reason} ({ctx.author.name})")
    await ctx.respond(f'{member.name} вигнано з сервера.')
    await ctx.create_dm(member.id)
    await member.send(f"Ви були вигнані з {ctx.guild.name} з причини {reason}")

@bot.slash_command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member:discord.Member):
    await member.kick()
    await ctx.respond(f'{member.name} вигнано з сервера.')
    await ctx.create_dm(member.id)
    await member.send(f"Ви були вигнані {ctx.guild.name}")

@bot.slash_command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, id):
    membr = await ctx.fetch_member(id)
    await membr.unban()
    await ctx.respond(f"{membr.name} може повертатись на сервер.")

@bot.slash_command()
@commands.has_permissions(moderate_members = True)
async def mute(ctx, member:discord.Member, time="10m", reason=None):
    ttime = pandasd.Timedelta(time).to_pytimedelta()
    await member.timeout_for(ttime, reason)
    await ctx.respond(f"{member.name} посидить {torelativetime(time)}без права голосу")

@bot.slash_command()
@commands.has_permissions(moderate_members = True)
async def unmute(ctx, member:discord.Member):
    await member.remove_timeout()
    await ctx.respond(f"{member.name} повернено право голосу.")

# @bot.command()
# @commands.check(check_if_it_is_me)
# async def cock(ctx, *, command):
#     await eval(command)

bot.run(str(token))
