from os import environ 

class Config:
    API_ID = environ.get("API_ID", "21102617")
    API_HASH = environ.get("API_HASH", "31de0d24a6b8048c48730bc420f4b70c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7651811990:AAEMogQsWn0zAei8SB5SdT175Oo67-hSsSw") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6300568870').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
