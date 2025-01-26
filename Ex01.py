from collections import Counter
def calculate_love_score(girlname:str,boyname:str) -> float:
    average_length =  (len(girlname) + len(boyname)) /2
    s1 = girlname
    s2 = boyname
     
    c1 = Counter(s1.lower())
    c2 = Counter(s2.lower())
    Number_of_shared_unique_letters = sum((c1 & c2).values())
    print(f" Number of shared unique letters: {Number_of_shared_unique_letters}")
    print(f" Average length of names : {average_length}")
    LoveScore = (Number_of_shared_unique_letters / average_length) * 100
    return LoveScore


girlname = input("Enter a girlname:").strip().lower()   
boyname = input("enter a boyname:").strip().lower()
result = calculate_love_score(girlname,boyname)

print(f" The lovescore between {girlname} and {boyname} is {result:.2f} %")
             
             
         
    