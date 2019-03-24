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
   
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    embed=discord.Embed(title="HIGHSCAPE - Announcement", description="{}".format(msg),color=0x00ffff)
    await bot.send_message(channel, embed=embed)
    await bot.delete_message(ctx.message)
    
@client.command(pass_context =True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(Colour = discord.Colour.orange())
    embed.set_author(name = 'Help Commands')
    embed.add_field(name ='hs!say', value ='Returns what the user says.', inline=False)
    embed.add_field(name ='hs!announce', value ='Announce something on an specified channel.', inline=False)
    embed.add_field(name ='hs!serverinfo', value ='Gives the server information on the selected user,so you must do hs!serverinfo and mention the user!', inline=False)

    await client.send_message(author, embed=embed)
    await client.say('📬 Check your DMs!')
    
@client.command(pass_context=True)
async def serverinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    
bot.run('NTU5MDk4Mjk0ODA3MTY2OTg4.D3gccQ.mgq1wIkY2_xhdgaXJnq3sRHdwsc')
