import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_swap_by_similar_fabric_success_returns_true():
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321, fabric="Striped")
    item_e = Decor(id=654, width=3, length=5)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_similar(
        other_vendor=jesse,
        my_attributes="Striped",
        their_attributes="Striped"
    )

    # Assert
    assert result

    assert len(tai.inventory) == 3
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

#@pytest.mark.skip
def test_swap_by_similar_space_used_success_returns_true():
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321, fabric="Striped")
    item_e = Decor(id=654, width=2, length=4)
    item_f = Clothing(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_similar(
        other_vendor=jesse,
        my_attributes="2 by 4",
        their_attributes="2 by 4"
    )

    # Assert
    assert result

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_e in tai.inventory
    assert item_b in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_c in jesse.inventory
    assert item_f in jesse.inventory

#@pytest.mark.skip
def test_swap_by_similar_type_success_returns_true():
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321, fabric="Striped")
    item_e = Decor(id=654, width=3, length=5)
    item_f = Electronics(id=987, type="Handheld Game")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_similar(
        other_vendor=jesse,
        my_attributes="Handheld Game",
        their_attributes="Handheld Game"
    )

    # Assert
    assert result

    assert len(tai.inventory) == 3
    assert item_f in tai.inventory
    assert item_c in tai.inventory
    assert item_a in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d in jesse.inventory

#@pytest.mark.skip
def test_swap_by_similar_no_my_attributes_returns_false():
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456)
    item_c = Decor(id=789, width=2, length=4)
    
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321, fabric="Striped")
    item_e = Decor(id=654, width=3, length=5)
    item_f = Electronics(id=987, type="Handheld Game")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_similar(
        other_vendor=jesse,
        my_attributes="Handheld Game",
        their_attributes="Handheld Game"
    )

    # Assert
    assert not result

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

#@pytest.mark.skip
def test_swap_by_similar_no_their_attributes_returns_false():
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(id=321, fabric="Striped")
    item_e = Decor(id=654, width=3, length=5)
    item_f = Electronics(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_similar(
        other_vendor=jesse,
        my_attributes="Handheld Game",
        their_attributes="Handheld Game"
    )

    # Assert
    assert not result

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

#@pytest.mark.skip
def test_swap_by_similar_empty_my_inventory_returns_false(): 
    tai = Vendor(
        inventory=[]
    )

    item_d = Clothing(id=321, fabric="Striped")
    item_e = Decor(id=654, width=3, length=5)
    item_f = Electronics(id=987)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_similar(
        other_vendor=jesse,
        my_attributes="Handheld Game",
        their_attributes="Handheld Game"
    )

    # Assert
    assert not result

    assert len(tai.inventory) == 0

    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

#@pytest.mark.skip
def test_swap_by_similar_empty_their_inventory_returns_false():
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_similar(
        other_vendor=jesse,
        my_attributes="Handheld Game",
        their_attributes="Handheld Game"
    )

    # Assert
    assert not result

    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert len(jesse.inventory) == 0
