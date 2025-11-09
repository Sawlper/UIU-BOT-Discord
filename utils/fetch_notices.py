import requests
from bs4 import BeautifulSoup
import asyncio

URL = "https://www.uiu.ac.bd/notice/"

async def fetch_notices():
    """
    Scrapes the UIU notice board for the latest notices.
    This function is now purely responsible for data retrieval, 
    running in a separate thread to avoid blocking the bot.
    """
    loop = asyncio.get_running_loop()
    page = await loop.run_in_executor(None, lambda: requests.get(URL))

    try:
        page.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
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