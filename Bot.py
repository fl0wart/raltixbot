import discord
from discord.ext import commands
import asyncio
import time
 
bot=commands.Bot(command_prefix='r!')
flow='535541341980065814'
start=time.time()
 
@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    await bot.change_presence(game=discord.Game(name='r!help ;)',type=1))
  
bot.remove_command('help')
@bot.command(pass_context =True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(Colour = discord.Colour.orange())
    embed.set_author(name = 'Help Commands')
    embed.add_field(name ='r!ping', value ='Ping the bot!', inline=False)
    embed.add_field(name ='r!purge', value ='Deletes certain amount of messages, default amount is 10 (INACTIVE COMMAND / OFFLINE COMMAND)', inline=False)
    embed.add_field(name ='r!mute', value ='Mute an specified user', inline=False)
    embed.add_field(name ='r!unmute', value ='Unmute an specified user', inline=False)
    embed.add_field(name ='r!warn', value ='Warn an specified user', inline=False)
    embed.add_field(name ='r!serverinfo', value ='Gives the server information on the selected user,so you must do ;serverinfo and mention the user!', inline=False)
    embed.add_field(name ='r!kick', value ='Kicks an specified user', inline=False)
    embed.add_field(name ='r!ban', value ='Bans an specified user', inline=False)
    embed.add_field(name ='r!uptime', value ='Get the bot uptime', inline=False)
    embed.add_field(name ='r!presence', value ='Change the bot presence', inline=False)
    
    await client.send_message(author, embed=embed)
    
@bot.command(pass_context=True)
async def ping():
    await bot.say(':ping_pong:')
    await bot.say('You pinged me haha')
   
@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
    if ctx.message.author.id==(flow):
      role=discord.utils.get(ctx.message.server.roles,name='Muted')
 
      await bot.add_roles(target,role)
    else:
        await bot.say('No permission!')
 
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unmute(ctx, member: discord.Member=None):
    if member is None:
      await client.say('Please specify member i.e. Mention a member to unmute. Example- ``mv!unmute @user``')
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.remove_roles(member, role)
      await client.say("Unmuted **{}**".format(member))
      for channel in member.server.channels:
        if channel.name == '<log channel name>':
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)
            
@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    if ctx.message.author.id==(flow):
      await bot.send_message(target,'You got an warning!!')
    else:
        await bot.say('No permission!')
       
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
    if ctx.message.author.id==(flow):
      await bot.kick(target)
    else:
        await bot.say('No permission!')
 
@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
    if ctx.message.author.id==(flow):
      await bot.ban(target)
    else:
        await bot.say('No permission!')
   
@bot.command(pass_context=True)
async def uptime(ctx):
    now=time.time()
    sec=int(now-start)
    mins=int(sec//60)
    await bot.say(f'Uptime is {sec} seconds!')
   
@bot.command(pass_context=True)
async def purge(ctx,num:int):
    if ctx.message.author.id==(flow):
        await bot.purge_from(ctx.message.channel,limit=num)
        await bot.say(f'Purged {num} messages.')
    else:
          await bot.say('No permission!')
         
@bot.command(pass_context=True)
async def presence(ctx,text:str,type:int):
    if ctx.message.author.id==(flow):
        await bot.change_presence(game=discord.Game(name=text,type=type))
    else:
          await bot.say('No permission!')
 
bot.run('NTU0NzI1MTM5ODA0MDYxNzA2.D2gzpg.P1VmXJSUzozuDyke-y9V50ASK2g')
