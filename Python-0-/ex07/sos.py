import sys

def main():
    """Morse code use dict and print"""
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    text = ""
    try:
        if len(sys.argv) != 2:
            raise AssertionError
        
        for c in sys.argv[1]:
            if not c.isalpha() and not c.isdigit() and c != " ":
                raise AssertionError
            if c.isalpha() and c.islower():
                c = c.upper()
            text += NESTED_MORSE[c]
        text = text.strip()
        print(text)

    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()