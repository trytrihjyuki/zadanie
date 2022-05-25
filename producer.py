import logging
import threading
import time

from common import mutex, queue_A
from source import Source

logging.basicConfig(level=logging.NOTSET, format='[%(threadName)s] %(message)s')
logger = logging.getLogger()


class Producer(threading.Thread):
    def __init__(self, source: Source, n_frames: int, production_wait: float = 0.05):
        """
        Class for the production of frames using the source.

        Args:
            source: Source object to produce frames
            n_items: number of frames produced
            production_wait: delay after each production
        """
        super().__init__()
        self.name = 'Producer'
        self._source: Source = source
        self._n_frames = n_frames
        self._production_wait = production_wait

    def run(self):
        for i in range(1, self._n_frames+1):
            frame = self._source.get_data()
            logger.debug(f'Produced {i}. frame.')

            mutex.acquire()
            queue_A.put(frame)
            logger.info(f'Put {i}. frame into A queue.')
            mutex.release()

            time.sleep(self._production_wait)