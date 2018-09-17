import functools
import sys

from timely3._report import report as report
from timely3._context_manager import context_manager


import logging

log = logging.getLogger(__name__)


LOG_SCOPE = False
# LOG_SCOPE = True


class timely3(context_manager):
    """
        top-level class to interact with timely3.
        It acts as decorator or context manager
    """
    def __init__(self, scope=None):
        if scope is None:
            f = sys._getframe(1)  # caller's frame
            glob_name = f.f_globals.get('__name__', '')

            if LOG_SCOPE:
                log.debug("[SCOPE] Frame __name__:%s %s:%s",
                          glob_name,
                          f.f_code.co_filename, f.f_lineno)

            if glob_name != '__main__':
                scope = "%s:%s" % (glob_name, f.f_lineno)
            else:
                scope = "%s:%s" % (f.f_code.co_filename, f.f_lineno)

        self.scope = scope

    @staticmethod
    def report():
        return report()

    def __call__(self, func=None):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return _wrapper


__all__ = [
    timely3,
    report,
]
