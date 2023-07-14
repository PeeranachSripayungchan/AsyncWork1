# import library
import random
import asyncio
import time

# coroutine to execute in a new task
async def task_coro(arg):
    value = random.random()
    await asyncio.sleep(value)
    print(f'{time.ctime()} > task {arg} done with {value}')

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(20)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    print(f'{time.ctime()} All done')

# start the asyncio program
asyncio.run(main())