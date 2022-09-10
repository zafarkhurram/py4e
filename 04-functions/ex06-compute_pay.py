def compute_pay(hours, rate):
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    else:
        pay = hours * rate
    
    return pay


try:
    hours = input("Enter Hours: ")
    hours = int(hours)

    rate = input("Enter Rate: ")
    rate = float(rate)
    
    pay = compute_pay(hours, rate)
    print("Pay", pay)
except ValueError:
    print("Error, please enter numeric input")