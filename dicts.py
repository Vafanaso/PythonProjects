def create_inventory(items) -> dict:
    inventory:dict = {}
    for item in items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory
# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))
def add_items(inventory:dict, items:list) -> dict:
    # for item in items:
    #     if item in inventory:
    #         inventory[item] += 1
    #     else:
    #         inventory[item] = 1
    # return inventory.

    big_inventory = create_inventory(items)
    for key in inventory:
        if key not in big_inventory:
            big_inventory[key] = inventory[key]
        else:
            big_inventory[key] += inventory[key]
    return big_inventory
# print(add_items({"coal":1, "marble":2}, ["wood", "iron", "wood", "coal"]))

def decrement_items(inventory:dict, items:list) -> dict:
    for item in items:
        if item in inventory:
            if inventory[item] == 0:
                continue
            else:
                inventory[item] -= 1
    return inventory
# print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))

def remove_item(inventory:dict, item:str) -> dict:
    if item in inventory:
        inventory.pop(item)
    return inventory
# print(remove_item({"coal":2, "wood":1, "diamond":2}, "diamond"))

def list_inventory(inventory:dict) -> list:
    result:list = []
    for key in inventory:
        if inventory[key] != 0:
            result.append((key, inventory[key]))
    return result
# print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))