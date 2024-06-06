import asyncio
from susi import susi

from .utils.logger import log

loop = asyncio.get_event_loop()

async def init():
    log("main").info("Attempting to start bot.")
    await susi.start()

    # Add some asynchronous tasks here to keep the event loop running
    while True:
        await asyncio.sleep(1)
        print("Event loop is still running...")

if __name__ == "__main__":
    loop.run_until_complete(init())
    log("main").warning("Bot stopped due to inactivity.")