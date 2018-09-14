"""
    Sample code to test timely3
"""

import time
from pprint import pprint

from timely3 import timely3
import timely3 as timely3_module




import logging
log = logging.getLogger('timely3/simple')

logging.basicConfig(
    format='[%(name)s:%(lineno)s][%(levelname)s] %(message)s',
    level=logging.DEBUG,
)

log.setLevel(logging.DEBUG)


# Import after logger setup
from example_module.example_submodule import func_from_pkg_01, func_from_pkg_02


def func01():
    """
        Func with timed block
    """
    with timely3('deepest_block'):
        time.sleep(0.1)


@timely3()
def func02():
    """
        decorated function
    """
    time.sleep(0.2)


@timely3('super_duper')
def func03():
    """
        decorated function with custom scope name
    """
    time.sleep(0.3)



if __name__ == "__main__":
    with timely3():
        func01()
        func02()
        func03()
        func_from_pkg_01()
        func_from_pkg_02()

    # report

    # as module-level function
    pprint(timely3_module.report())

    # as method
    pprint(timely3().report())  # bad idea since add new scope

    # as staticmethod
    pprint(timely3.report())
