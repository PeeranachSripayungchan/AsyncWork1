# example of running coroutine
import asyncio

# define the coroutine
async def custom_coro():
    # wait for a take to be done
    # await another routine
    await asyncio.sleep(1)

# main coroutine
async def main():
    # execute my custom coroutine
    await custom_coro()

# start the coroutine program
asyncio.run(main())