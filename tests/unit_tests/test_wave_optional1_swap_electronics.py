import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# ~~~~~ swap_electronics_by_type Tests ~~~~~

def test_swap_electronics_by_type_success_returns_true():
    # Arrange
    item_a = Electronics(type="Game Console")
    item_b = Electronics(type="Health Tracker")
    item_c = Electronics(type="Health Tracker")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics(type="Game Console")
    item_e = Electronics(type="Health Tracker")
    item_f = Electronics(type="Health Tracker")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_electronics_by_type(
        other_vendor=jesse,
        category="Electronics",
        type="Game Console"
    )

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_d in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

#self inventory no match type return false
def test_swap_electronicd_by_type_self_inventory_no_match_returns_false():
    # Arrange
    item_a = Electronics(type="Health Tracker")
    item_b = Electronics(type="Health Tracker")
    item_c = Electronics(type="Health Tracker")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics(type="Game Console")
    item_e = Electronics(type="Health Tracker")
    item_f = Electronics(type="Health Tracker")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    # Act
    result = tai.swap_electronics_by_type(
        other_vendor=jesse,
        category="Electronics",
        type="Game Console"
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
def test_swap_electronics_by_type_other_inventory_no_match_returns_false():
    # Arrange
    item_a = Electronics(type="Kitchen Appliance")
    item_b = Electronics(type="Game Console")
    item_c = Electronics(type="Game Console")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics(type="Kitchen Appliance")
    item_e = Electronics(type="Health Tracker")
    item_f = Electronics(type="Health Tracker")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_electronics_by_type(
        other_vendor=jesse,
        category="Electronics",
        type="Game Console"
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


# type = "Unknown" no match 
def test_swap_electronics_by_type_no_match_unknown_returns_false():
    # Arrange
    item_a = Electronics(type="Kitchen Appliance")
    item_b = Electronics(type="Game Console")
    item_c = Electronics(type="Game Console")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics(type="Kitchen Appliance")
    item_e = Electronics(type="Health Tracker")
    item_f = Electronics(type="Health Tracker")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_electronics_by_type(
        other_vendor=jesse,
        category="Electronics",
        type="Unknown"
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

#items default type  = "Known" return true
def test_swap_clothing_by_fabric_default_returns_true():
    # Arrange
    item_a = Electronics()
    item_b = Electronics()
    item_c = Electronics()
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics()
    item_e = Electronics()
    item_f = Electronics()
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_electronics_by_type(
        other_vendor=jesse,
        category="Electronics",
        type="Unknown"
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
def test_swap_electronics_self_inventory_empty_returns_false():
    # Arrange
    
    tai = Vendor()

    item_d = Electronics()
    item_e = Electronics()
    item_f = Clothing()
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_electronics_by_type(
        other_vendor=jesse,
        category="Electronics",
        type="Unknown"
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 0


    assert len(jesse.inventory) == 3
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d in jesse.inventory

# no match category
def test_swap_electronics_no_match_category_returns_false():
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
    result = tai.swap_electronics_by_type(
        other_vendor=jesse,
        category="Electronics",
        type="Unknown"
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