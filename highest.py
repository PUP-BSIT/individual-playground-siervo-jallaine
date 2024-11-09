def first_key_with_highest_value(dict):
    highest_value = max(dict.values())
    for key, value in dict.items():
        if value == highest_value:
            return key

scores = {'John': 82, 'Alice': 92, 'Bob': 85, 'Charlie': 92}
print(first_key_with_highest_value(scores)) 
