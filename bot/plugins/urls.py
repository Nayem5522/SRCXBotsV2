import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.utils import Utilities
from bot.screenshotbot import ScreenShotBot
from bot.config import Config

@ScreenShotBot.on_message(
    filters.private
    & (filters.text | filters.video | filters.document)
    & filters.incoming
)
async def _(c, m):

    # এডিট করা মেসেজ ইগনোর করা (Pyrogram V2 এর নিয়ম অনুযায়ী)
    if m.edit_date:
        return

    # ফাইল বা ইউআরএল ভ্যালিডেশন
    if m.media:
        if not Utilities.is_valid_file(m):
            return
    else:
        if not Utilities.is_url(m.text):
            return

    snt = await m.reply_text(
        "Hi there, Please wait while I'm getting everything ready to process your request!",
        quote=True,
    )

    # স্ট্রিমিং লিঙ্ক জেনারেশন
    if m.media:
        file_link = Utilities.generate_stream_link(m)
    else:
        file_link = m.text

    duration = await Utilities.get_duration(file_link)
    
    # যদি ফাইল খুলতে সমস্যা হয়
    if isinstance(duration, str):
        await snt.edit_text("😟 Sorry! I cannot open the file.")
        # লগ চ্যানেলে ফরওয়ার্ড করা (যদি Config এ দেওয়া থাকে)
        if Config.LOG_CHANNEL:
            try:
                log = await m.forward(Config.LOG_CHANNEL)
                await log.reply_text(duration, quote=True)
            except:
                pass
        return

    # বাটন জেনারেট করা
    btns = Utilities.gen_ik_buttons()

    # যদি ভিডিও ১০ মিনিটের বেশি হয় তবে স্যাম্পল ভিডিওর বাটন যোগ করা
    if duration >= 600:
        btns.append([InlineKeyboardButton("Generate Sample Video!", callback_data="smpl")])

    await snt.edit_text(
        text=f"Choose one of the options.\n\nTotal duration: `{datetime.timedelta(seconds=duration)}` (`{duration}s`)",
        reply_markup=InlineKeyboardMarkup(btns),
    )
