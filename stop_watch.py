import time
import traceback


class StopWatch:
    """
    Based on code from: Python Cookbook, 3rd edition, by David Beazley and Brian K. Jones (O’Reilly)
    """
    def __init__(self, name=None, time_method_parameter=time.perf_counter):
        if name is None:
            name = str(traceback.extract_stack(None, 2)[0][2])
        self.elapsed = 0.0
        self.time_method_parameter = time_method_parameter
        self._start = None
        self.name = name

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self.time_method_parameter()

    def end(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self.time_method_parameter()
        self.elapsed += end - self._start
        self._start = None
        print('{' + self.name + '}' + ' takes:', self.elapsed, 'seconds')

    def reset(self):
        self.elapsed = 0.0

    # @property
    def is_running(self):
        print(self._start is not None)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.end()
