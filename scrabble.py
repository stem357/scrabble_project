#!/usr/bin/env python
# coding: utf-8

# In[19]:


from wordscore import score_word
import os

def run_scrabble(rack):
    """
    Given a rack of 2-7 characters, finds all valid Scrabble words that can be made from the rack
    and returns the words along with their Scrabble scores.
    
    The function also handles wildcard characters ('*' and '?').
    
    Parameters:
    rack (str): A string containing 2 to 7 characters representing the Scrabble rack.
    
    Returns:
    tuple: A sorted list of (score, word) tuples and the total number of valid words, 
           or an error message if the input is invalid.
    """
    # Input validation
    if not isinstance(rack, str):
        return "Error: The rack must be a string."
    
    if not (2 <= len(rack) <= 7):
        return "Error: The rack must contain between 2 and 7 characters."

    # Handle non-alphabet characters other than wildcards
    allowed_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ*?")
    if any(char.upper() not in allowed_characters for char in rack):
        return "Error: The rack contains invalid characters. Only letters, '*' and '?' are allowed."
    
    # Check if there are more than 2 wildcards
    if rack.count('*') + rack.count('?') > 2:
        return "Error: Only up to two wildcards are allowed."

    # Load the list of valid Scrabble words from 'sowpods.txt'
    file_path = os.path.join(os.path.dirname(__file__), 'sowpods.txt')
    
    if not os.path.exists(file_path):
        return "Error: The word list file 'sowpods.txt' was not found."

    with open(file_path, "r") as infile:
        raw_input = infile.readlines()
        valid_words = [datum.strip().upper() for datum in raw_input]
    
    results = []

    # Helper function to check if a word can be made from the rack
    def can_form_word(rack, word):
        rack_copy = list(rack.upper())
        wildcards = rack_copy.count('*') + rack_copy.count('?')
        common_letters = []  # For scoring

        for letter in word:
            if letter in rack_copy:
                rack_copy.remove(letter)
                common_letters.append(letter)  # Match letter to rack
            elif wildcards > 0:
                wildcards -= 1  # Use a wildcard if available
            else:
                return False, []

        return True, common_letters

    # Find all valid words that can be made from the rack
    for word in valid_words:
        is_valid, common_letters = can_form_word(rack, word)
        if is_valid:
            # Score the word using only the common letters
            score = score_word(''.join(common_letters))
            results.append((score, word))
    
    # Sort the results by score (descending), then alphabetically by word (ascending)
    sorted_results = sorted(results, key=lambda x: (-x[0], x[1]))

    if len(sorted_results) == 0:
        return "No valid words can be formed from the given rack."

    return sorted_results, len(sorted_results)


# In[ ]:





# In[ ]:





# In[ ]:




