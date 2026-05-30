from os import environ 

class Config:
    API_ID = environ.get("API_ID", "38059343")
    API_HASH = environ.get("API_HASH", "551bdd4028d523579c499e4821ae3016")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8647959631:AAG0SBqjC5hDaC0WEUAVEHUdcD31VsAloTo") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Forward:zhwJ1EEz5RNYCun6@cluster0.tmou4ig.mongodb.net/?appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
