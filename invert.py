def invert_dictionary(dict):
    return {v: k for k, v in dict.items()}

original_dict = {'a': 1, 'b': 2, 'c': 3}
print(invert_dictionary(original_dict))
