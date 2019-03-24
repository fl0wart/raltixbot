import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='hs!')
@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    await bot.change_presence(game=discord.Game(name="the community! 👀", type=3))

bot.remove_command('help')

@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)
   
bot.run('NTU5MDk4Mjk0ODA3MTY2OTg4.D3gccQ.mgq1wIkY2_xhdgaXJnq3sRHdwsc')
