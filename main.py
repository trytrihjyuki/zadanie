from consumer import Consumer
from producer import Producer
from source import Source

N_FRAMES = 100
PRODUCTION_DELAY = 0.001

if __name__ == '__main__':
    source = Source((768, 1024, 3))
    producer = Producer(source, N_FRAMES, PRODUCTION_DELAY)
    consumer = Consumer(N_FRAMES)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()