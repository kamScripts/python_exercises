import os

cwd= os.getcwd()
def walk(dirname):
    """Prints the names of all files in dirname and its subdirectories.

    This is the version in the book.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
def w(directory):
    """Prints the names of all files in dirname and its subdirectories.
       Using os.walk()
        
    directory: str name of directory
    """
    for d in os.walk(directory):
#os.walk() return tuples ()
        if len(d[2])>=1:
            for file in d[2]:
                path=os.path.join(d[0], file)
                print(path)

w(cwd)
