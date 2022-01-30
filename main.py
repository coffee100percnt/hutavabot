import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="*")

token = ''
def check_if_it_is_me(ctx):
    return ctx.message.author.id == 335102389017378818

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("фемка не имеешь права🤣🤣")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("а аргументы.")

@bot.event
async def on_ready():
    # presence = discord.BaseActivity(name="секс с конки")
    # await bot.change_presence(status=discord.Status.dnd, activity=presence) 
    await bot.change_presence(status=discord.Status.dnd)

# @bot.event
# async def on_connect():
    # await bot.sync_commands()
    await bot.register_commands()
    print("Commands are ready!")
    # девелоперы ебанулись им лень делать синк 

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member:discord.Member, *, reason='пошёл нахуй'):
    await member.ban(reason=f"{reason} ({ctx.author.name})")
    await ctx.send('Ок, забанил')
    await ctx.create_dm(member.id)
    await member.send(f"Вы былы забанены с {ctx.guild.name} по причине {reason}")

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member:discord.Member):
    await member.kick()
    await ctx.send('Ок, кикнул')
    await ctx.create_dm(member.id)
    await member.send(f"Вы были кикнуты с {ctx.guild.name}")

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, id):
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        if user.id == id:
            ctx.guild.unban(user)


# @bot.command()
# @commands.check(check_if_it_is_me)
# async def cock(ctx, *, command):
#     await eval(command)
    
bot.run(token)

