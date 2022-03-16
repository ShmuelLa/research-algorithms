last_val = None
last_func = None


def lastcall(func):
    """
    Checks it the same function is being called again with the same former input
    If the case is true than prints the value is being repeated.
    Else, runs the function and saves the input value
    """
    def wrapper(*args):
        global last_val, last_func
        if last_func == func:
            if last_val is None or last_val != args:
                last_val = args
            elif last_val == args:
                print(f"I already told you that the answer is {func(*args)}!")
        else:
            last_func = func
            last_val = args

    return wrapper


@lastcall
def square_num(x):
    return x**2


@lastcall
def add_two(x):
    return x+2


if __name__ == "__main__":
    """
    Test runs for checking
    """
    square_num(2)
    square_num(2)
    square_num(3)
    square_num(3)
    add_two(3)
    add_two(3)
