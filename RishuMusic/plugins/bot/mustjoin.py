import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from RishuMusic import app

# Channels to enforce join
MUST_JOIN_1 = "ll_botchamber_ll"
MUST_JOIN_2 = "nenobots"

# List of random images
IMAGES = [
    "https://graph.org/file/f86b71018196c5cfe7344.jpg",
    "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
    "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
    "https://graph.org/file/84de4b440300297a8ecb3.jpg",
    "https://graph.org/file/84e84ff778b045879d24f.jpg",
    "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
    "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
    "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
    "https://graph.org/file/37248e7bdff70c662a702.jpg",
    "https://graph.org/file/0bfe29d15e918917d1305.jpg",
    "https://graph.org/file/16b1a2828cc507f8048bd.jpg",
    "https://graph.org/file/e6b01f23f2871e128dad8.jpg",
    "https://graph.org/file/cacbdddee77784d9ed2b7.jpg",
    "https://graph.org/file/ddc5d6ec1c33276507b19.jpg",
    "https://graph.org/file/39d7277189360d2c85b62.jpg",
    "https://graph.org/file/5846b9214eaf12c3ed100.jpg",
    "https://graph.org/file/ad4f9beb4d526e6615e18.jpg",
    "https://graph.org/file/3514efaabe774e4f181f2.jpg",
]

# Updated list of random captions
CAPTIONS = [
    "๏ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ {channel_name} ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ᴜsɪɴɢ ᴛʜᴇ ʙᴏᴛ!",
    "๏ ɪᴛ sᴇᴇᴍs ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ {channel_name} ʏᴇᴛ. ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ.",
    "๏ ᴊᴏɪɴ {channel_name} ᴛᴏ ᴜɴʟᴏᴄᴋ ғᴜʟʟ ᴀᴄᴄᴇss ᴛᴏ ᴍʏ ғᴇᴀᴛᴜʀᴇs!",
    "๏ ᴛᴏ ᴜsᴇ ᴍᴇ, ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ {channel_name}. ᴛᴀᴘ ᴛʜᴇ ʟɪɴᴋ ʙᴇʟᴏᴡ.",
    "๏ {channel_name} ᴍᴜsᴛ ʙᴇ ᴊᴏɪɴᴇᴅ ʙᴇғᴏʀᴇ ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛɪɴᴜᴇ!",
    "๏ ᴊᴏɪɴ {channel_name} ғᴏʀ ᴇxᴄʟᴜsɪᴠᴇ ᴄᴏɴᴛᴇɴᴛ ᴀɴᴅ ғᴜᴛᴜʀᴇ ᴜᴘᴅᴀᴛᴇs!",
    "๏ {channel_name} ɪs ᴀ ʀᴇǫᴜɪʀᴇᴍᴇɴᴛ ᴛᴏ ᴀᴄᴄᴇss ᴛʜɪs ʙᴏᴛ. ᴊᴏɪɴ ɴᴏᴡ!",
    "๏ ɴᴇᴠᴇʀ ᴍɪss ᴏᴜᴛ! ᴊᴏɪɴ {channel_name} ᴛᴏ ᴇɴᴊᴏʏ ᴛʜᴇ ғᴜʟʟ ᴇxᴘᴇʀɪᴇɴᴄᴇ.",
    "๏ {channel_name} ᴋᴇᴇᴘs ʏᴏᴜ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴡɪᴛʜ ᴛʜᴇ ʙᴇsᴛ! ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.",
    "๏ ᴛʜɪs ʙᴏᴛ ʀᴇǫᴜɪʀᴇs ᴍᴇᴍʙᴇʀsʜɪᴘ ɪɴ {channel_name}. ᴘʟᴇᴀsᴇ ᴊᴏɪɴ.",
    "๏ ᴊᴏɪɴ {channel_name} ᴀɴᴅ sᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ! ʏᴏᴜ'ʟʟ ɴᴇᴇᴅ ɪᴛ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.",
    "๏ {channel_name} ɪs ᴀ ᴘʟᴀᴄᴇ ғᴏʀ ᴇxᴄʟᴜsɪᴠᴇ ᴄᴏɴᴛᴇɴᴛ. ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ᴜɴʟᴏᴄᴋ!",
]

async def send_join_message(msg: Message, link: str, channel_name: str):
    image = random.choice(IMAGES)
    caption = random.choice(CAPTIONS).format(channel_name=channel_name)
    try:
        await msg.reply_photo(
            photo=image,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("• ᴊᴏɪɴ •", url=link)]
                ]
            )
        )
        await msg.stop_propagation()
    except ChatWriteForbidden:
        pass

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channels(app: Client, msg: Message):
    if not (MUST_JOIN_1 and MUST_JOIN_2):
        return

    try:
        try:
            await app.get_chat_member(MUST_JOIN_1, msg.from_user.id)
        except UserNotParticipant:
            link1 = f"https://t.me/{MUST_JOIN_1}"
            await send_join_message(msg, link1, "ll_botchamber_ll")

        try:
            await app.get_chat_member(MUST_JOIN_2, msg.from_user.id)
        except UserNotParticipant:
            link2 = f"https://t.me/{MUST_JOIN_2}"
            await send_join_message(msg, link2, "Nenobots")

    except ChatAdminRequired:
        print("Please make me admin in the required channels!")
