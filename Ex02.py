from random import sample
def make_couples(list_of_unique_names:list[str],desired_number_of_couples:int)-> dict:
 if desired_number_of_couples * 2 > len(list_of_unique_names):
    print(" Not enough names to form the requested the number of couples!")
    return {}
  
 list_couples = {}
 for _ in range(desired_number_of_couples):
    pair = sample(list_of_unique_names,2)
    list_couples[pair[0]] = pair[1]
    list_of_unique_names.remove(pair[0])
    list_of_unique_names.remove(pair[1])
 return list_couples    
list_of_unique_names = ["Karel", "Ben", "Tim", "Ken", "Henk", "Lies", "Barbie", "Sandra", "Debbie"]
desired_number_of_couples = int(input("How many couples should be formed:?"))
result = make_couples(list_of_unique_names,desired_number_of_couples)
print(f" The Students are: {list_of_unique_names}")
print(f" Test -> result of the function : {result}")

for person,partner in result.items():
    print(f" {person}  {partner}")