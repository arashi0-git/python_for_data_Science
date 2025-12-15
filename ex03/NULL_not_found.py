from NULL_not_found import NULL_not_found

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: None {type(object)}")
    elif object is NaN:
        print(f"Cheese: nan {type(object)}")
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")



Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
