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
    command(["مطورين نورهان","المطورين","مطورين","مطوريني"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين نورهان ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩𓏺᭙ɦᎥ᥉ƙᥱᥡ ˹َّّ ", url=f"https://t.me/bp_bp"), 
                 ],[
                    
                
                    InlineKeyboardButton(
                        "★⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝⚡", url=f"https://t.me/Libya13n"),
                ],[
                    InlineKeyboardButton(
                        "᳒𝑻ٌْ!ًِ𝑶𝑴ّْ𝑴ً𝒀#¹🇱🇾 ˹َّّ", url=f"https://t.me/CVVVS1"), 
                 ],

            ]

        ),

    )








@app.on_message(
    command(["ويسكي","مبرمج السورس","وسكي","الوسكي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("bp_bp")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["قناة السورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Libya13n")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["مطوري","محمد","حمادي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("bp_bp")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["المطور","مطور السورس","تومي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("CVVVS1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["ذكاء نورهان"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://k.top4top.io/p_2706s63yo1.jpg",
        caption=f"""**⩹⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس نورهان\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩𓏺᭙ɦᎥ᥉ƙᥱᥡ ˹َّّ", url=f"https://t.me/bp_bp"), 
                 ],[
                    InlineKeyboardButton(
                        "᳒𝑻ٌْ!ًِ𝑶𝑴ّْ𝑴ً𝒀#¹🇱🇾 ˹َّّ", url=f"https://t.me/CVVVS1"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝⚡", url=f"https://t.me/Libya13n"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://b.top4top.io/p_2682mb2f41.jpg",
        caption=f"""**⩹⊷━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس حياه\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩𓏺᭙ɦᎥ᥉ƙᥱᥡ ˹َّّ", url=f"https://t.me/bp_bp"), 
                 ],[
                    InlineKeyboardButton(
                        "᳒𝑻ٌْ!ًِ𝑶𝑴ّْ𝑴ً𝒀#¹🇱🇾 ˹َّّ", url=f"https://t.me/CVVVS1"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِᥒَِ᥆َِᖇَِꫝُِꪖَِᥒ⌝⚡", url=f"https://t.me/Libya13n"),
                ],

            ]

        ),

    )



    
