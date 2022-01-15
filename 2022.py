# Its been 2 years,
# How has it been this long.

import os; import discord; from discord.ext import commands; from discord_slash import SlashCommand, SlashContext; from dotenv import load_dotenv;bot = commands.Bot(command_prefix="RipMessageIntents", intents=discord.Intents.default(), help_command=None); slash = SlashCommand(bot); load_dotenv(); exec('@slash.slash(name="rocket")\nasync def rocket(ctx: SlashContext):\n    await ctx.send(embed=discord.Embed(title="WEEEEEE 🔥🔥🚀 (but in 2022)", colour=discord.Colour.blurple(), description="Wow! You made it! Check out some other amazing bots such as... oh wait, its 2022, they all died :("))'); exec('@bot.event\nasync def on_ready():\n    await slash.sync_all_commands()'); bot.run(os.environ.get("token"))
