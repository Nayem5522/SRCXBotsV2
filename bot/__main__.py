# bot/__main__.py আপডেট করুন
import logging
from .screenshotbot import ScreenShotBot
from .config import Config
from keep_alive import keep_alive # নতুন ইমপোর্ট

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG if Config.DEBUG else logging.INFO)
    logging.getLogger("pyrogram").setLevel(
        logging.INFO if Config.DEBUG else logging.WARNING
    )
    
    # পোর্ট ওপেন রাখার জন্য সার্ভার চালু করুন
    keep_alive()
    
    ScreenShotBot().run()
