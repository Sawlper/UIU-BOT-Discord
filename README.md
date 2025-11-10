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
  <img src="https://github.com/Sawlper/UIU-BOT-Discord/blob/0d5e53a8c7b6cb22f8cd807fa0942ba6f2b564dd/Asset/CommandsPVWgifs/Screenshot%202025-11-10%20022703.png" width="28%">
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
|  General  | `/ping`, `/about`, `/help` (without any admin perms) | Bot latency, Info about the bot & guide for all other commands |
|  Academic | `/notices`, `/calendar` (without any admin perms)| Shows UIU latest notices and the calender for all students      |
|  Admin    | `/setup`, `/stop_notices`, `/poll` ( admin perms are needed) | Set auto post notices, stop posting notices & polls   |



## ⚡ Highlights

- <img src="https://github.com/Sawlper/UIU-BOT-Discord/blob/485ba68d207d39fb67eb55626f3b570354ce355b/Asset/Icon%20%20gifs/Sync.gif" width="20" height="20" valign="middle"/>  **Automatic notice updates**  async background fetching  
- <img src="https://github.com/Sawlper/UIU-BOT-Discord/blob/485ba68d207d39fb67eb55626f3b570354ce355b/Asset/Icon%20%20gifs/Api.gif" width="20" height="20" valign="middle"/>   **Slash commands**  modern UX for all users  
- <img src="https://github.com/Sawlper/UIU-BOT-Discord/blob/485ba68d207d39fb67eb55626f3b570354ce355b/Asset/Icon%20%20gifs/Setup.gif" width="25" height="25" valign="middle"/> **Admin tools**  setup & automation  
- <img src="https://github.com/Sawlper/UIU-BOT-Discord/blob/485ba68d207d39fb67eb55626f3b570354ce355b/Asset/Icon%20%20gifs/Sustainability.gif" width="25" height="25" valign="middle"/> **Lightweight** JSON persistence, no DB needed



<h1 align="center"> Command Previews</h1>

<div align="center">
  <img src="https://github.com/Sawlper/UIU-BOT-Discord/blob/485ba68d207d39fb67eb55626f3b570354ce355b/Asset/CommandsPVWgifs/bothelp.gif" width="49%" style="margin-right: 10px;">
  <img src="https://github.com/Sawlper/UIU-BOT-Discord/blob/485ba68d207d39fb67eb55626f3b570354ce355b/Asset/CommandsPVWgifs/dcsetup.gif" width="49%">
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




<p align="center">
  <a href="https://discord.com/api/oauth2/authorize?client_id=1434163768488890549&permissions=8&scope=bot%20applications.commands">
    <img src="https://img.shields.io/badge/INVITE%20UIU%20BOT-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Invite UIU BOT">
  </a>
</p>




