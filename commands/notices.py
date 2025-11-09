from discord.ext import commands, tasks
from discord import app_commands
import discord
import requests
from bs4 import BeautifulSoup
import json
import os

class Notices(commands.Cog):
    
    def __init__(self, client: commands.Bot):
        self.client = client
        self.memory_file = "data/notices_memory.json"
        self.check_notices_loop.start()

    
    def _load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"servers": {}}

    
    def _save_memory(self, memory_data):
        with open(self.memory_file, 'w') as f:
            json.dump(memory_data, f, indent=4)

    
    async def fetch_notices(self):
        URL = "https://www.uiu.ac.bd/notice/"
        try:
            page = requests.get(URL)
            page.raise_for_status() 
        except requests.exceptions.RequestException as e:
            return [] 

        soup = BeautifulSoup(page.content, "html.parser")
        all_notices = soup.find_all("div", class_="details")
        
        results = []
        for notice in all_notices[:5]: 
            title_tag = notice.find("div", class_="title").find("a")
            if title_tag:
                title_text = title_tag.text.strip()
                title_link = title_tag['href']
                if not title_link.startswith("http"):
                    title_link = "https://www.uiu.ac.bd" + title_link
                results.append( (title_text, title_link) )
        
        return results

    
    @app_commands.command(name="notices", description="Get the latest 3 UIU notices")
    async def notices(self, interaction):
        
        await interaction.response.defer()

        notices_list = await self.fetch_notices()

        if not notices_list:
            await interaction.followup.send("Sorry, I couldn't find any notices or the website is down.")
            return

        embed = discord.Embed(
            title="UIU Latest Notices",
            description="Here are the top 3 notices from the board.",
            color=0xCCCCCC,
        )
        
        embed.set_thumbnail(url="https://i.ibb.co.com/ZphvQT2g/meme-20251103070415-139132.gif")

        for (title, link) in notices_list[:3]:
            embed.add_field(name=title, value=f"[Click to Read]({link})", inline=False)
        
        await interaction.followup.send(embed=embed)

    
    @tasks.loop(minutes=1)
    async def check_notices_loop(self):
        
        latest_notices = await self.fetch_notices()
        if not latest_notices:
            return
            
        memory = self._load_memory()
        
        for server_id, server_data in memory["servers"].items():
            
            channel_id = server_data.get("notice_channel_id")
            if not channel_id:
                continue
            
            channel = self.client.get_channel(channel_id)
            if not channel:
                continue
            
            seen_notices = server_data.get("seen_notices", [])
            new_notices_found_for_this_server = False
            
            for (title, link) in reversed(latest_notices):
                if link not in seen_notices:
                    
                    new_notices_found_for_this_server = True
                    
                    new_embed = discord.Embed(
                        title=f"New UIU Notice: {title}",
                        description="A new notice has been posted on the UIU website.",
                        color=0xCCCCCC,
                        url=link
                    )
                    new_embed.set_thumbnail(url="https://i.ibb.co.com/ZphvQT2g/meme-20251103070415-139132.gif")
                    new_embed.add_field(name="Click to Read", value=f"[Read the full notice here]({link})", inline=False)
                    
                    try:
                        await channel.send(embed=new_embed)
                        seen_notices.append(link)
                    except Exception as e:
                        print(f"Error posting to Discord channel {channel_id}: {e}")

            if new_notices_found_for_this_server:
                memory["servers"][server_id]["seen_notices"] = seen_notices
        
        self._save_memory(memory)

    
    @check_notices_loop.before_loop
    async def before_check_notices_loop(self):
        await self.client.wait_until_ready()


async def setup(client: commands.Bot):
    await client.add_cog(Notices(client))