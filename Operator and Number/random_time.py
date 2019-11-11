import random

random = random.randint(100000, 1000000)

hours = random // 360
minutes = (random % 360) // 60
seconds = (random % 360) % 60

print("Time", random, "seconds equal", hours, "Hours", minutes,"Minutes",seconds,"Seconds")
