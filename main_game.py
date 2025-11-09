import random
print("welcome to hang-man game!")
list_of_words=[
    "banana",
    "monkey",
    "zoom",
    "cat",
    "dog",
    "avocado",
    "epic"
]
def choose_random_word(word_list:list):
    len_of_list=len(list_of_words)
    random_index=random.randint(a=0,b=len_of_list-1)
    return (list_of_words(random_index))




