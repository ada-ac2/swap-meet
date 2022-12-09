import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# ~~~~~ swap_clothing_by_fabric Tests ~~~~~

def test_swap_clothing_by_fabric_success_returns_true():
    # Arrange
    item_a = Clothing(fabric="Cotton")
    item_b = Clothing(fabric="Leather")
    item_c = Clothing(fabric="Cotton")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(fabric="Striped")
    item_e = Clothing(fabric="Leather")
    item_f = Clothing(fabric="Cotton")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_fabric(
        other_vendor=jesse,
        category="Clothing",
        fabric="Cotton"
    )

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_f in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d in jesse.inventory

#self inventory no match fabric return false
def test_swap_clothing_by_fabric_self_inventory_no_match_returns_false():
    # Arrange
    item_a = Clothing(fabric="Cotton")
    item_b = Clothing(fabric="Leather")
    item_c = Clothing(fabric="Cotton")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(fabric="Striped")
    item_e = Clothing(fabric="Leather")
    item_f = Clothing(fabric="Cotton")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_fabric(
        other_vendor=jesse,
        category="Clothing",
        fabric="Striped"
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d in jesse.inventory

# other inventory no match fabric return false
def test_swap_clothing_by_fabric_other_inventory_no_match_returns_false():
    # Arrange
    item_a = Clothing(fabric="Cotton")
    item_b = Clothing(fabric="Leather")
    item_c = Clothing(fabric="Cotton")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(fabric="Cotton")
    item_e = Clothing(fabric="Cotton")
    item_f = Clothing(fabric="Cotton")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_fabric(
        other_vendor=jesse,
        category="Clothing",
        fabric="Leather"
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d in jesse.inventory


# fabric = "Unknown" no match 
def test_swap_clothing_by_fabric_no_match_unknown_returns_false():
    # Arrange
    item_a = Clothing(fabric="Cotton")
    item_b = Clothing(fabric="Leather")
    item_c = Clothing(fabric="Cotton")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(fabric="Leather")
    item_e = Clothing(fabric="Leather")
    item_f = Clothing(fabric="Cotton")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_fabric(
        other_vendor=jesse,
        category="Clothing",
        fabric="Unknown"
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d in jesse.inventory

#items default fabric  = "Known" return true
def test_swap_clothing_by_fabric_default_returns_true():
    # Arrange
    item_a = Clothing()
    item_b = Clothing()
    item_c = Clothing()
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing()
    item_e = Clothing()
    item_f = Clothing()
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_fabric(
        other_vendor=jesse,
        category="Clothing",
        fabric="Unknown"
    )

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_d in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory
    assert item_a in jesse.inventory

#self inventory empty
def test_swap_clothing_self_inventory_empty_returns_false():
    # Arrange
    
    tai = Vendor()

    item_d = Clothing()
    item_e = Clothing()
    item_f = Clothing()
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_fabric(
        other_vendor=jesse,
        category="Clothing",
        fabric="Unknown"
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 0


    assert len(jesse.inventory) == 3
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d in jesse.inventory

# no match category
def test_swap_clothing_no_match_category_returns_false():
    # Arrange
    item_a = Clothing()
    item_b = Clothing()
    item_c = Clothing()
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor()
    item_e = Decor()
    item_f = Decor()
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_fabric(
        other_vendor=jesse,
        category="Clothing",
        fabric="Unknown"
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory


    assert len(jesse.inventory) == 3
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d in jesse.inventory
