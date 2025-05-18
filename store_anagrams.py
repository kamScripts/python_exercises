import anagram_sets as ans
import shelve

t=ans.all_anagrams('words.txt')

def store_obj(obj, fil):
    with shelve.open(fil, 'c') as db:
        for key, val in obj.items():
            db[key]= val
        print('recorded')
def read_anagrams(anagram, file):
    with shelve.open(file) as shelf:
        letters= ''.join(sorted(anagram))
        try:
            return shelf[letters]
        except KeyError:
            return []
#store_obj(t, 'anagrams2')

print(read_anagrams('alerts', 'anagrams'))