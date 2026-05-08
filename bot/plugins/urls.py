from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.utils import Utilities
from bot.screenshotbot import ScreenShotBot
from bot.config import Config
import datetime

@ScreenShotBot.on_message(filters.private & (filters.video | filters.document | filters.text) & filters.incoming)
async def _(c, m):
    # এডিট করা মেসেজ ইগনোর করা
    if m.edit_date:
        return

    # ফাইল চেক
    if m.media:
        if not Utilities.is_valid_file(m):
            return
    else:
        if not Utilities.is_url(m.text):
            return

    snt = await m.reply_text("Processing... Please wait!", quote=True)

    # ফাইল লিঙ্ক জেনারেট করা
    file_link = Utilities.generate_stream_link(m) if m.media else m.text

    duration = await Utilities.get_duration(file_link)
    if isinstance(duration, str):
        await snt.edit_text("😟 Sorry! I cannot open the file.")
        return

    btns = Utilities.gen_ik_buttons()
    if duration >= 600:
        btns.append([InlineKeyboardButton("Generate Sample Video!", callback_data="smpl")])

    await snt.edit_text(
        text=f"Total duration: `{datetime.timedelta(seconds=duration)}` (`{duration}s`)",
        reply_markup=InlineKeyboardMarkup(btns),
    )
