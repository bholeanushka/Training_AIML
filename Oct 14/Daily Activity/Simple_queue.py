import threading
import queue
import time

q = queue.Queue()


def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(1)
    print("Producer done")


def consumer():
    while True:
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer, daemon=True)

producer_thread.start()
consumer_thread.start()

producer_thread.join()  # Wait for producer to finish
q.join()  # Wait until all tasks are processed
print("All tasks done")
