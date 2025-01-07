from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**⌾ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ ʀᴇᴘᴏs ⌾
 
● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ˹🦋⃟≛⃝ᴀʀᴀᴅʜʏᴀꭙ ᴍᴜsɪᴄ ♡゙゙

● ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ● 

❖ ϻᴧᴅє ʙʏ  ➛ [ʙᴏᴛ ᴄʜᴀᴍʙᴇʀ](https://t.me/ll_botchamber_ll)**
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
InlineKeyboardButton("• RADHE •", url=f"https://t.me/radhe_music_robot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/oK4.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
