import discord, os, pandas, json
from discord.ext import commands
import dice
from random import randint

bot = discord.Bot()
token = os.getenv('API_TOKEN')

@bot.event
async def on_ready():
    presence = discord.Game("фурі гей порно без смс і регістрації")
    await bot.change_presence(status=discord.Status.dnd, activity=presence) 
    print("Bot is ready!")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.respond("лох без прав)))")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.respond("аргументи де")

def check_if_it_is_me(ctx):
    return ctx.user.id == 335102389017378818
def to_relative_time(ctx,interval):
    interval = interval.replace("w", " week(s) ")
    interval = interval.replace("d", " day(s) ")
    interval = interval.replace("h", " hour(s) ")
    interval = interval.replace("m", " minute(s) ")
    return interval

#region Moderation
modcategory = bot.create_group("moderation", "Commands for moderating your server")
@modcategory.command()
@commands.has_guild_permissions(ban_members = True)
async def ban(ctx, member:discord.Member, reason="No reason provided"):
    await ctx.create_dm(member.id)
    await member.send(f"You were banned from {ctx.guild.name}")
    await member.ban(reason=reason+"\n\n{ctx.author.name}")
    await ctx.respond()
    

@modcategory.command()
@commands.has_guild_permissions(ban_members = True)
async def unban(ctx, id):
    member = await bot.fetch_user(id)
    await member.unban()
    await ctx.respond(f"{member.display_name} is now unbanned")

@modcategory.command()
@commands.has_guild_permissions(kick_members = True)
async def kick(ctx, member:discord.Member, reason="No reason provided"):
    await ctx.create_dm(member.id)
    await member.send(f"You were kicked from {ctx.guild.name}")
    await member.kick()
    await ctx.respond(f"{member.display_name} is now kicked")

@modcategory.command()
@commands.has_guild_permissions(moderate_members = True)
async def mute(ctx, member:discord.Member, time="10m", reason=None):
    ttime = pandas.Timedelta(time).to_pytimedelta()
    await member.timeout_for(ttime)
    await ctx.respond(f"{member.display_name} is now muted for {to_relative_time(time)}")

@modcategory.command()
@commands.has_guild_permissions(moderate_members = True)
async def unmute(ctx, member:discord.Member):
    await member.remove_timeout()
    await ctx.respond(f"{member.display_name} is now unmuted")
#endregion Moderation

#region Settings
settingscategory = bot.create_group("set", "setings")
#endregion

#region Fun
funcategory = bot.create_group("fun", "Fun commands")

@funcategory.command(name="dice")
async def dice_command(ctx, roll: str):
    await ctx.respond(str(dice.roll(roll)))

@bot.command()
async def random(ctx, smallest: int, highest: int):
    await ctx.respond(str(randint(smallest, highest)))
#endregion Fun

# really dangerous command, only use for testing 
# @bot.command()
# @commands.check(check_if_it_is_me)
# async def cock(ctx, *, command):
#     eval(command)

bot.run(str(token))
