import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime


from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests

sython.start()





@sython.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    
    await event.edit(f'''**
♔ 𝐬𝐲𝐭𝐡𝐨𝐧 𝐢𝐬 𝐰𝐨𝐫𝐤𝐢𝐧𝐠
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
السورس يعمل بنجاح
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
**''')

@sython.on(events.NewMessage(outgoing=True, pattern=r".الاسعار"))
async def _(event):
    
    await event.edit(f'''
حياتي تسعيرة تصاميمي تبلش من ال3$ وانت صاعد كل ماتدفع اكثر تستلم تصميم اقوى و ب جوده افضل. 

يعني اذا تدفع. 3$ اصمملك حگ 3$ لذلك ميصير تتوقع شي خرافي اما اذا دفعت 10-15$ حتستلم شي مرتب ومراح تندم انك دفعتهن عله هيج شي

 وهاي قناتي تكدر تدخل وتوف الاختلاف ب مستوى التصاميم على حسب اسعارهم
 • @PAIIIIIIIIIIIIIIN •
 
''')


@sython.on(events.NewMessage(outgoing=True, pattern=r".فرق"))
async def _(event):
    
    await event.edit(f'''
التصميم النصي هوة اسمك او اسم فريقك مصمم بشكل مرتب وجذاب 

اما تعديل الصور هوة صورة من عندي او منك انت تجيبهه اكتب عليهه النص الي انت تريده واعدلها من ناحية اضائة و جوده و ضلال والى اخره ولازم تكون صورة دقتهه عالية

 
''')

@sython.on(events.NewMessage(outgoing=True, pattern=r".تفاصيل"))
async def _(event):
    
    await event.edit(f'''
عزيزي ارسل جميع التفاصيل الي تريدهه تكون ب التصميم مثل الوان التصميم او اسلوب التصميم حسابات التواصل او ارقام التواصل الى اخره بالاضافه الى النص الرئيسي (الاسم) الي راح يكون ب التصميم
 
''')

@sython.on(events.NewMessage(outgoing=True, pattern=r".علية"))
async def _(event):
    
    await event.edit(f'''
اذا تريد يكون التصميم على ذوقي من جميع النواحي وبجميع التفاصيل فا مايحقلك تطلب اكثر من تعديل ع التصميم لمن اخلصه باختصار لتكلي صمم من يمك واخر شي تكلي معجبني
 
''')

@sython.on(events.NewMessage(outgoing=True, pattern=r".تم"))
async def _(event):
    
    await event.edit(f'''
تم استلام طلبك الحد الاقصى لتسليم الطلب هو 24 ساعه راح تستلم تصميمك خلال هاذي الفتره ان شاء الله، لتراسل وتحلى بالصبر بين ميكمل تصميمك
 
''')


@sython.on(events.NewMessage(outgoing=True, pattern=r".الفارات"))
async def _(event):
    
    await event.edit(f'''

`.الاسعار`
`.علية`
`.تفاصيل`
`.تم`
`.فرق`

« اضغط الامر للنسخ »
 
''')

print("♦️ sython is Running ♦️")
sython.run_until_disconnected()
