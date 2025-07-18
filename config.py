# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25013204")

API_HASH = os.environ.get("API_HASH", "771c072b4ae280c10508d636b494b285")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8060557109:AAEOK1Kp1ecuFjgbln9ViRp7rs_w-Sj0QTU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "KeyLink_bot") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Keylink")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://damiruimo:ABVvGpyR8fVe7nar@x-kevin.83vo1.mongodb.net/")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '8046796637').split()]

PORT = os.environ.get("PORT", "8000")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
