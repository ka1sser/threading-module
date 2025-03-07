import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):

    print(f"Sleeping {seconds} second(s)...")

    time.sleep(seconds)

    return f"Done sleeping for {seconds}..."


with concurrent.futures.ThreadPoolExecutor() as executor:
    # Execute functions one at a time using .submit()
    # .submit(func, *args) -> schedules a function to be executed and returns a future object
    # Created a list via list comprehension

    secs = [5, 4, 3, 2, 1]

    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # Another option
    # .map() returns the results in the order that they were started
    results = executor.map(do_something, secs)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")
