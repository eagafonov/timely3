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
from example_module.example_submodule import (   # noqa: E402
    func_from_pkg_01,
    func_from_pkg_02,
)


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
    assert timely3.sw.count == 0
    assert timely3.sw.duration_total == 0

    with timely3():
        func01()
        func02()
        func03()
        for _ in range(3):
            func01()
        func_from_pkg_01()
        func_from_pkg_02()

    assert timely3.sw.count == 0
    assert timely3.sw.duration_total == 0

    with timely3('second_top_level') as t1:
        assert t1.stack.len() == 1

        with timely3('sub_level') as t2:
            assert t1.stack.len() == 2
            assert t2.stack.len() == 2

            for _ in range(4):
                func02()

    assert timely3.sw.count == 0
    assert timely3.sw.duration_total == 0
    assert len(t2.journal) == 0

    # report

    # as module-level function
    pprint(timely3_module.report())

    # as method
    pprint(timely3().report())  # bad idea since add new scope

    # as staticmethod
    pprint(timely3.report())
