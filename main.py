import discord, os, pandas, json
from discord.ext import commands
import localization as localize
from dice import roll as rollmydice
from random import randint

bot = discord.Bot()
token = os.getenv('API_TOKEN')

@bot.event
async def on_ready():
    # global guildbase
    # try:
    #     guildbasefile = open("./guildlang.json", 'r')
    # except FileNotFoundError:
    #     guildbasefile =  open("./guildlang.json", 'x')
    #     guildbasefile.close()
    #     guildbasefile =  open("./guildlang.json", 'w')
    #     guildbasefile.write('{}')
    #     guildbasefile.close()
    #     guildbasefile = open("./guildlang.json", 'r')
    # guildbase = json.loads(guildbasefile.read())
    # guildbasefile.close()
    presence = discord.Game("e621 - femboy male/male")
    await bot.change_presence(status=discord.Status.dnd, activity=presence) 
    print("Bot is ready!")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.respond("You can't execute this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.respond("missing argument smh")
# @bot.event
# async def on_guild_join(guild):
#     if str(guild.id) in guildbase:
#         pass
#     else:
#         guildbase[str(guild.id)] = "en"

#get guild language
# def "en":
#     return guildbase[str(ctx.guild.id)]
def check_if_it_is_me(ctx):
    return ctx.user.id == 335102389017378818
def to_relative_time(ctx,interval):
    interval = interval.replace("w", localize.weeks["en"])
    interval = interval.replace("d", localize.days["en"])
    interval = interval.replace("h", localize.hours["en"])
    interval = interval.replace("m", localize.minutes["en"])
    return interval
# write result to guildbase
# def refresh_guildbase():
#     refreshedjson = json.dumps(guildbase)
#     guildbasefile = open("./guildlang.json", 'w')
#     guildbasefile.write(refreshedjson)
#     guildbasefile.close()

#region Moderation
modcategory = bot.create_group("moderation", "Commands for moderating your server")
@modcategory.command()
@commands.has_guild_permissions(ban_members = True)
async def ban(ctx, member:discord.Member):
    await member.ban(reason=f"{ctx.author.name} did this")
    await ctx.respond(localize.ban["en"].format(member.display_name))
    await ctx.create_dm(member.id)
    await member.send(localize.bandm["en"].format(ctx.guild.name))

@modcategory.command()
@commands.has_guild_permissions(ban_members = True)
async def unban(ctx, id):
    membr = await ctx.fetch_member(id)
    await membr.unban()
    await ctx.respond(localize.unban["en"].format(membr.display_name))

@modcategory.command()
@commands.has_guild_permissions(kick_members = True)
async def kick(ctx, member:discord.Member):
    await member.kick()
    await ctx.respond(localize.kick["en"].format(member.display_name))
    await ctx.create_dm(member.id)
    await member.send(localize.kickdm["en"].format(ctx.guild.name))

@modcategory.command()
@commands.has_guild_permissions(moderate_members = True)
async def mute(ctx, member:discord.Member, time="10m", reason=None):
    ttime = pandas.Timedelta(time).to_pytimedelta()
    await member.timeout_for(ttime)
    await ctx.respond(localize.mute["en"].format(member.display_name, to_relative_time(ctx, time)))

@modcategory.command()
@commands.has_guild_permissions(moderate_members = True)
async def unmute(ctx, member:discord.Member):
    await member.remove_timeout()
    await ctx.respond(localize.unmute["en"].format(member.display_name))
#endregion Moderation

#region Settings
settingscategory = bot.create_group("set", "setings")

# @settingscategory.command()
# @commands.has_guild_permissions(manage_guild = True)
# async def serverlang(ctx, lang):
#     if lang in localize.supported_languages:
#         guildbase[str(ctx.guild.id)] = lang
#         await ctx.respond(localize.lang_change_success[lang])
#         refresh_guildbase()
#     else:
#         await ctx.respond(localize.lang_not_supported["en"].format("en"))
#endregion

#region Fun
funcategory = bot.create_group("fun", "Fun commands")

@funcategory.command()
async def dice(ctx, roll: str):
    await ctx.respond(str(rollmydice(roll)))

@funcategory.command()
async def random(ctx, smallest: int, highest: int):
    await ctx.respond(str(randint(smallest, highest)))
#endregion Fun

# really dangerous command, only use for testing 
# @bot.command()
# @commands.check(check_if_it_is_me)
# async def cock(ctx, *, command):
#     eval(command)

bot.run(str(token))
