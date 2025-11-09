import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN') 

# Basic bot info
BOT_NAME = "UIU_BOT"
BOT_VERSION = "1.0.0"
BOT_OWNER = "sawlper"
BOT_DESCRIPTION = "Your own soft place for notices, updates, and community info."
