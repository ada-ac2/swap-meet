import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

@pytest.mark.skip
@pytest.mark.integration_test
def test_integration_wave_01_02_03():
    # make a vendor  
    vendor = Vendor()
    assert len(vendor.inventory) == 0

    # add an item
    item1 = Item()
    item2 = Item()
    result1 = vendor.add(item1)
    result2 = vendor.add(item2)

    assert len(vendor.inventory) == 2
    assert item1 in vendor.inventory
    assert item2 in vendor.inventory
    assert result1 == item1
    assert result2 == item2

    # remove an item
    remove_result = vendor.remove(item1)

    assert len(vendor.inventory) == 1
    assert item1 not in vendor.inventory
    assert remove_result == item1

    other_vendor = Vendor()

    # swap items
    item3 = Item()
    other_vendor.add(item3)

    vendor.swap_items(other_vendor, item2, item3)

    assert len(vendor.inventory) == 1
    assert len(other_vendor.inventory) == 1
    assert item2 in other_vendor.inventory
    assert item3 in vendor.inventory


