import os

from PIL import Image
import threading
import queue

mutex = threading.Semaphore() # Semaphore to lock and realse shared queue A
queue_A = queue.Queue()
queue_B = queue.Queue()

def store_images():
    os.mkdir('processed/')

    cnt = 1
    while queue_B.qsize():
        print(cnt)
        frame = queue_B.get()
        im = Image.fromarray(frame)
        im.save(f'processed/frame_{cnt}.png')
        cnt += 1