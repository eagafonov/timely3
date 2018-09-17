import time

from timely3.context_stack import context_stack
from timely3.stop_watch import stop_watch
from timely3._report import log_reporter

import logging

log = logging.getLogger(__name__)


class context_manager:
    stack = context_stack()
    journal = list()
    sw = stop_watch()
    reporter = log_reporter

    @classmethod
    def _reset(cls):
        cls.sw.reset()
        cls.journal = list()

    def __enter__(self):
        self.start_ts = time.perf_counter()

        self.stack.push(self.scope)

        return self

    def __exit__(self, *args, **kwargs):
        self.end_ts = time.perf_counter()
        duration = self.end_ts - self.start_ts

        with self.sw as w:
            scopes = tuple(self.stack.items())

            scope = self.stack.pop()

            assert scope == self.scope, ("Scope error", scope, self.scope)

            self.journal.append((scopes, duration))

            if self.stack.empty():
                if context_manager.reporter:
                    context_manager.reporter(self.journal)

        if self.stack.empty():
            log.debug("[PERF] SW:%s", w)
            self._reset()
