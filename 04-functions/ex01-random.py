import random

for i in range(10):
    x = random.random()
    print("random.random(): %d", x)

for i in range(10):
    x = random.randint(1, 100)
    print("random.randint(1, 100): %d", x)

for i in range(10):
    x = random.choice([1,2,3,4,5,6,7,8,9,10])
    print("random.choice([1,2,3,4,5,6,7,8,9,10]): %d", x)