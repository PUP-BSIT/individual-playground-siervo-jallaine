def first_key_with_highest_value(dict):
    highest_value = max(dict.values())
    for key, value in dict.items():
        if value == highest_value:
            return key

scores = {'John': 82, 'Alice': 92, 'Bob': 85, 'Charlie': 92}
print(first_key_with_highest_value(scores)) 


def invert_dictionary(input_dict):
    return {v: k for k, v in input_dict.items()}

original_dict = {'a': 1, 'b': 2, 'c': 3}
print(invert_dictionary(original_dict))


def dict_to_list_of_tuples(dict):
    return list(dict.items())

original_dict = {'a': 1, 'b': 2, 'c': 3}
print(dict_to_list_of_tuples(original_dict)) 

