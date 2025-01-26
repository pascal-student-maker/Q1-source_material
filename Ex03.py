import random
def select_random_gift(dict_wishlist_persons:dict[str,list[str]]):
    random_gift = {}
    for name,wishlist in dict_wishlist_persons.items():
            random_gift[name] = random.choice(wishlist)
    return random_gift  


dic_wishlist_persons = { "Stijn":["Bike", "headphones", "fitbit"], "Marie": ["Game", "bike", "screen",
"swimming band"], "Joerie": ["racing bike", "swimming band", "book"], "Henk":["Laptop", "Beer Omer",
"bike"]   }   

result  = select_random_gift(dic_wishlist_persons) 


print("Each person is randomly given a gift from their wish list. ")
print(" This is the result")

for name,wishlist in result.items():
    print(f" {name} -> {wishlist}")
    
    
       