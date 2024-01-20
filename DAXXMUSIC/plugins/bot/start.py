import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from DAXXMUSIC import app
from DAXXMUSIC.misc import _boot_
from DAXXMUSIC.plugins.sudo.sudoers import sudoers_list
from DAXXMUSIC.utils.database import get_served_chats, get_served_users, get_sudoers
from DAXXMUSIC.utils import bot_sys_stats
from DAXXMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from DAXXMUSIC.utils.decorators.language import LanguageStart
from DAXXMUSIC.utils.formatters import get_readable_time
from DAXXMUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string



YUMI_PICS = [
"https://telegra.ph/file/7f44ed4c727d6b9c655cf.jpg",
"https://telegra.ph/file/1f4b7196a50aa6c535e09.jpg",
"https://telegra.ph/file/19961f6433d5747677d0d.jpg",
"https://telegra.ph/file/69f06abdc7c330a007979.jpg",
"https://telegra.ph/file/e0b414dcf8aedc36bb694.jpg",
"https://telegra.ph/file/5dbff91edfa22be7be826.jpg",
"https://telegra.ph/file/808e55c04d0561ec14fff.jpg",
"https://telegra.ph/file/90392ff07e2d7f0e21ba9.jpg",
"https://telegra.ph/file/042af63d674c1d2d813b7.jpg",
"https://telegra.ph/file/2419bf7887f4ec2fb43fa.jpg",
"https://telegra.ph/file/048574c4feab46ca96d56.jpg",
"https://telegra.ph/file/7146663c51be76494a6fb.jpg",
"https://telegra.ph/file/008d5f4a1b214d61e27e7.jpg",

]



EMOJIOS = [ 
      "🌿",
      "⚡",
      "💗",
      "😍",
      "🥰",
      "💫",
      "✨",
    
]



@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            accha = await m.reply_text(
            text = random.choice(EMOJIOS),
            )
            await asyncio.sleep(1)
            await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠..")
            await asyncio.sleep(0.1)
            await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠...")
            await asyncio.sleep(0.1)
            await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠....")
            await asyncio.sleep(0.1)
            await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐞𝐝.✓")
            await asyncio.sleep(0.2)
            await accha.edit("𝐒𝐭𝐚𝐫𝐭")
            await asyncio.sleep(0.2)
            await accha.delete()
            return await message.reply_photo(
                random.choice(YUMI_PICS),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        accha = await m.reply_text(
            text = random.choice(EMOJIOS),
            )
        await asyncio.sleep(1)
        await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠..")
        await asyncio.sleep(0.1)
        await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠...")
        await asyncio.sleep(0.1)
        await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠....")
        await asyncio.sleep(0.1)
        await accha.edit("𝐒𝐭𝐚𝐫𝐭𝐞𝐝.✓")          
        await asyncio.sleep(0.2)
        await accha.edit("𝐒𝐭𝐚𝐫𝐭")
        await asyncio.sleep(0.2)
        await accha.delete()
        await message.reply_sticker("CAACAgUAAxkBAAIJnmWp7yxispwFOhwufAon5GJkMabMAAIlCwACpm9QVX8Bb2L6G_JtHgQ"),
        await message.reply_photo(
            random.choice(YUMI_PICS),
            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM,served_users,served_chats),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        random.choice(YUMI_PICS),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    random.choice(YUMI_PICS),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
                               
