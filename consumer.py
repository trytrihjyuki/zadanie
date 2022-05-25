import logging

import cv2
import numpy as np
import threading

from common import mutex, queue_A, queue_B

logging.basicConfig(level=logging.NOTSET, format='[%(threadName)s] %(message)s')
logger = logging.getLogger()


class Consumer(threading.Thread):
    def __init__(self, n_frames: int):
        """
        Class for the reading and processing the frames collected from queue A.

        Args:
            n_frames: number of frames to process
        """
        super().__init__()
        self.name = 'Consumer'
        self._n_frames = n_frames

    def run(self):
        counter = 0
        while True:
            frame = None
            mutex.acquire()
            if queue_A.qsize():
                counter += 1
                frame = queue_A.get()
                logger.info(f'Got {counter}. frame from A queue.')
            mutex.release()

            if frame is not None:
                processed_frame = self.process(frame)
                queue_B.put(processed_frame)
                logger.info(f'Put {counter}. processed frame into B queue.')

            if counter >= self._n_frames:
                return

    def process(self, frame: np.ndarray) -> np.ndarray:
        """
        Function to process frames. It reduces the frame twice and applies a median filter.

        Args:
            frame: frame to process

        Returns:
            processed frame
        """
        width, height = int(frame.shape[1]/2), int(frame.shape[0]/2)
        frame = cv2.resize(frame, (width, height))
        frame = cv2.medianBlur(frame, 5)
        return frame