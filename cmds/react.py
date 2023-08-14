import discord
from discord.ext import commands
import os
from core import Cog_Extension
import random
from Get_image import get_img_url,get_want_url
from load_save import load,save 
import json
from datetime import datetime,timezone,timedelta
import time
jdata=load('setting.json')
class Get_image(Cog_Extension):

    @commands.command()
    # 自己file的圖   
    async def 抽(self, ctx, msg1="fuck"): 
        if msg1=="help":
            now_time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
            embed=discord.Embed(title="Bot", description="目前功能 >>", color=0x5ce4ff, timestamp=now_time)
            embed.set_author(name="MrLin", icon_url="https://imgur.com/iQPDgwi.jpg")
            embed.set_thumbnail(url="https://img.sxsme.com.cn/uploadimg/image/20220727/20220727103544_15298.gif") 
            #https://art.pixilart.com/13915fd65dd4.gif
            embed.add_field(name="$抽", value="自定義圖片", inline=True)
            embed.add_field(name="$超級抽", value="每月最佳圖片", inline=True)
            embed.add_field(name="$超級抽抽抽 搜尋字", value="你懂得", inline=True)
            embed.set_footer(text="Time")
            await ctx.send(embed=embed)
        else:
            await ctx.send("載入中... (請稍候)") 
            # your file name"01"
            imagelist=os.listdir(r'02')
            pic = discord.File('C:/Users/scott/OneDrive/桌面/DCBot_Tutorial-main/02/'+imagelist[random.randint(0,len(imagelist)-1)])
            await ctx.send(file=pic)
            await ctx.send("完成!")
            print(ctx.msg)
        
    @commands.command()
    # 網站上的圖*指定keyword  
    async def 超級抽抽抽(self, ctx, msg): 
        try: #如果找不到圖片    
            img_url=get_want_url(msg)
            jdata["WantimageURL"]=img_url
            save('setting.json',jdata)
            img_urls=jdata["WantimageURL"]
            n=random.randint(0,len(img_urls)-1)
            url=img_urls[n]
            await ctx.send(url+".jpg")   #await ctx.send(url)
        except Exception as ex: #如果找不到圖片
            print(ex)
            await ctx.send("我從沒看過這種人，給我重選")
            time.sleep(3)
            await ctx.channel.purge(limit = 2) #刪訊息
    @commands.command()
    # 網站上的圖
    async def 超級抽(self, ctx): 
            img_url=get_img_url()
            jdata["imageURL"]=img_url
            save('setting.json',jdata)
            img_urls=jdata["imageURL"]
            n=random.randint(0,len(img_urls)-1)
            url=img_urls[n]
            await ctx.send(url+".jpg")
        
        
        
        
        
        
    
        
    
    
    
    
    
def setup(bot):
    bot.add_cog(Get_image(bot))
        

            
            
        