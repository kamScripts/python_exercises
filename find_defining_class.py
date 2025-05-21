def find_def_class(obj, meth_name):
    """Returns the class that provides the definition of the method."""
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty