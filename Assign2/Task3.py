def longest_string(strings):

    # Check if the list is empty
    if not strings:  
        return None
    
    # Initialize the longest string to Empty String
    longest = ""

    for string in strings:
        if len(string) > len(longest):
            longest = string

    return longest

# Example usage
strings = ["India", "North America", "South  America", "Australia"]
print(longest_string(strings)) 
