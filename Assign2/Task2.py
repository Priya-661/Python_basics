#Python code to count vowel in a string
#Function to count vowel
def count_vowels(input_string):

    # Initializing count variable to 0
    count = 0
    vowels = "aeiouAEIOU"
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage:
example_string = "Python is the dream language of any programmer, it is simple yet powerful!"
print(f"Number of vowels in '{example_string}':", count_vowels(example_string))
