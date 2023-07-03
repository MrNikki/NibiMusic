import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "28974500"))
API_HASH = getenv("API_HASH", "cb2f5b366e83c79539f6b139186aa00d")
BOT_USERNAME = getenv("BOT_USERNAME", "LinuxMusicBot")
BOT_TOKEN = getenv("BOT_TOKEN", "6292589083:AAGH0_QAcn0xEDhE8PEk6M89JwZiL_mEucY")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "TheBothub")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "BlackWorldMF")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TheFunkyFox")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQCDeCJ0UWzhaI_NC45zPht4M9zhz0qQy4dRTZJ2KWIEB8nTSeN_z0ZZd3Zr6k4fVx5JWLQ7IKRsrSZXq72tCYE_KI9vyQPDd5NFiULKw35fLfwJfv4gsnGcu0E4oy8j8EcXNklMNgrUW_LfGOAfBjkYQhHF0tThaWob442Gs0v9g2fHyi4KW9NxX1IKPtrG43WyM0Ry9JchSZKYsD-OAbRRaFwugiV59kCqKuCAduQvyqpcKDcpxjUO6V0NxyHIbWHzQCrsRHqor4YNCrSxjLxdaBgtAgygwsuOJP_kkmEMIHTZAIWxC3J10vh_Ng64m6igEDEes2ktO6QHZRefDWLIeOoT4wA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6190680150").split()))
aiohttpsession = aiohttp.ClientSession()
