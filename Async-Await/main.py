# ! In Python, when we mark a function with Async, it becomes a coroutine and coroutine can be paused and resumed, allowing other tasks to run in the meantime.
# ! We can write non-blocking code that performs tasks concurrently resulting in faster and more responsive programs.
# ! Async don't wait for tasks to complete and then move  with the other one. it uses the downtime of one task to complete the another task.
# ! Async and await are fundamentally single threaded, not multithreaded.
# ! This provides concurrency not parallelism.
# ! Context switching happens only at await points.
#  We can use multiprocessing and async at the same time.


# ? Imagine Programming as a journey from point A to B, It's like sending out scouts to explore multiple paths at once without waiting for the first scout to return before sending out the next.
# ? This way, Our program can handle multiple tasks simultaneously, making it more efficient especially when dealing with operations that have waiting time.
# ? Async IO is your choice for the tasks that wait a lot like network requests or reading files.
# ? It excels at handling tasks concurrently without using much CPU power. This makes your application efficient and responsive when you are waiting on a lot of different tasks.
# ? Threads are suited for tasks that may need to wait but also share data. They can run in parallel within the same application making useful for tasks that are I/O bound but less CPU intensive.


# * In Python, The event loop is the core that manages and distributes tasks. Think of it as a central hub with the tasks circling around it, waiting for their turn to be executed. Each task takes turn in the center where it's executed immediately or paused if it is waiting for the data from the internet.
# * When a task awaits it steps aside making room for another task to run. Ensuring the loop is always efficiently utilized.
# * Once the awaited operation is complete, the task will resume ensuring a smooth and responsive program flow.


import asyncio


# Coroutine function
# # async def main():
# #     print("Start of the main coroutine")
# #     await asyncio.sleep(1)
# # # main() __> Coroutine Object, this coroutine object needs to be awaited in order for us to get the result.
# # We are passing a coroutine function which returns the coroutine object.
#
# # asyncio.run(main())  # This will handle awaiting the code routine
#
#
# #  Define a coroutine that simulates a time-consuming task
# async def fetch_data(delay):
#     print("Fetching data...")
#     await asyncio.sleep(delay)  # Simulate I/O operations with a sleep.
#     print("data fetched")
#     return {"data": "some data"}  #Return some data
#
#
# # Define another coroutine that calls the first coroutine.
# async def main():
#     print("Start the main coroutine")
#     task = fetch_data(2)  # This is a coroutine object and at this point in time, it is not being executed yet because it hasn't been awaited.
#     # Await the fetch data_coroutine, passing execution of main until fetch data completes.
#     result = await task
#     print(result)
#     print("End of the main coroutine")
#
#
# asyncio.run(main())
# In order for a coroutine to actually be executed, it needs to be awaited.


# time.sleep(5): This call blocks the entire Python process for 5 seconds. Nothing else happens during this time.
# await asyncio.sleep(5): This call tells the event loop, "I'm done for the next 5 seconds; go work on something else in the meantime." After 5 seconds, the event loop returns to this task.


# Define a coroutine that simulates a time_consuming task
# async def fetch_data(delay, id):
#     print("Fetching data ... id", id)
#     await asyncio.sleep(delay) # simulate an I/O operation with a sleep
#     print("data fetched id ", id)
#     return {"data": "some_data", "id": id}  # return some data
#
#
# # Define another coroutine that calls the first coroutine
# async def main():
#     task_1 = fetch_data(5,1)
#     task_2 = fetch_data(2,2)
#
#     result1 = await task_1
#     print(result1)
#     result2 = await task_2
#     print(result2)

#  In the above code, we haven't really got any performance benefit here, we have just created a way for a task to be finished.
# asyncio.run(main())

# The problem with the above code is that we needed to wait for one coroutine to finish before we start executing the next.
# With task we don't have that issue and as soon as the coroutine is sleeping or it's on something that's not in control of our program, we can move on and start executing another task.
# todo: Now we are going to see how to run both of these tasks at the same time.
# todo: Now we are moving to the next important concept which is a task. Now a task is a way to schedule a coroutine to run as soon as possible and allow us to run multiple coroutines simultaneously.
# todo: we are not going to be executing these tasks at the same time. we are not using multiple CPU cores or multiprocessing.

# async def fetch_data(id, sleep_time):
#     print(f"Coroutine {id} starting to fetch data")
#     await asyncio.sleep(sleep_time)
#     return {"id": id, "data": f"Sample data from coroutine {id}"}
#
#
# async def main():
#     # Create tasks for running coroutines concurrently
#     task1 = asyncio.create_task(fetch_data(1, 2))  # we passed in the coroutine object in create_task function.
#     task2 = asyncio.create_task(fetch_data(2, 3))
#     result1 = await task1
#     result2 = await task2
#     # We won't start the third one until the first and second one are done.
#     task3 = asyncio.create_task(fetch_data(3, 1))
#
#     result1 = await task1
#     result2 = await task2
#     result3 = await task3
#
#     print(result1, result2, result3)
#     When we create a task, we are scheduling the coroutine to run as quickly as possible and we are allowing multiple coroutines to run at the sma e time.
# Now all of that is handled by the event loop, and it's not something that we need to manually take care of.
# How-ever if we want to wait for some task to finish before moving to the next one , we can use the await syntax
# It allows us to synchronize our code in whatever manner we see fit.
# asyncio.run(main())

# ! GATHER FUNCTION __> IT IS A QUICK WAY TO RUN MULTIPLE COROUTINES RATHER THAN JUST CREATING THE TASK FOR EVERY SINGLE ONE OF THE COROUTINES USING THAT CREATE TASK FUNCTION.
# WE CAN USE GATHER AND IT WILL AUTOMATICALLY CONCURRENTLY FOR US AND COLLECT THE RESULTS IN A LIST.


# async def fetch_data(id, sleep_time):
#     print(f"Coroutine {id} starting to fetch data")
#     await asyncio.sleep(sleep_time)
#     return {"id": id, "data": f"Sample data from coroutine {id}"}
#
#
# async def main():
#     #     Run coroutines concurrently and gather their return values
#     # It is going to await for all the results to finish
#     results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))
#     #     Process the results
#     for result in results:
#         print(f" Received Result {result}")
#
#
# asyncio.run(main())
# ! Gather is not great at error handling and it's not going to cancel other coroutines, if one of them were to fail
# ? The next method is going to deal with error handling, and it is typically preferred over gather.

# todo: TASK GROUP FUNCTION __> It is more preferred way of actually creating multiple tasks and organise them together.
# It provides builtin error handling and if any of the tasks inside of our task groups were to fail, it will automatically cancel all of the other tasks which is typically preferable when we are dealing with some advanced errors or some larger applications where we wanna be a bit more robust.


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    #     After moving out of this async block, it will execute other tasks, but first it will execute everything inside the block.

    #      After the task group block, all tasks have completed
    results = [task.result() for task in tasks]
    for result in results:
        print(result)


asyncio.run(main())
# async with is the asynchronous context manager

# Another example of Task Group
# import asyncio
#
# async def say_hello(name, delay):
#     await asyncio.sleep(delay)
#     print(f"Hello from {name}")
#
# async def main():
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(say_hello("Task A", 2))
#         tg.create_task(say_hello("Task B", 1))
#         tg.create_task(say_hello("Task C", 3))
#
# asyncio.run(main())

# _____________________________________________________________________________________________________
# 4. Futures __> It is a promise of a future result, it is just saying that result will come in the future. we don't know when it's going to be
# We can create a future and await its value
# We didn't await the task to finish, we awaited the future object
# So inside the task, we set the value of the future, and we awaited that. which means that as soon as we get the value of the future this task may or may not actually be complete
# We are just waiting for an value to be available, we are not waiting for na entire task or an entire routine to finish
# import asyncio
#
# async def main():
#     loop = asyncio.get_running_loop()
#
#     # Create a Future
#     future = loop.create_future()
#
#     async def set_result_later():
#         await asyncio.sleep(2)
#         future.set_result("Task completed")
#
#     # Schedule another coroutine that will complete the Future
#     asyncio.create_task(set_result_later())
#
#     print("Waiting for future...")
#     result = await future
#     print(result)
#
# asyncio.run(main())

# import asyncio
#
# async def main():
#     future = asyncio.Future()
#
#     async def complete():
#         await asyncio.sleep(1)
#         future.set_result(42)
#
#     asyncio.create_task(complete())
#     print(await future)
#
# asyncio.run(main())

# Just a promise of an eventual result

# _________________________________________________________

# Synchronisation __> These are the tools that allow us to synchronize the synchronization of various coroutines even when we have larger or more complicated programs.

shared_resource = 0
# You can also have a database, or maybe it's a file
# ! We want to make sure that no two coroutines are working on this at the same time.
# ! If both coroutines are writing something to the file then it might give an error where we get a mutated state or just weird results end up occurring because different operations happening at same time.
# ! We want to lock it off and use one coroutine at a time.

# we have ability to acquire the lock
lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resource
    async with lock:
        #         Critical section starts __> It needs to finish executing before the lock will be released to the next coroutine
        # It is like synchronization programming
        print(f"shared resource before modification {shared_resource}")
        shared_resource += 1  # Modify the shared resource
        await asyncio.sleep(1)  # simulate an I/O operation
        print(f"Resource after Modification {shared_resource}")
        # Critical section ends


async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

asyncio.run(main())

# An asyncio.Lock prevents multiple coroutines from accessing the same code at the same time.
# All the lock is really doing is it's synchronizing our different code routines so they can't be using a particular block of code or executing this block of code while another coroutine is executing it.
# It is locking off access to a critical resource that we only want to be access one at a time but the rest of the code can work asynchronously.

"""
Short Answer (Direct)

You use locks because you want concurrency for speed and efficiency,
but still need correctness when accessing shared data.

If you truly do not need concurrency, synchronous programming is better."""


# import asyncio
#
# lock = asyncio.Lock()
#
# async def task(name):
#     async with lock:
#         print(f"{name} entered")
#         await asyncio.sleep(1)
#         print(f"{name} exited")
#
# async def main():
#     async with asyncio.TaskGroup() as tg:
#         tg.create_task(task("Task 1"))
#         tg.create_task(task("Task 2"))
#
# asyncio.run(main())


# ____________________________________________************************************________________________________________

# ! Semaphore __> It works very similar to a lock, However it allows multiple coroutines to have access to the same object at the same time but we can decide how many we want that to be.

import asyncio

semaphore = asyncio.Semaphore(2)

async def task(name):
    async with semaphore:
        print(f"{name} entered")
        await asyncio.sleep(1)
        print(f"{name} exited")

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task("Task 1"))
        tg.create_task(task("Task 2"))
        tg.create_task(task("Task 3"))
        tg.create_task(task("Task 4"))

asyncio.run(main())
# We throttle our code manually to send particular number of requests at a particular time.

# ________________________________________________________________________________________________________________________
# Event

import asyncio

event = asyncio.Event()

async def waiter():
    print("Waiter: waiting for event...")
    await event.wait()
    print("Waiter: event received!")

async def setter():
    await asyncio.sleep(2)
    print("Setter: setting event")
    event.set()

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(waiter())
        tg.create_task(setter())

asyncio.run(main())

# 1. What Is an Event?
#
# An Event is a signal.
# 	•	One task waits
# 	•	Another task sends the signal
# 	•	When the signal arrives, all waiting tasks continue


# 1. What Is an Event?
#
# An Event is a signal.
# 	•	One task waits
# 	•	Another task sends the signal
# 	•	When the signal arrives, all waiting tasks continue


# ! Condition -------------------------------------___________________-------_______)))))))))))))))))))))))))))


# What Is an asyncio.Condition?
#
# A Condition is used when:
#
# Tasks need to wait for a specific condition to become true,
# and another task will change the state and notify them.
#
# It is Event + Lock combined, with more control.
#
# ⸻
#
# Very Simple Example
#
# Scenario
#
# A consumer waits until data is available.
# A producer creates the data and notifies the consumer.


import asyncio

condition = asyncio.Condition()
data_ready = False

async def consumer():
    async with condition:
        while not data_ready:
            print("Consumer: waiting for data")
            await condition.wait()
        print("Consumer: data received")

async def producer():
    global data_ready
    await asyncio.sleep(2)
    async with condition:
        print("Producer: producing data")
        data_ready = True
        condition.notify()

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(consumer())
        tg.create_task(producer())

asyncio.run(main())


