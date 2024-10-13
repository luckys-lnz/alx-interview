#!/usr/bin/python3

def canUnlockAll(boxes):

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
