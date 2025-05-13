import discord
from discord.ext import commands

class Cog_Extension(commands.Cog): # 宣告一個新的 Cog 類別
     def __init__(self,bot): # 初始化函式，當這個 Cog 被加載時執行
        self.bot = bot    # 儲存 bot 實例以便之後使用
