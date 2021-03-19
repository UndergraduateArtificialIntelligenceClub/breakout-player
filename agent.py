from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPool2D
import numpy as np

class Agent(object):
    def __init__(self):
        pass

    def sample(self, env) -> int:
        pass

    def learn(self, observation: np.array, reward: float):
        pass
