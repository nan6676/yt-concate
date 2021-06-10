from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod #投入項目一定要繼承
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):
    pass
