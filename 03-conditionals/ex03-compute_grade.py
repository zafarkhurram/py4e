score = input("Enter score: ")

try:
    score = float(score)

    if score < 0 or score > 1.0:
        raise AttributeError
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except ValueError:
    print("Bad score")
except AttributeError:
    print("Bad score - should be between 0.0 and 1.0")