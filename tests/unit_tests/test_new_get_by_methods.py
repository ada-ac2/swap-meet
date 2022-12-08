from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#------------- get_clothes_by_fabric tests -------------
def test_get_clothes_by_fabric_non_empty_return():
    item_a = Electronics()
    item_b = Clothing()
    item_c = Clothing()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    clothes = nad.get_clothes_by_fabric("Unknown")

    assert len(clothes) == 2
    assert item_b in clothes
    assert item_c in clothes
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_clothes_by_fabric_inventory_with_clothing_no_fabric_match():
    item_a = Electronics()
    item_b = Clothing()
    item_c = Clothing()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    clothes = nad.get_clothes_by_fabric("wool")

    assert clothes == []
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_clothes_by_fabric_inventory_with_no_clothing():
    item_a = Electronics()
    item_b = Item()
    item_c = Item()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    clothes = nad.get_clothes_by_fabric("wool")

    assert clothes == []
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_clothes_by_fabric_inventory_with_empty_fabric():
    item_a = Electronics()
    item_b = Clothing()
    item_c = Clothing()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    clothes1 = nad.get_clothes_by_fabric("")
    clothes2 = nad.get_clothes_by_fabric(None)

    assert clothes1 == []
    assert clothes2 == []
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_clothes_by_fabric_no_inventory():
    nad = Vendor()

    clothes = nad.get_clothes_by_fabric("")

    assert clothes == []
    assert nad.inventory == []

#--- tests for get decors by space ------
def test_get_decors_by_space_non_empty_return():
    item_a = Decor()
    item_b = Decor()
    item_c = Clothing()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    decors = nad.get_decors_by_space((0,0))

    assert len(decors) == 2
    assert item_a in decors
    assert item_b in decors
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_decors_by_space_inventory_with_decors_no_space_match():
    item_a = Decor()
    item_b = Decor()
    item_c = Clothing()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    decors = nad.get_decors_by_space((1,2))

    assert decors == []
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_decors_by_space_inventory_with_no_decors():
    item_a = Electronics()
    item_b = Item()
    item_c = Item()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    decors = nad.get_decors_by_space((1,2))

    assert decors == []
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_decors_by_space_inventory_with_none_space():
    item_a = Electronics()
    item_b = Decor()
    item_c = Decor()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    decors = nad.get_decors_by_space(None)
    
    assert decors == []
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_decors_by_space_no_inventory():
    nad = Vendor()

    decors = nad.get_decors_by_space((1,2))

    assert decors == []
    assert nad.inventory == []

# ------- tests  get_electronics_by_type -------------------

def test_get_electronics_by_type_non_empty_return():
    item_a = Electronics()
    item_b = Clothing()
    item_c = Electronics()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = nad.get_electronics_by_type("Unknown")

    assert len(items) == 2
    assert item_a in items
    assert item_c in items
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_electronics_by_type_inventory_with_electronics_no_type_match():
    item_a = Electronics()
    item_b = Electronics()
    item_c = Clothing()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = nad.get_electronics_by_type("phone")

    assert items == []
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_electronics_by_type_inventory_with_no_electronics():
    item_a = Clothing()
    item_b = Item()
    item_c = Item()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = nad.get_electronics_by_type("wool")

    assert items == []
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_electronics_by_type_with_empty_type():
    item_a = Electronics()
    item_b = Clothing()
    item_c = Clothing()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    elec1 = nad.get_electronics_by_type("")
    elec2 = nad.get_electronics_by_type(None)

    assert elec1 == []
    assert elec2 == []
    assert nad.inventory == [item_a, item_b, item_c]

def test_get_electronics_by_type_no_inventory():
    nad = Vendor()

    clothes = nad.get_electronics_by_type("")

    assert clothes == []
