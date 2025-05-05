def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
print(first('racecar'), middle('r'), last('rececar'))

def is_pallindrome(word):
    word_no_spaces = ''.join(word.split(' '))
    if len(word) <= 1:
        return True
    if first(word_no_spaces) != last(word_no_spaces):
        return False
    return is_pallindrome(middle(word_no_spaces))
    
print(is_pallindrome('racecar'))

def is_pallindrome_slice(string):
    s_no_spaces = string.replace(' ', '').lower()
    return s_no_spaces == s_no_spaces[::-1]
def is_pallindrome_while_loop(string):
    string = string.replace(' ', '').lower()
    i=0
    j=len(string)-1
    while j > 0:
        if string[i] != string[j]:
            return False
        i+=1
        j-=1
    return True
print(is_pallindrome_slice('race Car'))