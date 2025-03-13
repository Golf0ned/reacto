from collections import Counter, deque

import yaml
import discord

MESSAGE_QUEUE_FILE = 'messages.yaml'

def load_file():
    try: 
        with open(MESSAGE_QUEUE_FILE, 'r') as file:
            return yaml.safe_load(file) or []
    except FileNotFoundError:
        return []

class NameLookUp(discord.ui.Modal):
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        mappings = load_file()
        global_name = None
        if not interaction.message:
            await interaction.followup.send("No message indicated")
            return

        for mapping in mappings:
            if interaction.message.id in mapping:
                global_name = mapping[interaction.message.id]
                break

        if not global_name:
            await interaction.followup.send("No name found for this message", ephemeral=True)
            return

        await interaction.followup.send(f"The user {global_name} called reacto on this message")
