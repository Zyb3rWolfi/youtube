import nextcord
from nextcord.ext import commands
import os

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

cogs = [

    "cogs.levels",
]

@bot.event
async def on_ready():

    print("Bot is ready")

if __name__ == "__main__":

    for cog in cogs:
        bot.load_extension(cog)

bot.run(os.environ.get("TOKEN"))