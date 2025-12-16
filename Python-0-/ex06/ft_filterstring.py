import sys
from ft_filter import ft_filter

def main():
    """Filter words from a string by length"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError

        text = sys.argv[1]
        n = int(sys.argv[2])

        words = text.split()

        filtered = ft_filter(lambda w: len(w) > n, words)
        result = [w for w in filtered]

        print(result)

    except Exception:
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()
