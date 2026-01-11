import time, multiprocessing

# start = time.perf_counter()
#
#
# def do_something():
#     print("Sleeping for 1 second")
#     time.sleep(1)
#     print("Done sleeping...")
#
#
# do_something()
# do_something()
#
# finish = time.perf_counter()
#
#
# print(finish - start)

# So we are running a function, and it is executing the task for 1 second, and we are executing another function which is again taking 1 second.
# A single CPU core is handling both of these functions
# We can use multiprocessing module to split these tasks to other CPU cores and run them at the same time.
# Tasks are either going to be I/O bound or CPU bound.
# CPU bound tasks are the things that are crunching a lot of numbers and using the CPU.
# I/O bound tasks are things that are waiting for input/Output operations to be completed, and they are not using the CPU all that much. Example _> File system operations and network operations
# We are going to spread work out on multiple processes on our machine, and run those tasks at the same time.

import multiprocessing, concurrent.futures
import time

#
# def worker_function():
#     """A function that simulates some work."""
#     print("Worker process started...")
#     time.sleep(2)  # Simulate a time-consuming task
#     print("Worker process finished.")
#
#
# if __name__ == "__main__":
#     # 1. Create a process object
#     p = multiprocessing.Process(target=worker_function)
#
#     # 2. Start the process (runs concurrently)
#     p.start()
#
#     # 3. Join the process: The main process waits here.
#     p.join()  # The main program will pause until 'p' is finished.
#
#     print("Main program continues and exits.")
#
# # In Python's multiprocessing module, the join() method is a synchronization primitive that blocks the main program's execution until the process on which it is called terminates. It is used to ensure that the main process waits for its child processes to complete their work before proceeding to subsequent code that might depend on the child processes' results or resources.
#
#
# start = time.perf_counter()
#
#
# def do_something(seconds):
#     print(f"Sleeping for {seconds} second")
#     time.sleep(1)
#     print("Done sleeping...")

#
# processes = []
# if __name__ == "__main__":
#     for _ in range(10):
#         p = multiprocessing.Process(target=do_something, args=[1.5])
#         p.start()
#         # p.join()
#
#     #     In this code with p.join(), it makes no sense to use multiprocessing because it is doing everything sequentially, one after the another like a normal piece of code.
#     # p.join() only makes sense when you 1 or more functions which need to be executed before another function because other functions depends on that particular function to complete.
#
#     finish = time.perf_counter()
#
#     print(finish - start)


# The Computer has ways of switching off between cores when one of them isn't too busy, so even though we have more processes than cores, it's still finished in a second.
# In Python 3.2, they added the process called pull executor, and in a lot of cases this will be a lot easier, and more efficient way to run multiple processes. It also allows us to easily switch over to using multiple threads instead of processes as well depending on the problem that we are trying to solve.


def worker_function():
    """A function that simulates some work."""
    print("Worker process started...")
    time.sleep(2)  # Simulate a time-consuming task
    print("Worker process finished.")


if __name__ == "__main__":
    # 1. Create a process object
    p = multiprocessing.Process(target=worker_function)

    # 2. Start the process (runs concurrently)
    p.start()

    # 3. Join the process: The main process waits here.
    p.join()  # The main program will pause until 'p' is finished.

    print("Main program continues and exits.")

# In Python's multiprocessing module, the join() method is a synchronization primitive that blocks the main program's execution until the process on which it is called terminates. It is used to ensure that the main process waits for its child processes to complete their work before proceeding to subsequent code that might depend on the child processes' results or resources.


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for {seconds} second")
    time.sleep(1)
    return "Done sleeping..."



if __name__ == "__main__":

    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(do_something, 3)
        f2 = executor.submit(do_something, 3)
        print(f1.result(), f2.result())
    # The submit method schedules a function to be executed and returns a future object so a future object basically encapsulates the execution of our function and allows us to check on this after it's been scheduled.

    finish = time.perf_counter()

    # The concurrent.futures.ProcessPoolExecutor() is a high-level interface provided b
    print(finish - start)
# Our pool will make a decision based on our hardware to make a decision whether to use multiprocessing or multithreading.y Python's concurrent.futures module that simplifies the execution.


# It abstracts away the complexity of managing individual multiprocessing.Process objects, queues, and locks, allowing you to easily parallelize CPU-bound tasks across multiple CPU cores.
# How It Works
# ProcessPoolExecutor manages a fixed (or dynamically sized) pool of worker processes. When you submit a function to the executor, it places the function and its arguments into a queue. One of the idle worker processes picks up the task, runs it, and returns the result to the main process via an internal mechanism.
# This is fundamentally different from the ThreadPoolExecutor, which uses threads and is better suited for I/O-bound tasks. ProcessPoolExecutor uses actual separate processes, bypassing Python’s Global Interpreter Lock (GIL) and enabling true parallel execution of CPU-intensive Python code.

import concurrent.futures
import time

def perform_cpu_intensive_task(input_data):
    """Simulates a task that takes 1 second of CPU time."""
    time.sleep(1) # Replace with actual calculation
    return input_data * 2

# This block ensures processes start up and shut down correctly
if __name__ == '__main__':
    data_to_process = [1, 2, 3, 4, 5]
    # With I/O bounds tasks, You can use thread pool executor. ThreadPoolExecutor is much better for I/O bound tasks but if you have a boat load of I/O bound tasks then multiprocessing with also outperform multithreading for I/O bound tasks.
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        # Using map to process all data in parallel
        # The results are returned in the order of the input list
        results = executor.map(perform_cpu_intensive_task, data_to_process)
    #     All of the numbers in data to process will be executed at the same time.

    # After the 'with' block exits, all workers are terminated
    print("All tasks complete. Results:")
    for result in results:
        print(result)
#         It will return the results in the order that they started.
#         They might not be able to complete the processes in order but they will print the results in order.


# ! The concurrent.futures.ProcessPoolExecutor is not an alternative to multiprocessing; rather, it is a high-level wrapper built on top of the lower-level multiprocessing module.
# It provides a simpler, more streamlined interface for a specific common use case: distributing a set of tasks across a fixed pool of worker processes.
# Yes, the concurrent.futures.ProcessPoolExecutor() effectively manages the join() method for you automatically.
# That is one of its primary benefits: it abstracts away the need for manual process management.
# When you use the ProcessPoolExecutor, you don't call start() and join() manually. The library handles the entire lifecycle:
# Process Creation: It starts the worker processes when the executor is initialized (usually at the start of the with block).
# Joining and Cleanup: When the with concurrent.futures.ProcessPoolExecutor(...) as executor: block is exited, the executor's shutdown(wait=True) method is automatically called. This method internally performs the equivalent of calling join() on all the worker processes, ensuring all tasks are completed and resources are cleaned up before your main program continues past that block.

# The results are coming in as they are completed. The CPU will assign the task as they come.


#  Submit method is submitting each function once at a time but to run list
# ! We can use map method to pass in multiple iterables and execute the same function for each element of iterable.

# Using executor.map(): The map() call itself is a blocking operation. It waits internally until all results are computed and returned to the main process, managing the joining implicitly.
# Using executor.submit(): The submit() method returns a Future object immediately. To explicitly wait for a specific task to finish, you would call future.result() or use concurrent.futures.wait(). These methods manage the underlying synchronization and joining process.
# Instead of returning results, as they are completed, map method will maintain the order of execution. map will return the results in the order that they are started.


#  So anytime you are using the context manager like this it's going to automatically "join" (there is no wait time like before, the computer will automatically decide whether to wait or not for a particular method to complete)
#  those processes and there going to complete before that context manager finishes.

# ? WHENEVER YOU ADD IN EVEN MORE ITEMS MAYBE PROCESSES WILL START TO BECOME MORE PERFORMANT THAN THREADS
# ? Try both multiprocessing and multithreading and check which gives you the most speed up.
# * A single CPU core has two threads, you can perform two different tasks in these two different threads at the same time.
# * CPython is the most commonly used form of Python does allow multithreading due to GIL, but you can also use other forms like Jython.
# * Multithreading is not recommended because memory management and processing becomes very confusing and can cause a system to  crash.


