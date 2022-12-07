from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics  
    
item_a = Decor(id=123)
item_b = Electronics(id=456)
item_c = Decor(id=789)
tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

item_d = Clothing(id=321)
item_e = Decor(id=654)
item_f = Clothing(id=987)
jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

result = tai.choose_and_swap_items(other_vendor=jesse)

print(result)