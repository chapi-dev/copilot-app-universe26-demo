"""Tiny shopping cart used as the demo target. Contains two deliberate bugs."""
from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float
    qty: int = 1


@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)

    def add(self, name: str, price: float, qty: int = 1) -> None:
        self.items.append(Item(name, price, qty))

    def subtotal(self) -> float:
        return sum(i.price * i.qty for i in self.items)

    def total(self, discount: float = 0.0) -> float:
        # BUG 1: discount larger than subtotal gives a negative total
        # BUG 2: float result is not rounded to cents
        return self.subtotal() - discount
