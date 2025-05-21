def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))