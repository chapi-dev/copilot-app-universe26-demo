import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from cart import Cart  # noqa: E402


def test_subtotal():
    c = Cart()
    c.add("pen", 1.5, 2)
    assert c.subtotal() == 3.0


def test_discount_never_negative():
    c = Cart()
    c.add("pen", 1.0)
    assert c.total(discount=5.0) == 0.0


def test_total_rounded_to_cents():
    c = Cart()
    c.add("a", 0.1, 3)
    assert c.total() == 0.30
