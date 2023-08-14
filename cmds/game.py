from multiprocessing.connection import Client
import discord
from discord.ext import commands
from core import Cog_Extension
import random
import datetime
from datetime import datetime,timezone,timedelta
client = discord.Client()##client 是我們與 Discord 連結的橋樑
class Game(Cog_Extension):
    def __init__(self,ctx)->None:
        self.commands =["$猜 help","$猜 start","$猜","$猜 exit","$猜 scoreboard"]
        self.key =""
        self.choose =["1","2","3","4","5","6","7","8","9"]
        self.guess_time =0
        self.score ={}
        self.fast_list ={}
        self.guess_list =[]
    @commands.command()
    async def 猜(self,ctx,msg1):
        if ctx.author==client.user: #如果是機器人就不管
            return 
        
        elif msg1=="help": #要help    
            now_time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
            embed=discord.Embed(title="Bot", description="目前功能 >>", color=0x5ce4ff, timestamp=now_time)
            embed.set_author(name="MrLin", icon_url="https://imgur.com/iQPDgwi.jpg")
            embed.set_thumbnail(url="https://art.pixilart.com/13915fd65dd4.gif")
            embed.add_field(name="$猜 start", value="開始遊戲", inline=True)
            embed.add_field(name="$猜 exit", value="離開遊戲", inline=True)
            embed.add_field(name="$猜 <4位數>", value="猜數字", inline=True)
            embed.add_field(name="$猜 scoreboard", value="記分板", inline=True)
            embed.set_footer(text="Time")
            await ctx.send(embed=embed)
        elif msg1=="exit": #離開遊戲，重製數字
            self.key=""
            self.choose=["1","2","3","4","5","6","7","8","9"]
            self.guess_time=0
            await ctx.send("exited")
        
        elif msg1=="scoreboard": #查看排行榜(用猜測次數當key，玩家id當value)
            score=self.score
            score_key=sorted(score.keys())
            j=0
            print(score) #查看最近一次猜測紀錄
            for i in score_key:
              j+=1
              print(score[i])  
              await ctx.send(f'{j}. 猜了{i}次 **{score[i]}**')
            
             
        elif msg1=="start": #生成遊戲代碼
            self.key=""
            for i in range(4):
                pin=self.choose[random.randint(0, len(self.choose)-1)]
                self.key+=pin
                self.choose.remove(pin)
                print(self.key) #列出要猜的數字
                
            await ctx.send("Game started,please send game via `$猜 <your guess>`,eg:`$猜 1235`")
        
        
        elif len(msg1)==4 and (msg1.isdigit()) and int(msg1)>0: #確認格式是否正確
            try:    
                guess=[]
                guess_time=self.guess_time
                b=msg1
                A,B=0,0 #猜對並在正確位置，猜對但不在正確位置
                for i in range(4):
                    a=b[0:1]
                    b=b[1:] 
                    guess.append(a)
                    if a==self.key[i:i+1]:
                        A+=1
                B={x for x in msg1 if x in self.key}
                B=len(B)-A
                guess_time+=1
                print(guess_time)
                self.guess_time=guess_time    
                if A==4:
                    await ctx.send(f'恭喜答對,答案是{self.key},你用了{guess_time}次機會')
                    self.guess_time=0
                    if self.fast_list.get(ctx.author,77)==77: #沒有record，創建帳戶
                        self.fast_list[ctx.author]=guess_time #存個人紀錄
                        if self.score.get(guess_time,77)==77: #如果該次數已有人
                            self.score[guess_time]=ctx.author
                        else:
                            self.score[guess_time]=self.score[guess_time]+" "+ctx.author
                    else:
                        if self.fast_list[ctx.author]>guess_time: #比原先紀錄快
                            old_data=self.fast_list[ctx.author]
                            print(self.score[old_data])
                            pop_bool=len(self.score[old_data])
                            if pop_bool==len(str(ctx.author)): #舊紀錄只有一個，就全刪掉
                                self.score.pop(self.score[old_data])
                            else:
                                old_word_start=self.score[old_data].find(ctx.author)#舊紀錄不只一個，找到那個人的位置
                                self.score[old_data]=(self.score[old_data])[0:old_word_start]+(self.score[old_data])[old_word_start+pop_bool:]
                            # self.score[self.fast_list[ctx.author]].replace(ctx.author," ")
                            self.fast_list[ctx.author]=guess_time
                            if self.score.get(self.guess_time,77)==77:
                                self.score[guess_time]=ctx.author
                            else:
                                self.score[guess_time]=self.score[guess_time]+" "+ctx.author
                        
                    
                else:
                    await ctx.send(f'{A}A{B}B')
            except Exception as ex:
                print(ex) #發生什麼錯誤
                await ctx.send("格式有誤 請參考'$猜 help'格式")
        else:
            print(msg1) #觸發錯誤訊息
            await ctx.send("格式有誤 請參考'$猜 help'格式")        
                    
                
        
            
            
            
def setup(bot):
    bot.add_cog(Game(bot))        
    
         