import sys
import string


def count_arguments(text: str):
    """count characters and Upper, Lower, punctuation marks and digits"""
    print(f"The text contains {len(text)} characters:")
    upper = 0
    lower = 0
    digit = 0
    punc = 0
    space = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digit += 1
        elif c in string.punctuation:
            punc += 1
        elif c == " " or c == "\n":
            space += 1

    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """get arguments and give func"""
    if len(sys.argv) == 2:
        count_arguments(sys.argv[1])
    elif len(sys.argv) == 1:
        print("What is the text to count?")
        text = sys.stdin.read()
        count_arguments(text)
    else:
        print("AssertionError: number of arguments allow only 1 or 2")


if __name__ == "__main__":
    main()
