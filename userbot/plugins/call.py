"""call

Available Commands:

.call

"""

from telethon import events

import asyncio
from userbot.utils import admin_cmd




@borg.on(admin_cmd(pattern=r"call"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

   # input_str = event.pattern_match.group(1)

   # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` @P4R4D0XXX ,`Please Connect me to my lil bro,Pavel Durov`",
            "`User Authorised.`",
            "`Calling Pavel Durov`  `At +918978978908`",
            "`Private  Call Connected...`",
            "`Me: Hello Bc , Tere Baap bol raha , Telegram pe 1 bnde bakchodi kr rhe .`",   
            "`Me: uss bakchod madarchod ka account block kr jldi , tere baap ka hukam hai.`",    
            "`Pavel: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @P4R4D0XXX ",
            "`Pavel: OMG!!! Long time no see, Wassup Brother...\nI'll Make Sure That Bakchod Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Pavel: Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Apne baap ko mat sikhe , mujhe pta telegram mera hai and mere saaath hindi bole kr mc`",
            "`Pavel: Theek hai gaitonde sir , aap ka dhanyawaad .`",
            "`Me: Ha Ha , Chl milte hai raat ko daaru piyega saath mai.`",
            "`Pavel: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
