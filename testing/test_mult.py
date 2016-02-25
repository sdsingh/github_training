import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import multiply as mult


def test_multiply1():
    assert mult.multiply(1, 2) == 2


def test_multiply2():
    assert mult.multiply(4) == 16
