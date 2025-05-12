def find_anagrams(file_path):
    """
    Find all anagrams in a file and group them together
    
    Args:
        file_path: str - path to file containing words
        
    Returns:
        dict: keys are sorted tuples of characters, values are lists of anagram words
    """
    anagram_dict = {}

    try:
        with open(file_path, 'r', encoding='UTF-8') as fin:
            for line in fin:
                word = line.lower().strip()

                # Skip empty lines
                if not word:
                    continue

                # Use sorted characters as key
                key = tuple(sorted(word))

                # Add word to the appropriate anagram group
                if key in anagram_dict:
                    anagram_dict[key].append(word)
                else:
                    anagram_dict[key] = [word]

        # Filter out non-anagrams (words that have no matching anagrams)
        return {key: words for key, words in anagram_dict.items() if len(words) > 1}

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    
def print_anagrams(d):
    """Display anagram sets sorted by their length
    
    d: dict - anagrams dict
    
    Returns: None
    """
    a_list=[]
    for val in d.values():
        a_list.append((len(val), val))
    a_list.sort()
    for l, item in a_list:
        print(l, ', '.join(item))
    



if __name__ == '__main__':
    file_path = 'words.txt'
    anagram_dict = find_anagrams(file_path)
    print_anagrams(anagram_dict)
    
    