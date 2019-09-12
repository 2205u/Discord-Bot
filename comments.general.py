# imports -------------------------
import discord
from discord.ext import commands

from datetime import datetime
# ---------------------------------


Client = discord.Client()  # connection b/w client and discord
bot = commands.Bot(command_prefix="!")  # sets bot prefix as ">" # TODO: add variable prefix
# TODO: add cogs

"""COGS: General"""
@bot.event  # registers/detects events
async def on_ready():  # registers after the bot is ready to be used
    drpname = "for >manual."  # Discord Rich Presence variable to be used later
    # sets the DRP to the variable and activity to watching right about here V
    activity = discord.Activity(name=drpname, type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity, status=discord.Status.do_not_disturb)  # sets bot status
    print("DRP: Watching " + drpname)  # prints DRP activity to console
    print("Bot deployed.")  # prints to console when bot is ready to be used


@bot.command()  # function name is the command name basically; removed need of excess code to call commands
async def manual(ctx):  # ctx is used for sending stuff
    # creates embed named embed (creative, ik). options are self-explanatory
    embed = discord.Embed(title="Help on Byte", description="All the commands added so far", color=0xdc322f,
                          timestamp=datetime.utcfromtimestamp(1559025608))
    embed.add_field(name=">ping", value="Sens back 'Pong!'")  # adds field with options which are self-explanatory
    embed.add_field(name=">pingms", value="Sends back numerical latency")
    embed.add_field(name=">repeat", value="Repeats everything after '>repeat'")
    embed.add_field(name=">purge", value="Deletes specified number of messages")
    embed.add_field(name=">poke", value="More useless than SUPW")
    # embed.add_field(name=">kick", value="Kicks the mentioned user") change to
    # embed.add_field(name=">ban", value="Bans the mentioned user") mod only class
    embed.set_footer(text="Byte Alpha", icon_url="https://cdn.discordapp.com/attachments/497783794091294740/"
                                                 "582817787974516763/abstract-abstract-painting-art-2230796.jpg")

    await ctx.send(content=None, embed=embed)  # sends the embed


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!", delete_after=10)  # delete_after deletes the message after the {value} seconds pass


@bot.command()
async def pingms(ctx):
    latency = bot.latency  # bot.latency returns the numerical latency
    await ctx.send(latency, delete_after=10)


@bot.command()
async def repeat(ctx, *, message):
    await ctx.send(message, delete_after=10)


@bot.command(pass_context=True)
async def poke(ctx, member: discord.Member):
    member = member.mention  # mentions the member; full version is discord.Member.mention
    await ctx.send(ctx.message.author.mention + " poked " + member)

""" Cogs:MOD ONLY """
@bot.command(pass_context=True,)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, number):
    number = int(number)
    if number > 99 or number < 1:
        await ctx.send("I can only delete messages within a range of 1 - 99", delete_after=10)
    else:
        mgs = []  # creates empty list for the messages to be contained
        number = int(number)
        # sets the channel for the message to send, to the channel in which the command was sent
        channel = ctx.message.channel
        # gets {number} amount of messages
        async for x in discord.abc.Messageable.history(channel, limit=int(number+1)):
            mgs.append(x)
        for y in mgs:
            await discord.Message.delete(y)  # bye messages
        await ctx.send(str(number) + ' Messages deleted!', delete_after=10)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason: str = None):
    await discord.Member.kick(member, reason=reason)
    try:
        await ctx.send("Kicked " + str(member) + " for " + reason, delete_after=10)
    except TypeError:
        pass


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason: str = None):
    await discord.Member.ban(member, reason=reason)
    if reason == None:
        await ctx.send("Banned " + str(member))
    else:
        await ctx.send("Banned " + str(member) + " for " + reason, delete_after=10)


# not to be exposed ----------
bot.run("NTg4MDI3OTU0NjU1Nzg5MTEx.XP_KUA.hfVm5j4a-g5H0U7ugehGs1i1yhQ")  # connects to the bot via this token
