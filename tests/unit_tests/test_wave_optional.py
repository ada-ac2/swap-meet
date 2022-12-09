import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# ~~~~~ Test for swap_decor_by_size ~~~~~
def test_swap_decor_by_size():
    # Arrange
    item_a = Decor(id=779, width=2, length=4)
    item_b = Decor(id=789, width=4, length=3)
    item_c = Decor(id=799, width=2, length=4)
    item_d = Decor(id=809, width=4, length=3)

    my_vendor = Vendor(inventory=[item_a, item_b])
    their_vendor = Vendor(inventory=[item_c, item_d])

    # Act
    result = my_vendor.swap_decor_by_similiar_item(their_vendor)

    # Assert
    assert result 
    assert item_a in their_vendor.inventory
    assert item_c in my_vendor.inventory
    assert len(their_vendor.inventory) == 2
    assert len(my_vendor.inventory) == 2

def test_swap_decor_by_size_reordered():
    # Arrange
    item_a = Decor(id=779, width=4, length=2)
    item_b = Decor(id=789, width=4, length=3)
    item_c = Decor(id=799, width=2, length=4)
    item_d = Decor(id=809, width=4, length=3)

    my_vendor = Vendor(inventory=[item_a, item_b])
    their_vendor = Vendor(inventory=[item_c, item_d])

    # Act
    result = my_vendor.swap_decor_by_similiar_item(their_vendor)

    # Assert
    assert result 
    assert item_a in their_vendor.inventory
    assert item_c in my_vendor.inventory
    assert len(their_vendor.inventory) == 2
    assert len(my_vendor.inventory) == 2
    


# ~~~~~ Test for swap_clothings_by_fabric ~~~~~
def test_swap_clothings_by_fabric():
# Arrange
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Clothing(id=124, fabric="Floral")
    item_c = Clothing(id=125, fabric="Striped")
    item_d = Clothing(id=126, fabric="Cotton")

    my_vendor = Vendor(inventory=[item_a, item_b])
    their_vendor = Vendor(inventory=[item_c, item_d])

    # Act
    result = my_vendor.swap_decor_by_similiar_item(their_vendor)

    # Assert
    assert result 
    assert item_a in their_vendor.inventory
    assert item_c in my_vendor.inventory
    assert len(their_vendor.inventory) == 2
    assert len(my_vendor.inventory) == 2

# ~~~~~ Test for swap_electronics_by_type ~~~~~
def test_swap_electronics_by_type():
# Arrange
    item_a = Electronics(id=456, type="Handheld Game")
    item_b = Electronics(id=124, type="Kitchen Appliance")
    item_c = Electronics(id=125, type="Handheld Game")
    item_d = Electronics(id=126, type="Health Tracker")

    my_vendor = Vendor(inventory=[item_a, item_b])
    their_vendor = Vendor(inventory=[item_c, item_d])

    # Act
    result = my_vendor.swap_decor_by_similiar_item(their_vendor)

    # Assert
    assert result 
    assert item_a in their_vendor.inventory
    assert item_c in my_vendor.inventory
    assert len(their_vendor.inventory) == 2
    assert len(my_vendor.inventory) == 2