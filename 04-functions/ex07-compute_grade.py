def compute_grade(score):
    if score < 0 or score > 1.0:
        raise AttributeError
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"


try:
    score = input("Enter score: ")
    score = float(score)

    print(compute_grade(score))
except ValueError:
    print("Bad score")
except AttributeError:
    print("Bad score - should be between 0.0 and 1.0")