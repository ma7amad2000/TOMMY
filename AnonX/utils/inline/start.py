from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 الاوامر",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 الاوامر", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝑻ٌْ!ًِ𝑶𝑴ّْ𝑴ً𝒀#¹🇱🇾", url=f"https://t.me/CVVVS1"
            ),
            InlineKeyboardButton(
                text="👤 مطور البوت", user_id=OWNER
            ),
            InlineKeyboardButton(
                text="ᯓ𓆩𓏺᭙ɦᎥ᥉ƙᥱᥡ🇱🇾", url=f"https://t.me/bp_bp"
            )
        ],
        [
            InlineKeyboardButton(
                text=" ⌞ ⩹━⊷⌯ 𓏺᥉᥆ᥙᖇᥴᥱ ꫝꪖꪗꪖ⌝ ", url=f"https://t.me/HL_BG"
            )
        ],[
            InlineKeyboardButton(
                text=" ⌞ ⩹━⊷⌯ 𓏺𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝ ", url=f"https://t.me/Libya13n"
            )
        ],
     ]
    return buttons