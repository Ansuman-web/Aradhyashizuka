from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**𝙒𝙀𝙇 𝘾𝙊𝙈𝙀 𝙏𝙊 𝘼𝙍𝘼𝘿𝙃𝙔𝘼 𝙍𝙀𝙋𝙊

𝘽𝙎𝘿𝙆 𝙍𝙀𝙋𝙊 𝙇𝙀𝙉𝘼 𝙃𝘼𝙄 𝙏𝙊𝙃 𝙉𝙄𝘾𝙃𝙀 𝙍𝙀𝙋𝙊 𝘽𝙐𝙏𝙏𝙊𝙉 𝙋𝙀 𝘾𝙇𝙄𝘾𝙆 𝙆𝘼𝙍𝙆𝙀 𝙇𝙀 𝙅𝘼.

𝙇𝙄𝙁𝙀 𝙈𝘼𝙄𝙉 𝙆𝙐𝘾𝙃 𝙉𝘼𝙃𝙄 𝙆𝘼𝙍 𝙋𝘼𝙔𝙀𝙂𝘼 𝘽𝙎𝘿𝙆 𝘿𝙐𝙎𝙍𝙊 𝙆𝘼 𝘾𝙊𝙋𝙔 𝙆𝘼𝙍𝙆𝙀 .

𝘾𝙃𝘼𝙇 𝙈𝘼𝘿𝘼𝙍𝘾𝙃𝙊𝘿 𝙇𝙀 𝙅𝘼𝘼 𝙍𝙀𝙋𝙊 

𝙕𝙀𝙐𝙎 𝙏𝙀𝙍𝘼 𝙋𝘼𝙋𝘼 𝙃𝘼𝙄 𝙈𝘼𝘿𝘼𝙍𝘾𝙃𝙊𝘿 

[𝙏𝙀𝙍𝙀 𝙋𝘼𝙋𝘼](https://t.me/unbornedvillian)

𝙈𝘼𝘿𝙀 𝘽𝙔 ➛ [ʙᴏᴛ ᴄʜᴀᴍʙᴇʀ](https://t.me/ll_botchamber_ll)**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴇʟᴘ •", url="https://t.me/ll_botchamber_ll"),
          InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/unbornedvillian"),
          ],
               [
                InlineKeyboardButton("• ɴᴇᴛᴡᴏʀᴋ •", url=f"https://t.me/ll_botchamber_ll"),
],
[
InlineKeyboardButton("• ʀᴇᴘᴏ •", url=f"https://github.com/Ansuman-web/ZEUSFAKEREPO.git"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/7575371e35d91363554ab-c01e8fa76f06533ff9.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
