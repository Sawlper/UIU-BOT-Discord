<h1 align="center">
  <b>UIU BOT</b>
</h1>

<p align="left">
  Smart, minimal & student-friendly Discord bot built for <b>United International University (UIU)</b>.  
  Stay updated with <b>notices</b>, <b>polls</b>, and <b>academic info</b> all in real time.
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Discord-Bot-5865F2?style=for-the-badge&logo=discord&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Status-Active-27ae60?style=for-the-badge">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1145898013846468618/1299970218761418783/uiu_banner.gif" width="85%">
</p>

<p align="center"><i> Always in sync with your campus updates.</i></p>



##  Quick Setup

```bash
git clone https://github.com/Sawlper/UIU-BOT-Discord.git
cd UIU-BOT
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
````

**Create a `.env` file:**

```env
DISCORD_TOKEN=your_discord_bot_token
DISCORD_CLIENT_ID=your_bot_client_id
```

**Run the bot:**

```bash
python main.py
```



##  Commands Overview

| Category                                                                                   | Commands                           | Description                                  |
| ------------------------------------------------------------------------------------------ | ---------------------------------- | -------------------------------------------- |
| <img src="https://cdn.discordapp.com/emojis/1107423976077543424.gif" width="20"/> General  | `/ping`, `/about`, `/help`         | latency, Info & guide for all other commands |
| <img src="https://cdn.discordapp.com/emojis/1078349875366254663.gif" width="20"/> Academic | `/notices`, `/calendar`            | UIU notices both auto and manual & dates     |
| <img src="https://cdn.discordapp.com/emojis/1078350042043850853.gif" width="20"/> Admin    | `/setup`, `/stop_notices`, `/poll` | Manage posts, stop posting notices & polls   |



## ⚡ Highlights

- <img src="https://github.com/Sawlper/Minimal-Kepper/blob/e277bd7e8efec474735af5d5d48723b1c72b894e/Icon%20Gifs/Sync.gif" width="20" height="20" valign="middle"/>  **Automatic notice updates**  async background fetching  
- <img src="https://github.com/Sawlper/Minimal-Kepper/blob/ce8c66daaa9a04685e0e9218b35399bd07cb3d76/Icon%20Gifs/Api.gif" width="20" height="20" valign="middle"/>   **Slash commands**  modern UX for all users  
- <img src="https://github.com/Sawlper/Minimal-Kepper/blob/ce8c66daaa9a04685e0e9218b35399bd07cb3d76/Icon%20Gifs/Setup.gif" width="25" height="25" valign="middle"/> **Admin tools**  setup & automation  
- <img src="https://github.com/Sawlper/Minimal-Kepper/blob/ce8c66daaa9a04685e0e9218b35399bd07cb3d76/Icon%20Gifs/Sustainability.gif" width="25" height="25" valign="middle"/> **Lightweight** JSON persistence, no DB needed



<h1 align="center"> Command Previews</h1>

<div align="center">
  <img src="https://github.com/Sawlper/Minimal-Kepper/blob/dfba9b8e2abcbcb236d717ee0a626bfc5390344d/Gifs/bothelp.gif" width="49%" style="margin-right: 10px;">
  <img src="https://github.com/Sawlper/Minimal-Kepper/blob/dfba9b8e2abcbcb236d717ee0a626bfc5390344d/Gifs/dcsetup.gif" width="49%">
</div>

<p align="center">
  <sub>
    <b>/help</b> help menu showing all available commands. &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <b>/setup</b> Automatically fetches the latest UIU notices.
  </sub>
</p>


<h3 align="center"> Powered By</h3>

<div align="center">

<table>
  <tr>
    <th>Component</th>
    <th>Library</th>
  </tr>
  <tr>
    <td align="center">Discord API</td>
    <td align="center"><a href="https://github.com/Rapptz/discord.py">discord.py v2</a></td>
  </tr>
  <tr>
    <td align="center">Web Scraping</td>
    <td align="center">requests, beautifulsoup4</td>
  </tr>
  <tr>
    <td align="center">Config</td>
    <td align="center">python-dotenv</td>
  </tr>
  <tr>
    <td align="center">Async</td>
    <td align="center">asyncio, discord.ext.tasks</td>
  </tr>
</table>

</div>







