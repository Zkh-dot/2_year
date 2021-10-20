import time
import contextlib


class cm_timer_1:
    def enter(self):
        self.start_time = time.time()

    def exit(self, exc_type, exc_val, exc_tb):
        print('time: ', time.time() - self.start_time)


@contextlib.contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    print('time: ', time.time() - start_time)


with cm_timer_1():
    time.sleep(0)

with cm_timer_2():
    time.sleep(0)