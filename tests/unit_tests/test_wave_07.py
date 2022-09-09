import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# ~~~~~ display_inventory Tests ~~~~~

@pytest.mark.skip
def test_display_inventory_with_items_no_category(capfd):
    # Arrange
    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    item_d = Item(id=000)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    # Act
    vendor.display_inventory()

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "1. An object of type Clothing with id 123. It is made from Striped fabric..\n"
        "2. An object of type Electronics with id 456. This is a Handheld Game device.\n"
        "3. An object of type Decor with id 789. It takes up a 2 by 4 sized space.\n"
        "4. An object of type Item with id 000\n"
    )
    assert captured.out == expected_str

@pytest.mark.skip
def test_display_inventory_with_items_and_category(capfd):
    # Arrange
    item_a = Decor(id=123, width=2, length=4)
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=1, length=6)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    vendor.display_inventory(category="Decor")

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "1. An object of type Decor with id 123. It takes up a 2 by 4 sized space.\n"
        "2. An object of type Decor with id 789. It takes up a 1 by 6 sized space.\n"
    )
    assert captured.out == expected_str

@pytest.mark.skip
def test_display_inventory_with_category_and_no_matching_items(capfd):
    # Arrange
    item_a = Decor(id=123, width=2, length=4)
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=1, length=6)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    vendor.display_inventory(category="Clothing")

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "No inventory to display.\n"
    )
    assert captured.out == expected_str

@pytest.mark.skip
def test_display_inventory_no_items_no_category(capfd):
    # Arrange
    vendor = Vendor(inventory=[])

    # Act
    vendor.display_inventory()

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "No inventory to display.\n"
    )
    assert captured.out == expected_str

@pytest.mark.skip
def test_display_inventory_no_items_with_category(capfd):
    # Arrange
    vendor = Vendor(inventory=[])

    # Act
    vendor.display_inventory(category="Decor")

    # Assert
    captured = capfd.readouterr()
    expected_str = (
        "No inventory to display.\n"
    )
    assert captured.out == expected_str

# ~~~~~ swap_by_id Tests ~~~~~

# successful swap
# calling inventory empty
# other inventory empty
# calling inventory missing item
# other inventory missing item 

# ~~~~~ choose_and_swap_items Tests ~~~~~

# Successful swap
# calling inventory empty
# other inventory empty
# calling inventory missing item
# other inventory missing item 