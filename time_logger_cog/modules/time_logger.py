import datetime
import time

from up.base_thread_module import BaseThreadModule


class TimeLogger(BaseThreadModule):
    def __init__(self):
        super().__init__()

    def _execute_initialization(self):
        super()._execute_initialization()

    def _execute_start(self):
        super()._execute_start()
        return True

    def _execute_stop(self):
        super()._execute_stop()

    def _loop(self):
        while self._run:
            self.logger.info(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            time.sleep(0.5)
        self.__is_connected = False

    def load(self):
        return True
