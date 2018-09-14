import time

import logging

log = logging.getLogger(__name__)


class context_manager:
    def __enter__(self):
        self.start_ts = time.perf_counter()

        return self

    def __exit__(self, *args, **kwargs):
        self.end_ts = time.perf_counter()
        duration = self.end_ts - self.start_ts

        log.debug("%s %s", self.scope, duration)
