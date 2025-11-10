# commands/setup.py

from discord.ext import commands
from discord import app_commands
import discord
import json
import os

class Setup(commands.Cog):
    
    def __init__(self, client: commands.Bot):
        self.client = client
        self.memory_file = "data/notices_memory.json"
    

    def _load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"servers": {}}

    def _save_memory(self, memory_data):
        with open(self.memory_file, 'w') as f:
            json.dump(memory_data, f, indent=4)
    
    @app_commands.command(name="setup", description="Set the channel for automatic notice updates")
    @app_commands.describe(channel="The channel to post new notices in")
    @app_commands.default_permissions(administrator=True)
    async def setup_channel(self, interaction, channel: discord.TextChannel):
        
        await interaction.response.defer(ephemeral=True)
        
        server_id = str(interaction.guild.id)
        memory = self._load_memory()
        
        if server_id not in memory["servers"]:
            memory["servers"][server_id] = {"notice_channel_id": None, "seen_notices": []}
            
        memory["servers"][server_id]["notice_channel_id"] = channel.id
        
        self._save_memory(memory)
        
        await interaction.followup.send(f"Success! I will now post all new notices in {channel.mention}.")

    
    @app_commands.command(name="stop_notices", description="Stop automatic notice updates in this server")
    @app_commands.default_permissions(administrator=True)
    async def stop_notices(self, interaction):
        
        server_id = str(interaction.guild.id)
        memory = self._load_memory()
        
        if server_id in memory["servers"] and memory["servers"][server_id].get("notice_channel_id"):
            memory["servers"][server_id]["notice_channel_id"] = None
            self._save_memory(memory)
            await interaction.response.send_message("Success! I will no longer post automatic notices in this server.")
        else:
            await interaction.response.send_message("I am not currently posting notices in this server anyway.")


async def setup(client: commands.Bot):
    await client.add_cog(Setup(client))