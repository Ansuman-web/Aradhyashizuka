from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ᴛɢ ɴᴀᴍᴇ - ᴢᴇᴜꜱ ʙʟᴏᴏᴅʟɪɴᴇ 
│├ʀᴇᴀʟ ɴᴀᴍᴇ - 🙂🖕
│├─────────────────╯
├┼─────────────────⦿
├┤~ @ll_botchamber_ll
├┤~ @unbornedvillian
├┤~ @ll_radhe_ll
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @unbornedvillian
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ＺＥＵＳ", url=f"https://t.me/unbornedvillian")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/ll_botchamber_ll"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://github.com/Ansuman-web/ZEUSFAKEREPO.git"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/ll_botchamber_ll"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/zeus_music_robot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/c4ad0958b5913fd3ccb3e-7de280b4c35397f60b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
