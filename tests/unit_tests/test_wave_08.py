import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# ~~~~swap_similar_items Test ~~~~~

def test_no_similar_item():
    # Arrange
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    item_d = Item(id=100)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    item_e = Decor(id=234, width=2, length=4)
    item_f = Electronics(id=405, type="Handheld Game")
    item_g = Decor(id=909, width=1, length=6)
    item_h = Clothing(id=3567, fabric="Wool")
    jesse = Vendor(
        inventory=[item_e, item_f, item_g, item_h]
    )

    #Act

    result = vendor.swap_similar_items(jesse, item_a)

    #Assert
    assert not result
    assert item_a in vendor.inventory
    assert item_a not in jesse.inventory

def test_no_matching_category():
    # Arrange
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    item_d = Item(id=100)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    item_e = Decor(id=234, width=2, length=4)
    item_f = Decor(id=909, width=1, length=6)
    item_g = Clothing(id=3567, fabric="Wool")
    jesse = Vendor(
        inventory=[item_e, item_f, item_g]
    )

    #Act

    result = vendor.swap_similar_items(jesse, item_a)

    #Assert
    assert not result
    assert len(vendor.inventory) == 4
    assert len(jesse.inventory) == 3


def test_one_matching_similar_clothing():
    # Arrange
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    item_d = Item(id=100)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    item_e = Decor(id=234, width=2, length=4)
    item_f = Electronics(id=405, type="Handheld Game")
    item_g = Decor(id=909, width=1, length=6)
    item_h = Clothing(id=3567, fabric="Wool")
    item_i = Clothing(id=12344, fabric="Striped")
    jesse = Vendor(
        inventory=[item_e, item_f, item_g, item_h, item_i]
    )

    #Act

    result = vendor.swap_similar_items(jesse, item_a)

    #Assert
    assert result
    assert item_a in jesse.inventory
    assert item_i in vendor.inventory
    assert len(jesse.inventory) == 5
    assert len(vendor.inventory) == 4

def test_two_matching_similar_decor():
    # Arrange
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    item_d = Item(id=100)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    item_e = Decor(id=234, width=4, length=2)
    item_f = Electronics(id=405, type="Handheld Game")
    item_g = Decor(id=909, width=1, length=6)
    item_h = Clothing(id=3567, fabric="Wool")
    item_i = Decor(id=12344, width=4, length=2)
    jesse = Vendor(
        inventory=[item_e, item_f, item_g, item_h, item_i]
    )

    #Act

    result = vendor.swap_similar_items(jesse, item_c)

    #Assert
  
    assert result
    assert item_c in jesse.inventory
    assert item_e in vendor.inventory or item_i in vendor.inventory
    assert len(jesse.inventory) == 5
    assert len(vendor.inventory) == 4

def test_one_matching_electronics():
    # Arrange
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    item_d = Item(id=100)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    item_e = Decor(id=234, width=2, length=4)
    item_f = Electronics(id=405, type="Handheld Game")
    item_g = Decor(id=909, width=1, length=6)
    item_h = Clothing(id=3567, fabric="Wool")
    item_i = Clothing(id=12344, fabric="Striped")
    jesse = Vendor(
        inventory=[item_e, item_f, item_g, item_h, item_i]
    )

    #Act

    result = vendor.swap_similar_items(jesse, item_b)

    #Assert
    assert result
    assert item_b in jesse.inventory
    assert item_f in vendor.inventory
    assert len(jesse.inventory) == 5
    assert len(vendor.inventory) == 4