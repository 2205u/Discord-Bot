import discord
from discord.ext import commands
from datetime import datetime

Client = discord.Client()  
bot = commands.Bot(command_prefix=">")
  # TODO: add variable prefix

@bot.command()
@commands.has_permissions(administrator=True)
async def disable(ctx, *, extn = None):
  if extn == None:
    await ctx.send("Choose any of the following extensions to disable: General, Moderation, Fun. [Case sensitive]")
  elif extn == "General" or extn == "Moderation" or extn == "Fun":
    bot.unload_extension("cogs." + extn)
    await ctx.send("Disabled the " + extn + " extension")
  else:
    await ctx.send("The extension you have entered does not exist. Please note that the names of the extensions are case sensitive.")

@bot.command()
@commands.has_permissions(administrator=True)
async def enable(ctx, *, extn = None):
  if extn == None:
    await ctx.send("Choose any of the following extensions to disable: General, Moderation, Fun. [Case sensitive]")
  elif extn == "General" or extn == "Moderation" or extn == "Fun":
    bot.load_extension("cogs." + extn)
    await ctx.send("Enabled the " + extn + " extension"
  else:
    await ctx.send("The extension you have entered does not exist. Please note that the names of the extensions are case sensitive.")

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
bot.run("NTg4MDI3OTU0NjU1Nzg5MTEx.XP_KUA.hfVm5j4a-g5H0U7ugehGs1i1yhQ")
