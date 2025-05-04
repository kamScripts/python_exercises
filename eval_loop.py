def eval_loop():
    while True:
        user_input=input("type expression to evaluate or type 'done' to end program\n>")
        if user_input == 'done':
            break
        print(eval(user_input))
eval_loop()