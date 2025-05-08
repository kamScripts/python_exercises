import random
import math

def generate_bday():
    """Generates birthday date
    
    Returns: string 'day-month'
    """
    month= random.randint(1,12)
    if month==2:
        day=random.randint(1,28)
    else:
        day=random.randint(1,31)
    return f'{month}-{day}'
def create_sample(n):
    """Creates a sample of generated b-days:
    
    n: number of elements
    
    Returns: list of strings"""
    t=[]
    for i in range(n):
        t.append(generate_bday())
    return t
def compare_dates(birthdays):
    """Compares dates
    
    birthdays: list of dates in format {month-day}
    
    Returns: boolean
    """
    dates=sorted(birthdays)
    for i in range(len(dates)-1):
        if dates[i]==dates[i+1]:
            return True
    return False

def check_probability(n, sample_size):
    """Checks probability of birthday paradox of n groups of b_days
    
    n: integer number of tests
    sample_size: integer number of elements in a group
    
    Returns Float"""
    
    gr_with_duplicates=0
    for _ in range(n):
        b_days=create_sample(sample_size)
        if compare_dates(b_days):
            gr_with_duplicates+=1
    return round(gr_with_duplicates/n*100, 2) 
pr=check_probability(10000, 23)
print(pr,'%')
            
