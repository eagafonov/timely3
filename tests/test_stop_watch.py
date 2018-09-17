import time

from timely3.stop_watch import stop_watch


class TestStopWatch():
    def test_01(self):
        with stop_watch() as w:
            time.sleep(0.1)

        assert w.duration >= 0.1
        assert w.duration <= 0.1 + 0.01

    def test_09(self):
        with stop_watch() as w:
            time.sleep(0.9)

        assert w.duration >= 0.9
        assert w.duration <= 0.9 + 0.01
