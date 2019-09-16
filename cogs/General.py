import discord
from discord.ext import commands
from datetime import datetime

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()  
    async def on_ready(self):
            drpname = "for >manual."  
            activity = discord.Activity(name=drpname, type=discord.ActivityType.watching)
            print("DRP: Watching " + drpname)
            await self.bot.change_presence(activity=activity, status=discord.Status.do_not_disturb)
            print("Bot deployed.")

    @commands.command()
    async def manual(self, ctx):
        embed = discord.Embed(title="Help on Byte", description="All the commands added so far", color=0xdc322f,
            timestamp=datetime.utcfromtimestamp(1559025608))
        embed.add_field(name=">ping", value="Sens back 'Pong!'")
        embed.add_field(name=">pingms", value="Sends back numerical latency")
        embed.add_field(name=">repeat", value="Repeats everything after '>repeat'")
        embed.add_field(name=">poke", value="More useless than SUPW")
        embed.add_field(name=">purge", value="Deletes messages")
        embed.set_footer(text="Byte Alpha", icon_url="https://cdn.discordapp.com/attachments/497783794091294740/"
                                                 "582817787974516763/abstract-abstract-painting-art-2230796.jpg")
        await ctx.send(content=None, embed=embed)
        
    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        await ctx.send("Pong! Numerical latency: " + str(latency) + " ms")
         

def setup(bot):
    bot.add_cog(General(bot))
