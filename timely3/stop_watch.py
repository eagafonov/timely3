import time


class stop_watch:
    def __init__(self):
        self.reset()

    def reset(self):
        self.duration_total = 0
        self.count = 0

    def __enter__(self):
        self.start_ts = time.perf_counter()

        return self

    def __exit__(self, *args, **kwargs):
        self.duration = time.perf_counter() - self.start_ts
        self.duration_total += self.duration
        self.count += 1

    def __repr__(self):
        return "stop_watch(duration_total:%s count:%s)" % (self.duration, self.count)
