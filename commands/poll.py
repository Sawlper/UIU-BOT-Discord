from discord.ext import commands
from discord import app_commands
import discord

class Poll(commands.Cog):
    
    def __init__(self, client: commands.Bot):
        self.client = client
        self.poll_emojis = [
            '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟'
        ]

    @app_commands.command(name="poll", description="Create a simple poll for up to 10 options.")
    @app_commands.describe(
        question="The question to ask.",
        option1="Option 1.", option2="Option 2.", option3="Option 3 (Optional).",
        option4="Option 4 (Optional).", option5="Option 5 (Optional).", option6="Option 6 (Optional).",
        option7="Option 7 (Optional).", option8="Option 8 (Optional).", option9="Option 9 (Optional).",
        option10="Option 10 (Optional)."
    )
    async def create_poll(self, interaction: discord.Interaction, question: str, 
                          option1: str, option2: str, option3: str = None, option4: str = None, 
                          option5: str = None, option6: str = None, option7: str = None, 
                          option8: str = None, option9: str = None, option10: str = None):
        
        await interaction.response.defer()

        options = [o for o in [option1, option2, option3, option4, option5, option6, option7, option8, option9, option10] if o is not None]
        
        if len(options) < 2:
            await interaction.followup.send("Please provide at least two options for the poll!", ephemeral=True)
            return
        
        if len(options) > len(self.poll_emojis):
            await interaction.followup.send(f"Sorry, I only have {len(self.poll_emojis)} emojis available for this poll.", ephemeral=True)
            return

        
        options_text = "\n".join(f"{self.poll_emojis[i]} {opt}" for i, opt in enumerate(options))
        
        embed = discord.Embed(
            title=" ****`Poll Created`****",
            description=f"**{question}**\n\n{options_text}",
            color=discord.Color.blue()
        )
        embed.set_footer(text=f"Poll started by {interaction.user.display_name}")
        
        poll_message = await interaction.followup.send(embed=embed)
        
        for i in range(len(options)):
            await poll_message.add_reaction(self.poll_emojis[i])


async def setup(client: commands.Bot):
    await client.add_cog(Poll(client))