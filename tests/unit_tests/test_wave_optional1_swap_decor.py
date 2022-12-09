import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# ~~~~~ swap_decor_by_space Tests ~~~~~
def test_swap_decor_by_space_returns_true():
    # Arrange
    item_a = Decor(width=3, length=12)
    item_b = Decor(width=4, length=12)
    item_c = Decor(width=5, length=12)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor(width=3, length=12)
    item_e = Decor(width=4, length=12)
    item_f = Decor(width=7, length=12)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_decor_by_space(
        other_vendor=jesse,
        category="Decor",
        space = 36
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

#self inventory no match space return false
def test_swap_decor_by_space_self_inventory_no_match_returns_false():
    # Arrange
    item_a = Decor(width=3, length=12)
    item_b = Decor(width=4, length=12)
    item_c = Decor(width=5, length=12)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor(width=3, length=12)
    item_e = Decor(width=5, length=12)
    item_f = Decor(width=7, length=12)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_decor_by_space(
        other_vendor=jesse,
        category="Decor",
        space = 84
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

# other inventory no match space return false
def test_swap_decor_by_space_other_inventory_no_match_returns_false():
    # Arrange
    item_a = Decor(width=3, length=12)
    item_b = Decor(width=4, length=12)
    item_c = Decor(width=5, length=12)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor(width=3, length=12)
    item_e = Decor(width=5, length=12)
    item_f = Decor(width=7, length=12)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_decor_by_space(
        other_vendor=jesse,
        category="Decor",
        space = 48
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
def test_swap_decor_by_space_no_match_unknown_returns_false():
    # Arrange
    item_a = Decor(width=3, length=12)
    item_b = Decor(width=4, length=12)
    item_c = Decor(width=5, length=12)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor(width=3, length=12)
    item_e = Decor(width=5, length=12)
    item_f = Decor(width=7, length=12)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_decor_by_space(
        other_vendor=jesse,
        category="Decor",
        space = 0
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

#items default space = 0 return true
def test_swap_deor_by_space_default_returns_true():
    # Arrange
    item_a = Decor()
    item_b = Decor(width=4, length=12)
    item_c = Decor(width=5, length=12)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor()
    item_e = Decor(width=5, length=12)
    item_f = Decor(width=7, length=12)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_decor_by_space(
        other_vendor=jesse,
        category="Decor",
        space = 0
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
def test_swap_decor_self_inventory_empty_returns_false():
    # Arrange
    
    tai = Vendor(inventory=[])

    item_d = Decor()
    item_e = Decor(width=5, length=12)
    item_f = Decor(width=7, length=12)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_decor_by_space(
        other_vendor=jesse,
        category="Decor",
        space = 0
    )

    # Assert
    assert result == False

    assert len(tai.inventory) == 0


    assert len(jesse.inventory) == 3
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d in jesse.inventory

# no match category
def test_swap_decor_no_match_category_returns_false():
    # Arrange
    item_a = Clothing()
    item_b = Clothing()
    item_c = Clothing()
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
    result = tai.swap_decor_by_space(
        other_vendor=jesse,
        category="Decor",
        space = 0
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

def test_check_empty_inventory():
    #Arrange
    fatimah = Vendor(inventory=[]
    )
    #Act
    result = fatimah.check_inventory_empty()
    #Assert
    assert result == None

