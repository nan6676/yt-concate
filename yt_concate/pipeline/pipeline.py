from .steps.step import StepException #使用相對路徑


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print('Exception Happened:', e)
                break


