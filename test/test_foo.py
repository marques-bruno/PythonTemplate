import unittest
from python_template.foo import Foo


class TestFoo(unittest.TestCase):

    def test_foo_with_param_0(self):
        foo = Foo()
        self.assertEqual(0, foo.foo(0))
