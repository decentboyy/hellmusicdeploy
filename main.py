import asyncio
from pytgcalls import idle
from ImageFont.blaze import SUPPORT
from ImageFont.main import call_py, bot, user as blaze

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()
    await bot.join_chat("RaichuOfficial")
    await blaze.send_message(
               SUPPORT,
            "<b>Congrats!! Music Bot has started successfully!</b>",
        )    
                          
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

