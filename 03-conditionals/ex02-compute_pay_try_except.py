hours = input("Enter Hours: ")

try:
    hours = int(hours)
    
    rate = input("Enter Rate: ")

    rate = float(rate)

    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    else:
        pay = hours * rate

    print("Pay", pay)
except ValueError:
    print("Error, please enter numeric input")