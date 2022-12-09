import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_id_string_fails_with_type_error():
    #Act
    with pytest.raises(TypeError):
        item = Item(id="12345")

def test_id_list_fails_with_type_error():
    #Act
    with pytest.raises(TypeError):
        item = Item(id=["12345"])

def test_fabric_list_fails_with_type_error():
    #Act
    with pytest.raises(TypeError):
        clothing = Clothing(id=12345, fabric=["Pinstriped"])
    

def test_fabric_int_fails_with_type_error():
    #Act
    with pytest.raises(TypeError):
        clothing = Clothing(id=12345, fabric=88888)  

