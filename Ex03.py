import random

def select_random_gift(dict_wishlist_persons: dict[str, list[str]]) -> dict[str, str]:
    """
    Randomly selects a gift for each person from their wishlist.
    """
    gifts = {}
    
    # Loop through each person and their wishlist
    for name, wishlist in dict_wishlist_persons.items():
        # Select a random gift from their wishlist
        random_gift = random.choice(wishlist)
        # Assign the gift to the person
        gifts[name] = random_gift
    
    return gifts
