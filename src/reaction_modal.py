import discord

class ReactionModal(discord.ui.Modal):
    
    def __init__(self, message):
        super().__init__(title="Add Reaction")
        self.message = message

        self.add_item(discord.ui.InputText(label="Reaction (alphanumeric with spaces)"))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        modal_input = self.children[0].value
        # TODO: replace the hardcoded array with modal_input, and map to emojis
        for c in ["🇱", "🇲", "🇦", "🇴"]:
            await self.message.add_reaction(c)
