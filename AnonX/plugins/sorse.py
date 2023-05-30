import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint
@app.on_message(
    command(["صورص","سورس","السورس","سورس نورهان", "نورهان"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://k.top4top.io/p_2706s63yo1.jpg",
        caption=f"""
  ╭═★[⧼⌞𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⧽](https://t.me/Libya13n)★═╮
   
   么  [𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⋆♡](https://t.me/Libya13n) 𝐶𝐻𝐴𝑁𝑁𝐸𝐿

   么  [𝑻ٌْ!ًِ𝑶𝑴ّْ𝑴ً𝒀#¹🇱🇾⋆♡](https://t.me/CVVVS1) 𝐷𝐸𝑉𝐸L𝑂𝑃𝐸𝑅²    

   么  [َِ𓏺ꪔᥡ ᘜᖇ᥆ᥙρ⋆♡](https://t.me/Libya13n) 𝐺𝑅𝑂𝑈𝑃 𝐻𝐸L𝑃 

   么  [𓏺ꪔᥡ ხ᥆ƚ⋆♡](t.me/XXVXV6BOT) 𝑀𝑈𝑆𝐼𝐶 𝐵𝑂𝑇

  ╰─么[𓏺َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ](https://t.me/Libya13n)  • ◈ •[𓏺َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ](https://t.me/Libya13n)  么─╯ 
  
 ⍟𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑻ٌْ!ًِ𝑶𝑴ّْ𝑴ً𝒀#¹🇱🇾", url=f"https://t.me/CVVVS1"), 
                ],[
                    InlineKeyboardButton(
                        "⩹━⊷⌯ 𓏺𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ♡", url=f"https://t.me/Libya13n"),
                ],

            ]

        ),

    )



# @app.on_message(command(["غنيلي", "غني", "غ", "حياه غنيلي"]))
# async def ihd(client: Client, message: Message):
#     rl = random.randint(3,267)
#     url = f"https://t.me/bsmaatt/{rl}"
#     await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
#     reply_markup=InlineKeyboardMarkup(
#             [
#                 [
#                     InlineKeyboardButton(
#                         message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
#                 ],
#             ]
#         )
#     )
    
# @app.on_message(command(["صورة","صور"]))
# async def ihd(client: Client, message: Message):
#     rs = random.randint(39,148)
#     url = f"https://t.me/GTTUTY/{rs}"
#     await client.send_photo(message.chat.id,url,caption="💕 ¦ تـم اختيـار الصوره لـك",parse_mode="html",
#     reply_markup=InlineKeyboardMarkup(
#             [
#                 [
#                     InlineKeyboardButton(
#                         message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
#                 ],
#             ]
#         )
#     )
