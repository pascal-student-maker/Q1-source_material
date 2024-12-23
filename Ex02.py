# Ex02
import random
# write here your function
def make_couples(unique_names:list[str],number_of_couples:int) -> dict[str,str]:
   if number_of_couples > len(unique_names) //2:
       print("Number of pairs can't be formed!")
       return {}
    
   random.shuffle(unique_names)
   
   couples = {}
   for _ in range(number_of_couples):
       first_name,second_name = random.sample(unique_names)
       couples[first_name] = second_name
       
       unique_names.remove(first_name)
       unique_names.remove(second_name)
       
       return  couples  



# test your function 
print("💘 The couples of  Howest are 💘")
students = ["Karel", "Ben", "Tim", "Ken", "Henk", "Lies", "Barbie", "Sandra", "Debbie"]
print("The students are",students)
number_couples = int(input("How many couples should be formed?:> "))

result = make_couples(students,number_couples)

if result:
    print("\nn💘 The couples of Howest are 💘")
    for first,second in result.items():
        print(f"{first} & {second}")