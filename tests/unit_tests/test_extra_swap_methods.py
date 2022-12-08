from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# --- test_swap_decor_by_space tests -------

def test_swap_decor_by_space_returns_true_default_lenght_width():
    item_a = Decor()
    item_b = Decor()
    item_c = Decor()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor()
    item_e = Decor()
    maty = Vendor(
        inventory=[item_d, item_e]
    )
    
    result = nad.swap_decor_by_space_used(maty,(0,0),(0,0))

    assert result
    assert item_d in nad.inventory
    assert item_a not in nad.inventory
    assert item_b in nad.inventory
    assert item_c in nad.inventory
    assert len(nad.inventory) == 3

    assert item_a in maty.inventory
    assert item_d not in maty.inventory
    assert item_e in maty.inventory
    assert len(maty.inventory) == 2

def test_swap_decor_by_space_returns_true_non_default_lenght_width():
    item_a = Decor(length=2,width=1)
    item_b = Decor(length=3,width=4)
    item_c = Decor()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor(length=5,width=6)
    item_e = Decor(length=2,width=1)
    maty = Vendor(
        inventory=[item_d, item_e]
    )
    
    result = nad.swap_decor_by_space_used(maty,(2,1),(2,1))

    assert result
    assert item_e in nad.inventory
    assert item_a not in nad.inventory
    assert item_b in nad.inventory
    assert item_c in nad.inventory
    assert len(nad.inventory) == 3

    assert item_a in maty.inventory
    assert item_e not in maty.inventory
    assert item_d in maty.inventory
    assert len(maty.inventory) == 2

def test_swap_decor_by_space_no_matching_item_in_self():
    item_a = Decor()
    item_b = Decor()
    item_c = Decor()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor()
    item_e = Decor()
    maty = Vendor(
        inventory=[item_d, item_e]
    )
    
    result = nad.swap_decor_by_space_used(maty,(0,0),(1,2))

    assert not result
    assert len(nad.inventory) == 3
    assert nad.inventory == [item_a,item_b,item_c]

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]

def test_swap_decor_by_space_no_matching_item_in_other():
    item_a = Decor()
    item_b = Decor()
    item_c = Decor()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor()
    item_e = Decor()
    maty = Vendor(
        inventory=[item_d, item_e]
    )
    
    result = nad.swap_decor_by_space_used(maty,(1,2),(0,0))

    assert not result
    assert len(nad.inventory) == 3
    assert nad.inventory == [item_a,item_b,item_c]

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]


def test_swap_decor_by_space_no_decor_items_in_self_inventory():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Decor()
    maty = Vendor(
        inventory=[item_d, item_e]
    )

    result = nad.swap_decor_by_space_used(maty,(0,0),(0,0))

    assert not result
    assert len(nad.inventory) == 3
    assert nad.inventory == [item_a,item_b,item_c]

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]

def test_swap_decor_by_space_no_decor_items_in_other_inventory():
    item_a = Item()
    item_b = Decor()
    item_c = Item()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Item()
    maty = Vendor(
        inventory=[item_d, item_e]
    )

    result = nad.swap_decor_by_space_used(maty,(0,0),(0,0))

    assert not result
    assert len(nad.inventory) == 3
    assert nad.inventory == [item_a,item_b,item_c]

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]

def test_swap_decor_by_space_no_self_inventory():
    nad = Vendor(
        inventory=[]
    )

    item_d = Item()
    item_e = Item()
    maty = Vendor(
        inventory=[item_d, item_e]
    )

    result = nad.swap_decor_by_space_used(maty,(0,0),(0,0))

    assert not result
    assert len(nad.inventory) == 0
    assert nad.inventory == []

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]

def test_swap_decor_by_space_no_other_inventory():
    nad = Vendor(
        inventory=[]
    )

    item_d = Item()
    item_e = Item()
    maty = Vendor(
        inventory=[item_d, item_e]
    )

    result = maty.swap_decor_by_space_used(nad,(0,0),(0,0))

    assert not result
    assert len(nad.inventory) == 0
    assert nad.inventory == []

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]

# ----------tests for swaping clothes by fabric -----------------
def test_swap_clothing_by_fabric_returns_true_default_fabric():
    item_a = Clothing()
    item_b = Clothing()
    item_c = Clothing()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing()
    item_e = Clothing()
    maty = Vendor(
        inventory=[item_d, item_e]
    )
    
    result = nad.swap_clothing_by_fabric(maty,"Unknown")

    assert result
    assert item_d in nad.inventory
    assert item_a not in nad.inventory
    assert item_b in nad.inventory
    assert item_c in nad.inventory
    assert len(nad.inventory) == 3

    assert item_a in maty.inventory
    assert item_d not in maty.inventory
    assert item_e in maty.inventory
    assert len(maty.inventory) == 2


def test_swap_clothing_by_fabric_returns_true_non_default_fabric():
    item_a = Clothing(fabric="wool")
    item_b = Clothing()
    item_c = Clothing()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing()
    item_e = Clothing(fabric="wool")
    maty = Vendor(
        inventory=[item_d, item_e]
    )
    
    result = nad.swap_clothing_by_fabric(maty,"wool")

    assert result
    assert item_e in nad.inventory
    assert item_a not in nad.inventory
    assert item_b in nad.inventory
    assert item_c in nad.inventory
    assert len(nad.inventory) == 3

    assert item_a in maty.inventory
    assert item_e not in maty.inventory
    assert item_d in maty.inventory
    assert len(maty.inventory) == 2

def test_swap_clothing_by_fabric_no_matching_item_in_self():
    item_a = Clothing()
    item_b = Clothing()
    item_c = Decor()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(fabric="wool")
    item_e = Decor()
    maty = Vendor(
        inventory=[item_d, item_e]
    )
    
    result = nad.swap_clothing_by_fabric(maty,"wool")

    assert not result
    assert len(nad.inventory) == 3
    assert nad.inventory == [item_a,item_b,item_c]

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]

def test_swap_clothing_by_fabric_no_matching_item_in_other():
    item_a = Clothing(fabric="wool")
    item_b = Decor()
    item_c = Decor()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor()
    item_e = Clothing()
    maty = Vendor(
        inventory=[item_d, item_e]
    )
    
    result = nad.swap_clothing_by_fabric(maty,"wool")

    assert not result
    assert len(nad.inventory) == 3
    assert nad.inventory == [item_a,item_b,item_c]

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]


def test_swap_clothing_by_fabric_no_clothing_items_in_self_inventory():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Clothing()
    maty = Vendor(
        inventory=[item_d, item_e]
    )

    result = nad.swap_clothing_by_fabric(maty,"Unknown")

    assert not result
    assert len(nad.inventory) == 3
    assert nad.inventory == [item_a,item_b,item_c]

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]

def test_swap_clothing_by_fabric_no_clothing_items_in_other_inventory():
    item_a = Item()
    item_b = Clothing()
    item_c = Item()
    nad = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Item()
    maty = Vendor(
        inventory=[item_d, item_e]
    )

    result = nad.swap_clothing_by_fabric(maty,"wool")

    assert not result
    assert len(nad.inventory) == 3
    assert nad.inventory == [item_a,item_b,item_c]

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]

def test_swap_clothing_by_fabric_no_self_inventory():
    nad = Vendor(
        inventory=[]
    )

    item_d = Clothing()
    item_e = Clothing()
    maty = Vendor(
        inventory=[item_d, item_e]
    )

    result = nad.swap_clothing_by_fabric(maty,"Unknown")

    assert not result
    assert len(nad.inventory) == 0
    assert nad.inventory == []

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]

def test_swap_clothing_by_fabric_no_other_inventory():
    nad = Vendor(
        inventory=[]
    )

    item_d = Item()
    item_e = Item()
    maty = Vendor(
        inventory=[item_d, item_e]
    )

    result = maty.swap_clothing_by_fabric(nad,"Unknown")

    assert not result
    assert len(nad.inventory) == 0
    assert nad.inventory == []

    assert len(maty.inventory) == 2
    assert maty.inventory == [item_d, item_e]