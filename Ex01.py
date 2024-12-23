# Ex01
def calculate_love_score(first_name:str,second_name:str) -> float:
    set1 = set(first_name)
    set2 = set(second_name)
    common_chars = set1.intersection(set2)
    print(f"Shared unique letters: {','.join(common_chars)}")
    average_length_of_names = len(first_name) + len(second_name) / 2
    love_score = (len(common_chars)/ average_length_of_names) * 100
    return love_score

    



# test your function 
first_name = input("Enter a first name:> ")
second_name = input("Enter a second name:> ")


result = calculate_love_score(first_name,second_name)

print(f" the number of shared unique characters is: {len(set(first_name.lower()).intersection(set(second_name.lower())))}")
print(f"The love score between {first_name} and {second_name} is {calculate_love_score(first_name, second_name)} {result:.1f}%")


