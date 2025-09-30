import discord

from config import Config
from src.reaction_modal import ReactionModal


TOKEN = Config.secrets["discord"]["token"]

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.message_command(name="Message React")
async def react(ctx, message):
    modal = ReactionModal(message)
    await ctx.send_modal(modal)

@bot.message_command(name="Tomato")
async def react(ctx, message):
    await message.add_reaction(":tomato:")

bot.run(TOKEN)
