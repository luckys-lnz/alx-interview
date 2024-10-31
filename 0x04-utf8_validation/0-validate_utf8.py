#!/usr/bin/python3
'''a method that determines if a given data set
represents a valid UTF-8 encoding.'''


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Only keep the last 8bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine num of bytes in the UTF-8 character.
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                # If the first bit is set but it doesn't match the patterns above, it's invalid.
                return False
        else:
            # Check if the current byte is a continuation byte (10xxxxxx).
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
