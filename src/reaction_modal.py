from collections import Counter

import discord

from config import Config


EMOJIS = Config.emojis

EMOJI_COUNTS = { c: len(EMOJIS[c]) for c in EMOJIS }


class ReactionModal(discord.ui.Modal):
    
    def __init__(self, message):
        super().__init__(title="Add Reaction")
        self.message = message

        self.add_item(discord.ui.InputText(label="Reaction (alphanumeric with spaces)"))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        input = self.children[0].value

        # Check if input is valid
        if not input or not input.isalnum():
            await interaction.followup.send("Invalid input. Please provide an alphanumeric string with no spaces.")
            return

        # Make sure there's enough emojis to react with
        input_count = Counter(input)
        for c in input_count:
            if input_count[c] > EMOJI_COUNTS[c]:
                await interaction.followup.send(f"Not enough emojis for {c} (There's {EMOJI_COUNTS[c]} {c}'s).")
                return

        # All clear, add reactions
        cur_count = {}
        for c in modal_input:
            cur_emoji_num = cur_count.get(c, 0) + 1 # 1 indexed lmao
            await self.message.add_reaction()
            cur_count[c] = cur_emoji_num
