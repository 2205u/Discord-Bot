import discord
from discord.ext import commands

from datetime import datetime

Client = discord.Client()  
bot = commands.Bot(command_prefix=">")
  # TODO: add variable prefix

bot.load_extension("cogs.General")

bot.run("NTg4MDI3OTU0NjU1Nzg5MTEx.XP_KUA.hfVm5j4a-g5H0U7ugehGs1i1yhQ")
