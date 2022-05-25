# from consumer import Consumer
from producer import Producer
from source import Source


if __name__ == '__main__':
    source = Source((768, 1024, 3))
    producer = Producer(source, 10, 1)
    producer.start()