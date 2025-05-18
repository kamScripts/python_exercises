import os

cwd= os.getcwd()
def w(directory):
    """Traverse through directory with os.walk"""
    for d in os.walk(directory):

        if len(d[2])>=1:
            for file in d[2]:
                path=os.path.join(d[0], file)
                print(path)

w(cwd)

