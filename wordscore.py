#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
This module provides the function to score Scrabble words based on the Scrabble letter values.
"""

# Dictionary of letter scores
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

def score_word(word):
    """
    Given a word, returns the Scrabble score for that word.
    
    Wildcard characters ('*' or '?') are worth 0 points.
    
    Parameters:
    word (str): The word to score.
    
    Returns:
    int: The score of the word.
    """
    total_score = 0
    for letter in word.lower():
        if letter in scores:
            total_score += scores[letter]
        elif letter == '*' or letter == '?':
            continue  # Wildcards contribute 0 points
    return total_score


# In[ ]:





# In[ ]:





# In[ ]:




