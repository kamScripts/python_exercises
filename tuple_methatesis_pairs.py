from tuple_anagram import find_anagrams
def metathesis_words(anagrams):
    """Find metathesis pairs in list of anagram words
    Two words form m. pair if one can transform in another
    by swapping two letters
    
    example: converse and conserve
    
    anagrams: dict of anagrams
    
    Returns: dict of metathesis words
    """
    m_dict={}

    for val in anagrams.values():

        for word in val:
            for word2 in val:
                diff=0
                for char1, char2 in zip(word, word2):
                    if char1!=char2:
                        diff+=1
                if diff==2 and word2 not in m_dict:
                    m_dict[word] = m_dict.get(word, '')+ f'{word2} '

    return m_dict

a= find_anagrams('words.txt')
m = metathesis_words(a)
for key, val in m.items():
    print(key, val)
