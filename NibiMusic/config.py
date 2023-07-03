import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "13831288"))
API_HASH = getenv("API_HASH", "0d4c67b8d1bef020475434abc394ac4c")
BOT_USERNAME = getenv("BOT_USERNAME", "LinuxMusicBot")
BOT_TOKEN = getenv("BOT_TOKEN")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "TheBothub")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "BlackWorldMF")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TheFunkyFox")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6190680150").split()))
aiohttpsession = aiohttp.ClientSession()
