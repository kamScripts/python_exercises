def dict_by_lengths(file):
    """Reads a word list and returns dictionaries of words organized by length."""
    # Dictionary to hold all valid words
    all_words = {}
    # Dictionary to hold words grouped by length
    words_by_length = {}
    
    with open(file) as fin:
        for line in fin:
            word = line.strip().lower()
            all_words[word] = None
            
            # Group words by length
            length = len(word)
            if length not in words_by_length:
                words_by_length[length] = []
            words_by_length[length].append(word)
    
    # Add single letter words to the word list
    for letter in ['a', 'i']:
        all_words[letter] = None
        if 1 not in words_by_length:
            words_by_length[1] = []
        if letter not in words_by_length[1]:
            words_by_length[1].append(letter)
    
    return all_words, words_by_length
def is_reducible(word, all_words, memo=None):
    """Check if a word is reducible to 'a' or 'i'.
    
    Args:
        word: string to check
        all_words: dictionary of valid words
        memo: memoization dictionary to avoid recomputing
        
    Returns:
        list of words in reduction sequence if reducible, otherwise None
    """
    if memo is None:
        memo = {}
    
    # If we've already computed this word, return the result
    if word in memo:
        return memo[word]
    
    # Base case: if word is 'a' or 'i', it's reducible
    if word in ['a', 'i']:
        memo[word] = [word]
        return [word]
    
    # If word isn't in dictionary, it's not reducible
    if word not in all_words:
        memo[word] = None
        return None
    
    # Try removing each letter
    for i in range(len(word)):
        # Remove the i-th letter
        reduced_word = word[:i] + word[i+1:]
        
        # Check if reduced_word is reducible
        reduction = is_reducible(reduced_word, all_words, memo)
        
        if reduction:
            # If reducible, this word is also reducible
            memo[word] = [word] + reduction
            return memo[word]
    
    # If no reduction worked, this word is not reducible
    memo[word] = None
    return None

def find_longest_reducible_word(file='words.txt'):
    """Find the longest English word that is reducible."""
    all_words, words_by_length = dict_by_lengths(file)
    memo = {}
    
    # Add base cases to memo
    memo['a'] = ['a']
    memo['i'] = ['i']
    memo[''] = ['']
    
    longest_word = ""
    longest_reduction = []
    
    # Start from the longest words and work down
    max_length = max(words_by_length.keys())
    
    for length in range(max_length, 0, -1):
        if length in words_by_length:
            for word in words_by_length[length]:
                reduction = is_reducible(word, all_words, memo)
                if reduction and len(word) > len(longest_word):
                    longest_word = word
                    longest_reduction = reduction

            # If we've found a reducible word, we can stop checking shorter lengths
            if longest_word and length == len(longest_word):
                break

    return longest_word, longest_reduction


if __name__ == "__main__":
    word, reduction = find_longest_reducible_word()
    print(f"Longest reducible word: {word} ({len(word)} letters)")
    print("Reduction sequence:")
    for i, w in enumerate(reduction):
        print(f"{i+1}. {w}")