
def check_fermat(a, b, c, n):
    """Check if Fermat's Last Theorem holds
    there are no positive integers a,b and c such that
    a**n + b**n = c**n for any values of n > 2 """

    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!"')
    else:
        print('No, that doesn\'t work.')

def is_triangle(a, b, c):
    """Test if it possible to build a triangle from given legths a, b, c"""
    if a+b>=c and b+c>=a and c+a>=b:
        print('Yes')
    else:
        print('No')

descriptions = {
    'fermat': """
there are no positive integers a, b and c such that
a**n + b**n = c**n for any value > 2 """,
    'is_triangle': """
If any of the three lengths is greater than the sum of the other two,
then they cannot form a triangle.
""",
    
    }
def input_prompt(type, parameter):
    return f'Enter {type.__name__} for {parameter} or r to return: '

functions = {
    1: {
        'name': "Check if Fermat's Last Theorem holds",
        'description': descriptions['fermat'],
        'function':lambda a, b, c, n: check_fermat(a, b, c, n),
        "args": [('a', int), ('b', int), ('c', int), ('n', int)]
    },
    2: {
        'name': 'Check if you can form a triangle',
        'description': descriptions['is_triangle'],
        'function': lambda a, b, c: is_triangle(a, b, c),
        'args': [('a', int), ('b', int), ('c', int)]
    }
}

def get_usr_input(para, data_type):
    while True:
        try:
            user_input= input(input_prompt(data_type, para))
            if user_input.lower() == 'r':
                return user_input.lower()
            return data_type(user_input)
        except ValueError:
            print('invalid input please type only integer values')
def execute_func(func):
    func_info = func
    args = []
    print(func_info['name'], '\n', func_info['description'])
    for p in func_info['args']:
        arg = get_usr_input(p[0], p[1])
        if arg == 'r':
            return
        args.append(arg)
    try:
        func_info['function'](*args)
    except TypeError as e:
        print(e)


def menu():
    is_running = True
    while is_running:
        for index, func in functions.items():
            print(f"{index}. {func['name']}")
        user_input = input('Type function number or q to quit ')
        if user_input == 'q':
            print('Goodbye!')
            is_running = False
        try:
            index = int(user_input)
            execute_func(functions[index])
        except ValueError:
            print('Please type only valid numbers or q to exit')
        except KeyError:
            print('Please type only valid numbers or q to exit')
menu()