import discord
from discord.ext import commands

from datetime import datetime

Client = discord.Client()  
bot = commands.Bot(command_prefix=">")
  # TODO: add variable prefix

@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx):
  await ctx.send("Reloading bot.")
  await ctx.send("Unloading General")
  bot.unload_extension("cogs.General")
  await ctx.send("Unloading Moderation")
  bot.unload_extension("cogs.Moderation")
  await ctx.send("Unloading Fun")
  bot.unload_extension("cogs.Fun")
  await ctx.send("Extensions fully unloaded. Reloading.")
  bot.load_extension("cogs.General")
  bot.load_extension("cogs.Moderation")
  bot.load_extension("cogs.Fun")
  await ctx.send("Reloaded. Status: fully functional.")

bot.load_extension("cogs.General")
bot.load_extension("cogs.Moderation")
bot.load_extension("cogs.Fun")

bot.run(TOKEN)
