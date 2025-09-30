def get_num_words(text):
    words = text.split()
    length = len(words)
    return f"Found {length} total words"

def count_words(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_characters_by_count(char_counts):
    """
    Sorts the character counts dictionary into a list of dictionaries, ordered by frequency.

    Args:
        char_counts (dict): Dictionary of characters and their frequencies.

    Returns:
        list: A sorted list of dictionaries. Each dictionary contains:
              - "char": The character.
              - "num": The frequency of the character.
    """
    # Create a list of dictionaries, filtering out non-alphabetical characters
    char_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]

    # Sort the list by "num" (frequency) in descending order
    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list