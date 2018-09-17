from timely3 import timely3


class TestMeasure:
    def test_decorator_default_args(self):
        @timely3()
        def func2test():
            return 42

        assert func2test() == 42

    def test_decorator_with_some_args(self):
        @timely3('some_argument')
        def func2test():
            return 42

        assert func2test() == 42

    def test_decorator_class(self):
        @timely3()
        def func2test(a):
            return a * 2

        assert func2test(21) == 42
