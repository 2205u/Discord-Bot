import discord
from discord.ext import commands
from datetime import datetime

class Moderation(commands.Cog, name = "Mod"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def maodmanual(self, ctx):
        embed = discord.Embed(title="Help on Byte", description="Staff manual", color=0xdc322f,
                          timestamp=datetime.utcfromtimestamp(1559025608))
        embed.add_field(name=">kick", value="Kicks the mentioned user")
        embed.add_field(name=">ban", value="Bans the mentioned user")
        embed.add_field(name=">purge", value="Deletes specified number of messages")
        embed.set_footer(text="Byte Alpha", icon_url="https://cdn.discordapp.com/attachments/497783794091294740/"
                                                 "582817787974516763/abstract-abstract-painting-art-2230796.jpg")

        await ctx.send(content=None, embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member = None, *, reason: str = None):
        if member == None:
            await ctx.send("Please specify a user to be kicked")
        elif reason == None:
            await discord.Member.kick(member, reason=reason)
            await ctx.send("Kicked " +  str(member) + " for no reason xD")
        else:
            await discord.Member.kick(member, reason=reason)
            await ctx.send("Kicked " + str(member) + " for " + reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member = None, *, reason: str = None):
        if member == None:
            await ctx.send("Please specify a user to ban.")
        elif reason ==  None:
            reason = "No specific reason xD"
            await discord.Member.ban(member, reason = reason)
            await ctx.send("Banned " + str(member) + "for no reason xD")
        else:
            await discord.Member.ban(member, reason = reason)
            await ctx.send("Banned " + str(member) + " for " + reason)
            
    # TODO:
    # @commands.command()
    # @commands.has_permissions(manage_messages = True)
    # async def purge(ctx, number):

def setup(bot):
    bot.add_cog(Moderation(bot))
