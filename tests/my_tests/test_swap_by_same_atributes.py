import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

############################################################################
##                        testing swap clothing                           ##

def test_swap_clothing_by_same_attributes_success_returns_true():
    # Arrange
    item_a = Decor(id=123)
    item_b = Clothing(fabric = "Cotton")
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(fabric = "Cotton")
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory


def test_swap_all_clothing_by_same_attributes_success_returns_true():
    # Arrange
    item_a = Clothing(fabric = "Silk")
    item_b = Clothing(fabric = "Cotton")
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(fabric = "Cotton")
    item_e = Decor(id=654)
    item_f = Clothing(fabric = "Silk")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_all_clothing_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_f in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_e in jesse.inventory
    assert item_a in jesse.inventory


def test_swap_one_clothing_by_same_attributes_more_then_one_success_returns_true():
    # Arrange
    item_a = Decor(id=123)
    item_b = Clothing(fabric = "Cotton")
    item_c = Clothing(fabric = "Silk")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(fabric = "Cotton")
    item_e = Decor(id=654)
    item_f = Clothing(fabric = "Silk")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory


def test_swap_clothing_by_same_attributes_empty_my_inventory_returns_False():
    # Arrange
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(fabric = "Cotton")
    item_b = Decor(id=654)
    item_c = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    result = tai.swap_clothing_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_clothing_by_same_attributes_fails_if_caller_missing_item():
    # Arrange
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_b, item_c]
    )

    item_d = Clothing(id=321)
    item_e = Decor(id=654)
    item_f = Clothing(fabric = "Floral")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_clothing_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 2
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

def test_swap_clothing_by_same_attributes_fails_if_other_missing_item():
    # Arrange
    item_a = Clothing(fabric = "Cotton")
    item_b = Electronics(id=456)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_e = Decor(id=654)
    jesse = Vendor(
        inventory=[item_e]
    )

    # Act
    result = tai.swap_clothing_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 1
    assert item_e in jesse.inventory

############################################################################
##                        testing swap decor                              ##

def test_swap_decor_by_same_attributes_success_returns_true():
    # Arrange
    item_a = Decor(width = 10, length = 20)
    item_b = Clothing(fabric = "Cotton")
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(fabric = "Cotton")
    item_e = Decor(width = 10, length = 20)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_decor_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_e in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_d in jesse.inventory
    assert item_f in jesse.inventory

def test_swap_decor_by_same_attributes_empty_my_inventory_returns_False():
    # Arrange
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(fabric = "Cotton")
    item_b = Decor(id=654)
    item_c = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    result = tai.swap_decor_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_decor_by_same_attributes_fails_if_caller_missing_item():
    # Arrange
    item_a = Clothing(fabric = "Cotton")
    item_b = Electronics(id=456)
    tai = Vendor(
        inventory=[item_a, item_b]
    )

    item_d = Clothing(id=321)
    item_f = Clothing(fabric = "Floral")
    item_e = Decor(width = 10, length = 20)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_decor_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 2
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory

def test_swap_decor_by_same_attributes_fails_if_other_missing_item():
    # Arrange
    item_a = Clothing(fabric = "Cotton")
    item_b = Electronics(id=456)
    item_c = Decor(width = 10, length = 20)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_e = Clothing(id=654)
    jesse = Vendor(
        inventory=[item_e]
    )

    # Act
    result = tai.swap_decor_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 1
    assert item_e in jesse.inventory
############################################################################
##                      testing swap electronics                          ##

def test_swap_electronics_by_same_attributes_success_returns_true():
    # Arrange
    item_a = Electronics(type = "Phone")
    item_b = Electronics(type = "TV")
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics(type = "TV")
    item_e = Decor(id=654)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_electronics_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == True

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

def test_swap_electronics_by_same_attributes_empty_my_inventory_returns_False():
    # Arrange
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(fabric = "Cotton")
    item_b = Decor(id=654)
    item_c = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    result = tai.swap_electronics_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

def test_swap_electronics_by_same_attributes_fails_if_caller_missing_item():
    # Arrange
    item_a = Clothing(fabric = "Cotton")
    item_b = Decor(id=654)
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321)
    item_e = Electronics(type = "TV")
    item_f = Clothing(fabric = "Floral")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_electronics_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

def test_swap_electronics_by_same_attributes_fails_if_other_missing_item():
    # Arrange
    item_a = Clothing(fabric = "Cotton")
    item_b = Electronics(type = "TV")
    item_c = Decor(id=789)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_e = Decor(id=654)
    jesse = Vendor(
        inventory=[item_e]
    )

    # Act
    result = tai.swap_clothing_by_attributes(
        other_vendor=jesse)

    # Assert
    assert result == False

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 1
    assert item_e in jesse.inventory