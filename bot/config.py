import os
class config:
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5806016246:AAEocrUT_h8ZkM3dfqFWcNJsUk1_V_5uF9U")
    APP_ID = os.environ.get('APP_ID', "7880210")
    API_HASH = os.environ.get('API_HASH', "1bb4b2ff1489cc06af37cba448c8cce9")
    DATABASE_URL = os.environ.get('DATABASE_URL', "mongodb+srv://premiumbot:premiumbot@cluster0.5siafyp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")    
    SUDO_USERS = os.environ.get('SUDO_USERS', "1113630298")
    SUPPORT_CHAT_LINK = "t.me/MKS_REQUESTGROUP"
    DOWNLOAD_DIRECTORY = "./downloads/"
    PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""


class BotCommands:
  Authorize = ['auth', 'start']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  Channelmyanmar = ['cm']
  Mmsubtitles = ['mmsub']
  Vidsearch = ['vid']
  Linkgen = ['cmgen']
  Logo = ['logo']
  Javgen = ['javgen']
  Test = ['test']
class Messages:
    
    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    START = "Initiating Upload "
    DOWNLOADING = " 🥷 Initiating Download"
    DOWNLOADED_SUCCESSFULLY = "📤 **mmsub.co...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    
