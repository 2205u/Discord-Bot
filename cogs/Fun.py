import discord
from discord.ext import commands

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

def setup(bot):
    bot.add_cog(Fun(bot))
