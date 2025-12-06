"""Functions to manage a users shopping cart items."""


def add_item(current_cart:dict, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in (items_to_add):
        if item in current_cart.keys():
            current_cart[item] += 1
        else:
            current_cart.setdefault(item, 1)
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return_dict:dict = {}
    return add_item(return_dict, (notes))


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    # return_dict = ideas  |dict(recipe_updates)
    return ideas  |dict(recipe_updates)


def sort_entries(cart:dict):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart:dict, aisle_mapping:dict):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    return_dict:dict = {}
    for key in aisle_mapping.keys():
        if key in cart.keys():
            aisle_mapping[key].insert(0, cart[key])
            return_dict.setdefault(key, aisle_mapping[key])
    return dict(sorted(return_dict.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    right:list = []
    for key in fulfillment_cart.keys():
        right = store_inventory[key]
        if (right[0] - fulfillment_cart[key][0]) <=0:
            right[0] =  'Out of Stock'
        else:
            right[0] = right[0] - fulfillment_cart[key][0]
        store_inventory.setdefault(key, right)
    return store_inventory

print(send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
                  {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}))