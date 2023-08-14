from tkinter import W
import discord
from discord.ext import commands
import os
from core import Cog_Extension
import random,time
import todo_list
client = discord.Client()##client 是我們與 Discord 連結的橋樑
class Event(Cog_Extension):
    dream_words=["主人","名緯"]
    sad_word=["可以去照鏡子再說","鄭名緯不要再騙自己","お可愛いこと"]#
    @commands.Cog.listener()
    async def on_member_join(self, member):
        g_channel = self.bot.get_channel(int(os.getenv("general_channel")))
        await g_channel.send(f"歡迎{member}加入!")
    
    
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
        elif msg.content.startswith("孤單"):
            await msg.channel.send('可以去照鏡子再說')
        elif "孤單" in msg.content:
            await msg.channel.send('可以去照鏡子再說')
        elif msg.content.startswith("晚安"):  
            await msg.channel.send('風停了…')
            time.sleep(3)
            await msg.channel.send('安靜的世界，適合好好休息。明天見。')
        
        if  msg.content.find("不愛我") != -1 and msg.author.id =="ID": 
             
             await msg.channel.send(f'我當然愛主人<@{msg.author.id}>')
        elif msg.content.find("不愛我") != -1:
            await msg.delete()
            await msg.channel.send(f'你不是主人<@"ID">,可憐')
            
        elif msg.content.startswith("say") :
            if msg.author.id=="ID":
                await msg.delete()
                await msg.channel.send(f'{msg.content[3:]}')
            else:
                await msg.delete()
                await msg.channel.send("無法直面雷霆的人無法發言")
        
        elif any(word in msg.content for word in self.dream_words):
            
            await msg.channel.send(random.choice(self.sad_word))
        
        todo = todo_list.Todo(msg.content)
        for command in todo.commands:
            if msg.content.startswith(command):
            # 成功進來的 command 就是使用者開頭輸入的正確 todo list指令，但還不確定是其中的哪個指令，當然也不確定指令後面的語法又是否正確    
            # 這邊就交給 todo list.py 處理了，他會根據指令內容回傳正確訊息或是指令語法錯誤、輸入日期不合乎常理等等
                await msg.channel.send(todo.command_work(command))
        List = ["Never","gonna","give","up"]
        for i in List:
            if msg.content.find(i) >= 0 and msg.author != self.bot.user:
                await msg.channel.send('Never gonna give u up !')

def setup(bot):
    bot.add_cog(Event(bot))
