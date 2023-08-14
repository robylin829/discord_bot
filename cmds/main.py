import discord
from discord.ext import commands
import os
from core import Cog_Extension
import random
client = discord.Client()##client 是我們與 Discord 連結的橋樑
class Main(Cog_Extension):

    @commands.command()
    async def Hello(self, ctx):
        print(ctx.author)
        await ctx.send(f'<@{ctx.author.id}>還真是可愛')
        print(f'<@{ctx.author.id}>')
        
    @commands.command()
    async def Game(self, ctx):
        await ctx.send("輸入'@猜+oooo'猜一個4位數字")
        
        
           
    @commands.command()
    async def Video(self,ctx):
        embed=discord.Embed(title="杰哥不要 the 音樂劇", url=os.getenv("title"), description="非常好影片", color=0xce1c1c)
        embed.set_author(name="杰哥", url=os.getenv("author"), icon_url=os.getenv("icon"))
        embed.set_thumbnail(url=os.getenv("thumbnail"))
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Main(bot))
    
    