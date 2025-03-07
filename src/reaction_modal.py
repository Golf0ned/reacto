from collections import Counter

import discord

from config import Config


EMOJIS = Config.emojis

EMOJI_COUNTS = { c: len(EMOJIS[c]) for c in EMOJIS }


class ReactionModal(discord.ui.Modal):
    
    def __init__(self, message):
        super().__init__(title="Add Reaction")
        self.message = message

        self.add_item(discord.ui.InputText(
            label="Text (A-Z, 0-9, !?, space)",
            min_length=1,
            max_length=20,
        ))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        input = self.children[0].value.lower()

        # Ignore if message has already been reacted to
        if self.message.reactions:
            await interaction.followup.send("Message has already been reacted to.", ephemeral=True)
            return

        # Check if input is valid
        if not input or not all(c.isalnum() or c in "!? " for c in input):
            await interaction.followup.send("Invalid input. Please provide an alphanumeric string with no spaces.", ephemeral=True)
            return

        # Make sure there's enough emojis to react with
        input_count = Counter(input)
        for c in input_count:
            if input_count[c] > EMOJI_COUNTS[c]:
                await interaction.followup.send(f"Not enough emojis for {c} (There's {EMOJI_COUNTS[c]} {c}'s).", ephemeral=True)
                return

        # All clear, add reactions
        cur_count = {}
        for c in input:
            await self.message.add_reaction(EMOJIS[c][cur_count.get(c, 0)])
            cur_count[c] = cur_count.get(c, 0) + 1
