import discord
from discord.ext import commands
import os

bot = discord.Bot()

token = os.getenv('API_TOKEN')
def check_if_it_is_me(ctx):
    return ctx.message.author.id == 335102389017378818

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("лох без прав)))")
    if isinstance(error, commands.MissingRequiredArgument):
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
async def ban(ctx, member:discord.Member, *, reason='іді нахуй'):
    await member.ban(reason=f"{reason} ({ctx.author.name})")
    await ctx.send(f'Вигнав {member.name} з сервера.')
    await ctx.create_dm(member.id)
    await member.send(f"Ви були вигнані з {ctx.guild.name} з причини {reason}")

@bot.slash_command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member:discord.Member):
    await member.kick()
    await ctx.send(f'Вигнав {member.name} з сервера.')
    await ctx.create_dm(member.id)
    await member.send(f"Ви були вигнані {ctx.guild.name}")

@bot.slash_command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, id):
<<<<<<< HEAD
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        if user.id == id:
            ctx.guild.unban(user)
=======
    membr = await ctx.fetch_member(id)
    await membr.unban()
    await ctx.send(f"{membr.name} може повертатись на сервер.")
>>>>>>> c512cf1 (translation to ukrainian)

# @bot.slash_command()
# @commands.has_permissions()

# @bot.command()
# @commands.check(check_if_it_is_me)
# async def cock(ctx, *, command):
#     await eval(command)
<<<<<<< HEAD
    
bot.run(token)

=======

bot.run(str(token))
>>>>>>> c512cf1 (translation to ukrainian)
