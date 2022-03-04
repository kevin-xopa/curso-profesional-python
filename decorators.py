from datetime import datetime


def execution_time(func):
    # function wrapper, no matter what positional arguments are sent,
    # or named arguments, the function receives them
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        # execute the function as parameter, no matter what positional
        # arguments are sent, or named arguments, the function receives them
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {str(time_elapsed.total_seconds())} segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


random_func()
suma(5, 7)

