from termcolor import colored


def is_fibonacci(num):
    
    """Check if a number is in the Fibonacci sequence."""

    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num


def display_result(num, in_sequence):

    """Display the result with colored output."""

    if in_sequence:
        print(colored(f"{num} is in the Fibonacci sequence!", "green"))
    else:
        print(colored(f"{num} is not in the Fibonacci sequence.", "red"))


def check_if_num_perfect_square(num):

    """Check if the number is a perfect square."""

    is_perfect_square = num ** 0.5 == int(num ** 0.5)
    if is_perfect_square:
        print(colored(f"{num} is a perfect square!", "blue"))
    else:
        print(colored(f"{num} is not a perfect square.", "yellow"))


if __name__ == "__main__":
    try:
        user_num = int(input(colored("Enter a number: ", "yellow")))
        result = is_fibonacci(user_num)
        display_result(user_num, result)

        # Extra feature
        check_if_num_perfect_square(user_num)

    except ValueError:
        print(colored("Invalid input. Please enter a valid number.", "red"))
