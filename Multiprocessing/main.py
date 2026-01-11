# todo: Multithreading does not allow for actual parallelism because of GIL because we have CPU bound tasks.
# todo: A general rule of thumb is that you want to use threads for things that are I/O bound and and processes for things that are CPU bound
import multiprocessing as mp
import time, math

result_a = []
result_b = []
result_c = []


def make_calculation_one(numbers):
    for number in numbers:
        result_a.append(math.sqrt(number ** 3))


def make_calculation_two(numbers):
    for number in numbers:
        result_b.append(math.sqrt(number ** 4))


def make_calculation_three(numbers):
    for number in numbers:
        result_c.append(math.sqrt(number ** 5))


if __name__ == "__main__":
    number_list = list(range(50000000))

    p1 = mp.Process(target=make_calculation_one, args=(number_list,))
    p2 = mp.Process(target=make_calculation_two, args=(number_list,))
    p3 = mp.Process(target=make_calculation_three, args=(number_list,))

    start = time.time()
    p1.start()
    # p2.start()
    # p3.start()
    end = time.time()
    print(end - start)

    start = time.time()
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)
    end = time.time()
    print(end - start)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# In Python's multiprocessing module, the Pool class is used to manage a fixed pool of reusable worker processes to which you can submit tasks. This is ideal for data parallelism, where the same function needs to be executed many times on different sets of input data, particularly for CPU-bound tasks.

# import multiprocessing
#
# def square(n):
#     return n * n
#
# if __name__ == '__main__':
#     data = [1, 2, 3, 4, 5, 6, 7, 8]
#     with multiprocessing.Pool(processes=4) as pool:
#         # Distributes the 'square' function across the 'data' list
#         results = pool.map(square, data)

#     print(results)
#     # Output: [1, 4, 9, 16, 25, 36, 49, 64]

#  Both concurrent.futures.ProcessPoolExecutor() with map() and multiprocessing.Pool.map() achieve the same fundamental goal: distributing an iterable of tasks across multiple processes in an easy-to-use, "blocking" fashion.
#  The ProcessPoolExecutor approach is generally considered better for modern Python development due to cleaner resource management and better integration with other modern Python features.


# Both concurrent.futures.ProcessPoolExecutor() with map() and multiprocessing.Pool.map() achieve the same fundamental goal: distributing an iterable of tasks across multiple processes in an easy-to-use, "blocking" fashion.
# The ProcessPoolExecutor approach is generally considered better for modern Python development due to cleaner resource management and better integration with other modern Python features.

"""

Why ProcessPoolExecutor is Generally Better
The main advantage of ProcessPoolExecutor is its robust lifecycle management using the with statement (context manager protocol).
Automatic Cleanup: When the with block finishes, the executor's shutdown() method is called automatically, ensuring all worker processes are cleanly terminated and resources are released.
Cleaner Syntax: The code is generally cleaner and less prone to errors related to forgetting to close the pool manually.
Unified API: The concurrent.futures module provides a single, consistent API for both process-based parallelism (ProcessPoolExecutor) and thread-based concurrency (ThreadPoolExecutor), making code easier to swap and maintain.
Easier Error Handling: The Future objects used internally by ProcessPoolExecutor often provide clearer exception propagation than the older Pool structure.
Why multiprocessing.Pool is Still Used
multiprocessing.Pool is not a bad choice; it is mature, stable, and widely used in production code.
It is often found in older examples or tutorials.
It is still perfectly valid to use if you prefer its specific syntax or are working within an existing codebase that already uses it extensively.
Conclusion
If you are starting a new project in modern Python (3.2+), use concurrent.futures.ProcessPoolExecutor() as it provides a superior, safer, and cleaner interface for parallelizing tasks.
Both approaches ultimately manage the underlying process handling (including the join() operations) automatically, but the ProcessPoolExecutor does so in a more Pythonic and robust way.

"""
