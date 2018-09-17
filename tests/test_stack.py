import pytest

from timely3.context_stack import context_stack


class TestStack:
    @pytest.fixture
    def stack(self):
        return context_stack()

    def test_empty(self, stack):
        assert stack.empty()
        assert stack.len() == 0

    def test_push_pop(self, stack):
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.len() == 3

        assert not stack.empty()

        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

        assert stack.len() == 0

        assert stack.empty()

    def test_items(self, stack):
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert list(stack.items()) == [1, 2, 3]

        assert not stack.empty()

    def test_items_reversed(self, stack):
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert list(stack.ritems()) == [3, 2, 1]

        assert not stack.empty()
