import discord
from discord.ext import commands
import asyncio
import youtube_dl
import time
import os


bot=commands.Bot(command_prefix=':')
@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Bot is now online ')
    print('Created by fl0w.')
    bot.loop.create_task(status_task())    	 	 	 	 	 
@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))
               
@bot.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await bot.purge_from(ctx.message.channel, limit = number+1)
bot.say('Succesfully purged the messages!')

@bot.command(pass_context=True)
@commands.cooldown(1, 60*60*24, commands.BucketType.user)
async def daily(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 30
    await bot.edit_message(t, new_content=':white_check_mark: You  received:  {}daily coins'.format(int(ms)))
bot.say('Cooldown is 24 hours!')                                                                     			                           
@bot.event	                                                
async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='made by fl0w.', type=2))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name=str(len(set(bot.get_all_members())))+' users', type=3))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name=str(len(bot.servers))+' servers', type=3))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='made by fl0w.'))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='the server', type=3))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='made by fl0w.', type=2))
        await asyncio.sleep(5)	
        
bot.run('NTU0NzI1MTM5ODA0MDYxNzA2.D2gzpg.P1VmXJSUzozuDyke-y9V50ASK2g')
