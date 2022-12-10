import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# ~~~~~ display_inventory Tests ~~~~~
def test_swap_similar_with_other_vendor():
    # Arrange
    # me
    item_a = Decor(width=2, length=2)
    item_b = Electronics(type="laptop")
    item_c = Decor(width=4, length=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(fabric="Silk")
    item_e = Decor(width=2, length=2)
    item_f = Clothing(fabric="Cashmere")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_similar_with_other_vendor(
        other_vendor=jesse,
        item=item_a
    )
    
    assert result is True
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_e in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_a in jesse.inventory
    assert item_f in jesse.inventory

def test_swap_similar_with_other_vendor_not_found():
    # Arrange
    # me
    item_a = Decor(width=2, length=2)
    item_b = Electronics(type="laptop")
    item_c = Decor(width=4, length=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(fabric="Silk")
    item_e = Decor(width=2, length=2)
    item_f = Clothing(fabric="Cashmere")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_similar_with_other_vendor(
        other_vendor=jesse,
        item=item_b
    )
    
    assert result is False
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

def test_bad_instance_id():
    with pytest.raises(ValueError):
        item1 = Decor(id="abcd")
        item2 = Clothing(id=[])
        item3 = Electronics(id=int)
