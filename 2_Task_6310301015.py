# Example of getting the current task from the main coroutine
import asyncio

# Define a main corotine
async def main():
    # Report a message
    print("main coroutine started")
    # Get the current task
    task = asyncio.current_task()
    # Report its details
    print(task)

# Start the asyncio program
asyncio.run(main())

# main coroutine started
# <Task pending name='Task-1' coro=<main() running at D:\Homework\Async\1_asyncio\2_Asyncio_6310301015.py:11> cb=[_run_until_complete_cb() at D:\Python3.9.9\lib\asyncio\base_events.py:184]>
# PS D:\Homework\IOT\IOT_Quartet\Iot-quartet-main>