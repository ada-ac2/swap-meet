import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


# ~~~~~ swap_clothing_by_fabric Tests ~~~~~

def test_swap_clothing_by_fabric_returns_as_expected():
    item_a = Clothing(fabric="Striped")
    item_b = Clothing(fabric="Tulle")
    item_c = Clothing()
    item_d = Clothing(fabric="Tulle")
    item_e = Clothing(fabric="Silk")
    item_f = Clothing(fabric="Striped")

    vendor1 = Vendor([item_a, item_b, item_c])
    vendor2 = Vendor([item_d, item_e, item_f])

    result = vendor1.swap_clothing_by_fabric(vendor2, "Striped")
    assert result
    assert len(vendor1.inventory) == 3
    assert item_f in vendor1.inventory
    assert item_b in vendor1.inventory
    assert item_c in vendor1.inventory
    assert len(vendor2.inventory) == 3
    assert item_a in vendor2.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory

def test_swap_clothing_by_fabric_self_no_inventory_returns_falsy():
    item_d = Clothing(fabric="Tulle")
    item_e = Clothing(fabric="Silk")
    item_f = Clothing(fabric="Striped")

    vendor1 = Vendor()
    vendor2 = Vendor([item_d, item_e, item_f])

    result = vendor1.swap_clothing_by_fabric(vendor2, "Striped")
    assert not result 
    assert len(vendor1.inventory) == 0
    assert len(vendor2.inventory) == 3
    assert item_f in vendor2.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory

def test_swap_clothing_by_fabric_other_vendor_no_inventory_returns_falsy():
    item_d = Clothing(fabric="Tulle")
    item_e = Clothing(fabric="Silk")
    item_f = Clothing(fabric="Striped")

    vendor1 = Vendor()
    vendor2 = Vendor([item_d, item_e, item_f])

    result = vendor2.swap_clothing_by_fabric(vendor1, "Striped")
    assert not result 
    assert len(vendor1.inventory) == 0
    assert len(vendor2.inventory) == 3
    assert item_f in vendor2.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory

def test_swap_clothing_by_fabric_only_one_vendor_has_fabric_returns_falsy():
    item_d = Clothing(fabric="Tulle")
    item_e = Clothing(fabric="Silk")
    item_f = Clothing(fabric="Striped")
    item_g = Clothing(fabric="Silk")

    vendor1 = Vendor([item_g])
    vendor2 = Vendor([item_d, item_e, item_f])

    result = vendor1.swap_clothing_by_fabric(vendor2, fabric="Striped")
    assert not result 
    assert len(vendor1.inventory) == 1
    assert len(vendor2.inventory) == 3
    assert item_g in vendor1.inventory
    assert item_f in vendor2.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory

# ~~~~~ swap_decor_by_space_used Tests ~~~~~

def test_swap_decor_by_space_used_returns_as_expected():
    item_a = Decor(width=100, length=50)
    item_b = Decor(width=55, length=100)
    item_c = Decor(width=99, length=35)
    item_d = Decor(width=55, length=100)
    item_e = Decor()
    item_f = Decor(width=10, length=10)

    vendor1 = Vendor([item_a, item_b, item_c])
    vendor2 = Vendor([item_d, item_e, item_f])

    result = vendor1.swap_decor_by_space_used(vendor2, width=55, length=100)
    assert result
    assert len(vendor1.inventory) == 3
    assert item_a in vendor1.inventory
    assert item_c in vendor1.inventory
    assert item_d in vendor1.inventory
    assert len(vendor2.inventory) == 3
    assert item_f in vendor2.inventory
    assert item_b in vendor2.inventory
    assert item_e in vendor2.inventory

def test_swap_decor_by_space_used_self_no_inventory_returns_falsy():
    item_d = Decor(width=55, length=100)
    item_e = Decor()
    item_f = Decor(width=10, length=10)

    vendor1 = Vendor()
    vendor2 = Vendor([item_d, item_e, item_f])
    result = vendor1.swap_decor_by_space_used(vendor2, width=55, length=100,)

    assert not result 
    assert len(vendor1.inventory) == 0
    assert len(vendor2.inventory) == 3
    assert item_f in vendor2.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory

def test_swap_decor_by_space_used_other_vendor_no_inventory_returns_falsy():
    item_d = Decor(width=55, length=100)
    item_e = Decor()
    item_f = Decor(width=10, length=10)

    vendor1 = Vendor()
    vendor2 = Vendor([item_d, item_e, item_f])
    result = vendor2.swap_decor_by_space_used(vendor1, width=55, length=100,)

    assert not result 
    assert len(vendor1.inventory) == 0
    assert len(vendor2.inventory) == 3
    assert item_f in vendor2.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory

def test_swap_decor_by_space_used_only_one_vendor_has_space_used_returns_falsy():
    item_a = Decor(width=100, length=200)
    item_b = Decor(width=55, length=100)
    item_c = Decor(width=99, length=35)
    item_d = Decor(width=55, length=100)
    item_e = Decor()
    item_f = Decor(width=10, length=10)

    vendor1 = Vendor([item_a, item_b, item_c])
    vendor2 = Vendor([item_d, item_e, item_f])

    result = vendor2.swap_decor_by_space_used(vendor1, width=10, length=10)

    assert not result 
    assert len(vendor1.inventory) == 3
    assert len(vendor2.inventory) == 3
    assert item_a in vendor1.inventory
    assert item_b in vendor1.inventory
    assert item_c in vendor1.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory
    assert item_f in vendor2.inventory

# ~~~~~ swap_electronics_by_type Tests ~~~~~

def test_swap_electronics_by_type_returns_as_expected():
    item_a = Electronics(type = "TV")
    item_b = Electronics(type = "Phone")
    item_c = Electronics(type = "Laptop")
    item_d = Electronics(type = "VCR")
    item_e = Electronics(type = "Laptop")
    item_f = Electronics()

    vendor1 = Vendor([item_a, item_b, item_c])
    vendor2 = Vendor([item_d, item_e, item_f])

    result = vendor1.swap_electronics_by_type(vendor2, type="Laptop")

    assert result
    assert len(vendor1.inventory) == 3
    assert item_a in vendor1.inventory
    assert item_b in vendor1.inventory
    assert item_e in vendor1.inventory
    assert len(vendor2.inventory) == 3
    assert item_f in vendor2.inventory
    assert item_d in vendor2.inventory
    assert item_c in vendor2.inventory

def test_swap_electronics_by_type_self_no_inventory_returns_falsy():
    item_d = Electronics(type="VCR")
    item_e = Electronics()
    item_f = Electronics(type="TV")

    vendor1 = Vendor()
    vendor2 = Vendor([item_d, item_e, item_f])
    result = vendor1.swap_electronics_by_type(vendor2, type="Laptop")

    assert not result 
    assert len(vendor1.inventory) == 0
    assert len(vendor2.inventory) == 3
    assert item_f in vendor2.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory

def test_swap_electronics_by_type_other_vendor_no_inventory_returns_falsy():
    item_d = Electronics(type="Laptop")
    item_e = Electronics()
    item_f = Electronics(type="Phone")

    vendor1 = Vendor()
    vendor2 = Vendor([item_d, item_e, item_f])
    result = vendor2.swap_electronics_by_type(vendor1, "width=55, length=100",)

    assert not result 
    assert len(vendor1.inventory) == 0
    assert len(vendor2.inventory) == 3
    assert item_f in vendor2.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory

def test_swap_electronics_by_type_only_one_vendor_has_type_returns_falsy():
    item_a = Electronics(type="Laptop")
    item_b = Electronics(type="Laptop")
    item_c = Electronics(type="Phone")
    item_d = Electronics(type="VCR")
    item_e = Electronics()
    item_f = Electronics(type="Tablet")

    vendor1 = Vendor([item_a, item_b, item_c])
    vendor2 = Vendor([item_d, item_e, item_f])

    result = vendor2.swap_electronics_by_type(vendor1, type="Phone")

    assert not result 
    assert len(vendor1.inventory) == 3
    assert len(vendor2.inventory) == 3
    assert item_a in vendor1.inventory
    assert item_b in vendor1.inventory
    assert item_c in vendor1.inventory
    assert item_d in vendor2.inventory
    assert item_e in vendor2.inventory
    assert item_f in vendor2.inventory