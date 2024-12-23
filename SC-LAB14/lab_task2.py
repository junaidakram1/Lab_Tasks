import threading

counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100):
        with counter_lock:
            counter += 1

# Create threads
threads = [threading.Thread(target=increment_counter) for _ in range(3)]

# Start threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
