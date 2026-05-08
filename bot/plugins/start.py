from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.screenshotbot import ScreenShotBot

@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):
    txt = f"""
<b>╭━━━〔 📸 ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ʙᴏᴛ 〕━━━╮

👋 ʜᴇʏ {m.from_user.mention}

✨ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴀᴅᴠᴀɴᴄᴇᴅ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ

📸 ɪ ᴄᴀɴ ᴄʀᴇᴀᴛᴇ ʜɪɢʜ Qᴜᴀʟɪᴛʏ ꜱᴄʀᴇᴇɴꜱʜᴏᴛꜱ
ғʀᴏᴍ ʏᴏᴜʀ ᴠɪᴅᴇᴏꜱ ɪɴꜱᴛᴀɴᴛʟʏ ⚡

━━━━━━━━━━━━━━━━━━

⚡ ꜰᴀꜱᴛ • 🎞️ Qᴜᴀʟɪᴛʏ • 🚀 ꜱɪᴍᴘʟᴇ

━━━━━━━━━━━━━━━━━━

📌 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ:
➤ ꜱᴇɴᴅ ᴀɴʏ ᴠɪᴅᴇᴏ ғɪʟᴇ ᴏʀ ʟɪɴᴋ
➤ ʙᴏᴛ ᴡɪʟʟ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴄʀᴇᴇɴꜱʜᴏᴛꜱ

📖 ɴᴇᴇᴅ ʜᴇʟᴘ? ᴜꜱᴇ /help ᴄᴏᴍᴍᴀɴᴅ

━━━━━━━━━━━━━━━━━━
<blockquote>
⍟ ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/PrimeXBots'>ᴘʀɪᴍᴇXʙᴏᴛꜱ</a> ⍟
</blockquote></b>"""

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("〄 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/PrimeXBots")],
        [InlineKeyboardButton("✪ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ✪", url="https://t.me/Prime_Support_group"),
         InlineKeyboardButton("〄 ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ 〄", url="https://t.me/PrimeCineZone")],
        [InlineKeyboardButton("✧ ᴄʀᴇᴀᴛᴏʀ ✧", url="https://t.me/Prime_Nayem")]
    ])

    await m.reply_text(text=txt, quote=True, disable_web_page_preview=True, reply_markup=buttons)
