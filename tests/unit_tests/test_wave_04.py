import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item


def test_swap_first_item_returns_true():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Item()
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) == 3
    assert item_a not in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_a in jolie.inventory
    assert result


def test_swap_first_item_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item()
    item_e = Item()
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) == 0
    assert len(jolie.inventory) == 2
    assert not result


def test_swap_first_item_from_their_empty_returns_false():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) == 3
    assert len(jolie.inventory) == 0
    assert not result

def test_swap_first_item_when_items_are_the_same_returns_False():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_b, item_a, item_c]
    )

    item_d = Item()
    item_e = Item()
    item_f = item_b
    jolie = Vendor(
        inventory=[item_f, item_d, item_e]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) == 3
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert len(jolie.inventory) == 3
    assert item_d in jolie.inventory
    assert item_e in jolie.inventory
    assert item_f in jolie.inventory
    assert not result