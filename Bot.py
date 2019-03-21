import discord
from discord.ext import commands
import asyncio
import time
 
bot=commands.Bot(command_prefix='!')
daniel='531493086250139648'
start=time.time()
 
@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    await bot.change_presence(game=discord.Game(name='!help ;)',type=3))
    
@bot.command(pass_context=True)
async def ping():
    await bot.say('ping_pong')
    await bot.say('You pinged me haha')
   
@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
    if ctx.message.author.id==(daniel):
      role=discord.utils.get(ctx.message.server.roles,name='Muted')
 
      await bot.add_roles(target,role)
    else:
        await bot.say('No permission!')
 
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unmute(ctx, member: discord.Member=None):
    if member is None:
      await client.say('Please specify member i.e. Mention a member to unmute. Example- !unmute @user')
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.remove_roles(member, role)
      await client.say("Unmuted {}".format(member))
      for channel in member.server.channels:
        if channel.name == '<log channel name>':
            embed=discord.Embed(title="User unmuted!", description="{0} was unmuted by {1}!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)
            
@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    if ctx.message.author.id==(daniel):
      await bot.send_message(target,'You got an warning!!')
    else:
        await bot.say('No permission!')
       
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
    if ctx.message.author.id==(daniel):
      await bot.kick(target)
    else:
        await bot.say('No permission!')
 
@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
    if ctx.message.author.id==(daniel):
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
    if ctx.message.author.id==(daniel):
        await bot.purge_from(ctx.message.channel,limit=num)
        await bot.say(f'Purged {num} messages.')
    else:
          await bot.say('No permission!')
         
@bot.command(pass_context=True)
async def presence(ctx,text:str,type:int):
    if ctx.message.author.id==(daniel):
        await bot.change_presence(game=discord.Game(name=text,type=type))
    else:
          await bot.say('No permission!')
 
bot.run('NTU4MjE4ODU1MDMwNDU2MzMw.D3Vh-Q.obGMzLZeOExicNs1kt7msyQXvBc')
