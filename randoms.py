import random
from dict_histogram import histogram
ch=['a','a','b']
hist=histogram(ch)
print(hist)
r=random.choice(ch)
print(r, f'probability of {r} is {hist.get(r)}/{sum(hist.values())}')

