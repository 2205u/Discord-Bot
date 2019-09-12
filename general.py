# imports -------------------------
import discord
from discord.ext import commands

from datetime import datetime
# ---------------------------------


Client = discord.Client()  
bot = commands.Bot(command_prefix="!")  # TODO: add variable prefix
# TODO: add cogs


class General(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
@commands.Cog.listener()
async def on_ready(self):  
    drpname = "for >manual."  
    activity = discord.Activity(name=drpname, type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity, status=discord.Status.do_not_disturb)
    print("DRP: Watching " + drpname)
    print("Bot deployed.")


# @bot.command
# async def manual(ctx):
#     embed = discord.Embed(title="Help on Byte", description="All the commands added so far", color=0xdc322f,
#                           timestamp=datetime.utcfromtimestamp(1559025608))
#     embed.add_field(name=">ping", value="Sens back 'Pong!'")
#     embed.add_field(name=">pingms", value="Sends back numerical latency")
#     embed.add_field(name=">repeat", value="Repeats everything after '>repeat'")
#     embed.add_field(name=">purge", value="Deletes specified number of messages")
#     embed.add_field(name=">poke", value="More useless than SUPW")
#     #TODO:
#         # embed.add_field(name=">kick", value="Kicks the mentioned user") change to
#         # embed.add_field(name=">ban", value="Bans the mentioned user") mod only class
#     embed.set_footer(text="Byte Alpha", icon_url="https://cdn.discordapp.com/attachments/497783794091294740/"
#                                                  "582817787974516763/abstract-abstract-painting-art-2230796.jpg")

#     await ctx.send(content=None, embed=embed)


# @bot.command()
# async def ping(ctx):
#     await ctx.send("Pong!", delete_after=10)


# @bot.command()
# async def pingms(ctx):
#     latency = bot.latency
#     await ctx.send(latency, delete_after=10)


# @bot.command()
# async def repeat(ctx, *, message):
#     await ctx.send(message, delete_after=10)


# @bot.command(pass_context=True)
# async def poke(ctx, member: discord.Member):
#     member = member.mention
#     await ctx.send(ctx.message.author.mention + " poked " + member)

# """ Cogs:MOD ONLY """
# @bot.command(pass_context=True,)
# @commands.has_permissions(manage_messages=True)
# async def purge(ctx, number):
#     number = int(number)
#     if number > 99 or number < 1:
#         await ctx.send("I can only delete messages within a range of 1 - 99", delete_after=10)
#     else:
#         mgs = []
#         number = int(number)
#         channel = ctx.message.channel
#         async for x in discord.abc.Messageable.history(channel, limit=int(number+1)):
#             mgs.append(x)
#         for y in mgs:
#             await discord.Message.delete(y)
#         await ctx.send(str(number) + ' Messages deleted!', delete_after=10)


# @bot.command()
# @commands.has_permissions(kick_members=True)
# async def kick(ctx, member: discord.Member, *, reason: str = None):
#     await discord.Member.kick(member, reason=reason)
#     try:
#         await ctx.send("Kicked " + str(member) + " for " + reason, delete_after=10)
#     except TypeError:
#         pass


# @bot.command()
# @commands.has_permissions(ban_members=True)
# async def ban(ctx, member: discord.Member, *, reason: str = None):
#     await discord.Member.ban(member, reason=reason)
#     if reason == None:
#         await ctx.send("Banned " + str(member))
#     else:
#         await ctx.send("Banned " + str(member) + " for " + reason, delete_after=10)


bot.add_cog(General(bot))

# not to be exposed ----------
bot.run("TOKEN")
