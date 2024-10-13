#!/usr/bin/python3
"""
This module contains a function that determines if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list where each index represents a box,
                                     and the list at each index contains the
                                     keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """

    # if boxes is empty.
    if not boxes or len(boxes) == 1:
        return True
    
    # track unlocked boxes
    unlocked = set()
    # Start with the first box (index 0)
    unlocked.add(0)
    
    # Use list to keep track of the keys we have
    keys = list(boxes[0])
    

    while keys:
        key = keys.pop()
        
        # If the key is a valid box number and it hasn't been unlocked yet
        if key not in unlocked and 0 <= key < len(boxes):
            unlocked.add(key)
            
            # Add the keys from newly unlocked box to our list of keys
            keys.extend(boxes[key])
    
    # Check wether all boxes are unlocked
    return len(unlocked) == len(boxes)
