import threading
from collections import deque
from threading import Lock

# Thread-safe list using a lock
shared_list = deque()
list_lock = Lock()

def add_to_list():
    for i in range(10):
        with list_lock:
            shared_list.append(i)

def read_from_list():
    with list_lock:
        print(f"List content: {list(shared_list)}")

# Create threads
threads = [threading.Thread(target=add_to_list) for _ in range(3)]
threads.append(threading.Thread(target=read_from_list))

# Start threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
