import threading
from machine_learning.prediction.new_algorithm.ml_functions import initialize


# Initializes the training of the ML-model to shorten the loading time.
class ThreadingInitialize(object):

    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()                                  # Start the execution

    def run(self):
        initialize()
