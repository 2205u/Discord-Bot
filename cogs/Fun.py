import discord
from discord.ext import commands
import json
from urllib.request import urlopen, Request

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, *, message):
        await ctx.send(message, delete_after=10)

    @commands.command()
    async def poke(self, ctx, member : discord.Member = None):
        if member == None:
            await ctx.send("Please specify a user to poke.")
        else:
            mMember = member.mention
            await ctx.send(ctx.message.author.mention + " poked " + mMember)

    @commands.command()
    async def chatbot(self, ctx, *, chat):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        items = []
        int = 0
        url = ""

        words= chat.split(" ")
        url = '%20'.join(words)
        file = 'https://some-random-api.ml/chatbot?message=' + url

        req = Request(url=file, headers=headers) 
        html = urlopen(req).read() 
        data = json.loads(html)
        msg = str(data)
        msg2 = msg.lstrip(" {'response': ")
        Message = msg2.rstrip("'}'")
        print("Sent message: " + Message)

        await ctx.send(Message)

def setup(bot):
    bot.add_cog(Fun(bot))
