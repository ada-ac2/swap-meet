import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# ~~~~~ swap_by_category_attribute Tests ~~~~~
# ~~~~~ swap decor by area Tests ~~~~~
def test_swap__when_no_matching_area_returns_false():
    # Arrange
    item_a = Decor(width=3, length=4)
    item_b = Decor(width=2, length=2)
    item_c = Decor(width=4, length=4)
    item_d = Decor(width=8, length=9)
    stewart = Vendor(inventory=[item_a, item_b])
    jenny = Vendor(inventory=[item_c, item_d])

    # Act
    result = stewart.swap_by_category_attribute(
        other_vendor=jenny,
        category='Decor',
        attr='area',
        attr_val=12
    )

    # Assert
    assert result == False
    assert len(jenny.inventory) == 2
    assert len(stewart.inventory) == 2
    assert item_a and item_b in stewart.inventory
    assert item_c and item_d in jenny.inventory

def test_swap_decor_when_matching_areas_returns_true():
    # Arrange
    item_a = Decor(width=3, length=4)
    item_b = Decor(width=2, length=2)
    item_c = Decor(width=4, length=3)
    item_d = Decor(width=8, length=9)
    stewart = Vendor(inventory=[item_a, item_b])
    jenny = Vendor(inventory=[item_c, item_d])

    # Act
    result = stewart.swap_by_category_attribute(
        other_vendor=jenny,
        category='Decor',
        attr='area',
        attr_val=12
    )

    # Assert
    assert result == True
    assert len(jenny.inventory) == 2
    assert len(stewart.inventory) == 2
    assert item_c and item_b in stewart.inventory
    assert item_a and item_d in jenny.inventory

def test_swap_best_decor_when_multiple_matching_areas():
    # Arrange
    item_a = Decor(width=3, length=4, condition=1)
    item_b = Decor(width=3, length=4, condition=4)#
    item_c = Decor(width=4, length=3)#
    item_d = Decor(width=8, length=9)
    stewart = Vendor(inventory=[item_a, item_b])
    jenny = Vendor(inventory=[item_c, item_d])

    # Act
    result = stewart.swap_by_category_attribute(
        other_vendor=jenny,
        category='Decor',
        attr='area',
        attr_val=12
    )

    # Assert
    assert result == True
    assert len(jenny.inventory) == 2
    assert len(stewart.inventory) == 2
    assert item_a and item_c in stewart.inventory
    assert item_b and item_d in jenny.inventory

# ~~~~~ swap clothing by fabric Tests ~~~~~
def test_swap_clothing_with_no_matching_fabrics_returns_false():
    # Arrange
    item_a = Clothing(fabric='silk')
    item_b = Decor(width=2, length=2)
    item_c = Clothing(fabric='wool')
    item_d = Decor(width=8, length=9)
    stewart = Vendor(inventory=[item_a, item_b])
    jenny = Vendor(inventory=[item_c, item_d])

    # Act
    result = stewart.swap_by_category_attribute(
        other_vendor=jenny,
        category='Clothing',
        attr='fabric',
        attr_val='wool'
    )

    # Assert
    assert result == False
    assert len(jenny.inventory) == 2
    assert len(stewart.inventory) == 2
    assert item_a and item_b in stewart.inventory
    assert item_c and item_d in jenny.inventory

def test_swap_clothing_when_matching_fabrics_returns_True():
    # Arrange
    item_a = Clothing(fabric='silk')
    item_b = Decor(width=2, length=2)
    item_c = Clothing(fabric='wool')
    item_d = Decor(width=8, length=9)
    item_e = Clothing(fabric='silk')
    stewart = Vendor(inventory=[item_a, item_b])
    jenny = Vendor(inventory=[item_c, item_d, item_e])

    # Act
    result = stewart.swap_by_category_attribute(
        other_vendor=jenny,
        category='Clothing',
        attr='fabric',
        attr_val='silk'
    )

    # Assert
    assert result == True
    assert len(jenny.inventory) == 3
    assert len(stewart.inventory) == 2
    assert item_e and item_b in stewart.inventory
    assert item_a, item_c and item_d in jenny.inventory

def test_swap_best_clothing_when_multiple_matching_fabrics():
    # Arrange
    item_a = Clothing(fabric='silk')
    item_b = Decor(width=2, length=2)
    item_c = Clothing(fabric='wool')
    item_d = Decor(width=8, length=9)
    item_e = Clothing(fabric='silk')
    stewart = Vendor(inventory=[item_a, item_b])
    jenny = Vendor(inventory=[item_c, item_d, item_e])

    # Act
    result = stewart.swap_by_category_attribute(
        other_vendor=jenny,
        category='Clothing',
        attr='fabric',
        attr_val='silk'
    )

    # Assert
    assert result == True
    assert len(jenny.inventory) == 3
    assert len(stewart.inventory) == 2
    assert item_e and item_b in stewart.inventory
    assert item_a, item_c and item_d in jenny.inventory

# ~~~~~ swap electronics by type Tests ~~~~~
def test_swap_electronics_with_no_matching_type_returns_false():
    # Arrange
    item_a = Electronics(type='computer')
    item_b = Decor(width=2, length=2)
    item_c = Clothing(fabric='wool')
    item_d = Electronics(type='headphones')
    stewart = Vendor(inventory=[item_a, item_b])
    jenny = Vendor(inventory=[item_c, item_d])

    # Act
    result = stewart.swap_by_category_attribute(
        other_vendor=jenny,
        category='Electronics',
        attr='type',
        attr_val='electric toothbrush'
    )

    # Assert
    assert result == False
    assert len(jenny.inventory) == 2
    assert len(stewart.inventory) == 2
    assert item_a and item_b in stewart.inventory
    assert item_c and item_d in jenny.inventory

def test_swap_electronics_when_matching_types_returns_True():
    # Arrange
    item_a = Electronics(type='computer')
    item_b = Decor(width=2, length=2)
    item_c = Clothing(fabric='wool')
    item_d = Electronics(type='computer')
    stewart = Vendor(inventory=[item_a, item_b])
    jenny = Vendor(inventory=[item_c, item_d])

    # Act
    result = stewart.swap_by_category_attribute(
        other_vendor=jenny,
        category='Electronics',
        attr='type',
        attr_val='computer'
    )

    # Assert
    assert result == True
    assert len(jenny.inventory) == 2
    assert len(stewart.inventory) == 2
    assert item_d and item_b in stewart.inventory
    assert item_a and item_c in jenny.inventory

def test_swap_best_electronics_when_multiple_matching_types():
    # Arrange
    item_a = Electronics(type='computer', condition=3)
    item_b = Electronics(type='computer', condition=2)
    item_c = Clothing(fabric='wool')
    item_d = Electronics(type='computer')
    stewart = Vendor(inventory=[item_a, item_b])
    jenny = Vendor(inventory=[item_c, item_d])

    # Act
    result = stewart.swap_by_category_attribute(
        other_vendor=jenny,
        category='Electronics',
        attr='type',
        attr_val='computer'
    )

    # Assert
    assert result == True
    assert len(jenny.inventory) == 2
    assert len(stewart.inventory) == 2
    assert item_d and item_b in stewart.inventory
    assert item_a and item_c in jenny.inventory

# ~~~~~ Test invalid id inputs ~~~~~
def test_string_id_input_in_different_items():
    # Arrange
    string_id = "4068793"

    # Act
    item_a = Clothing(id=string_id)
    item_b = Decor(id=string_id)
    item_c = Electronics(id=string_id)
    item_d = Item(id=string_id)

    # Assert
    item_a.id, item_b.id, item_c.id, item_d.id == 4068793

def test_float_id():
    # Arrange
    string_id = 0.84937
    
    # Assert
    with pytest.raises(ValueError):
        item_a = Clothing(id=string_id)
        item_b = Decor(id=string_id)
        item_c = Electronics(id=string_id)
        item_d = Item(id=string_id)

def test_nonnumeric_string_id():
    # Arrange
    string_id = "!89a"
    
    # Assert
    with pytest.raises(ValueError):
        item_a = Clothing(id=string_id)
        item_b = Decor(id=string_id)
        item_c = Electronics(id=string_id)
        item_d = Item(id=string_id)

def test_empty_string_id():
    # Arrange
    string_id = ""
    
    # Act
    item_a = Clothing(id=string_id)
    item_b = Decor(id=string_id)
    item_c = Electronics(id=string_id)
    item_d = Item(id=string_id)

    # Assert
    assert [type(item) == int for item in [item_a.id, item_b.id, item_c.id, item_d]]