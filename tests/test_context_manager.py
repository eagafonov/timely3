from timely3 import timely3

# import time


class TestContextManager:
    def test_scope_default(self):
        # expected result is a linked to this line number
        assert timely3().scope == "test_context_manager:9"

    def test_scope_argument(self):
        assert timely3("the_scope").scope == "the_scope"

    def test_default_scope(self):
        with timely3():
            pass

    def test_scope_after_exit(self, caplog):
        with timely3("test_me_after_exit") as t:
            assert t.scope == "test_me_after_exit"

        assert t.scope == "test_me_after_exit"
