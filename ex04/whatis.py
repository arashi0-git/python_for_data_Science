import sys

if len(sys.argv) == 2:
    try:
        num = int(sys.argv[1])
        s = 'odd' if num % 2 else 'even'
        print(s)
    except ValueError:
        print("AssertionError: argument is not an integer")
else:
    print("AssertionError: more than one argument is provided")
