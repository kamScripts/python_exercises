def count(letter, string)->int:
    """Count how many times a character occurs in a string."""
    count=0
    for i in string:
        if i==letter:
            count+=1
    return count
sentence = 'czarna krowa w kropki bordo zuje trawe i mieli morda'
print(count('w', sentence))
print(sentence.count('w'))