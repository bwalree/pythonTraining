"""
This is an exercise to get familiar with Pylint.

You can install pylint with:
pip install pylint

To use pylint, run the following in the terminal/commandline:
pylint pylint_exercise.py
"""


def main():
    """Main function."""
    name = input("What is your name? ")
    greet(name)


def greet(name):
    """Greet the person."""
    print(f"Hello %s, how are you?" % name)


def make_percentage(number):
    """"Turn a number into a percentage."""
    percentage = number / 100
    return f"{percentage}%"


if __name__ == "__main__":
    main()
