import threading
import queue

mutex = threading.Semaphore() # Semaphore to lock and realse shared queue A
queue_A = queue.Queue()
queue_B = queue.Queue()