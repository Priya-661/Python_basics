def sort_dict_keys(dictionary):
    
    # Sort the keys of the dictionary in ascending order
    sorted_keys = sorted(dictionary.keys())
    return sorted_keys

# Example usage
example_dict = {'Apple': 2, 'Doughnut': 5, 'Dairymilk': 3}

# Call the function and print the result
sorted_keys = sort_dict_keys(example_dict)
print(sorted_keys)
