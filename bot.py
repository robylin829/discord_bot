import discord
from discord.ext import commands
import time
import os  
from dotenv import load_dotenv


load_dotenv()
bot = commands.Bot(command_prefix =["$",";"] )
client = discord.Client()##client 是我們與 Discord 連結的橋樑
@bot.event
async def on_ready():
    print(f">>{bot.user} is Online<<")
        

for FileName in os.listdir('./cmds'):
    if FileName.endswith('.py'):
        bot.load_extension(f'cmds.{FileName[:-3]}')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded')
@bot.command()
async def clear(ctx, num:int):
    await ctx.channel.purge(limit = num+1) #刪訊息
    await ctx.send("有些話是秘密")
    time.sleep(5)
    await ctx.channel.purge(limit = 1)
    

if  __name__ == "__main__":
    bot.run(os.getenv('TOKEN'))

