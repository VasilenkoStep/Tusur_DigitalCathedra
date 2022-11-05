print("Задача №2: Python art")
print(" ")

thickness = 4
c = 'M'

# Write letter
for i in range(thickness + 1):
    print((c * thickness).center(thickness + 2) + " " * i + (c * thickness) + " " * (thickness - i) * 2 + (
                c * thickness).center(thickness - 1) + " " * (i + 1) + (c * thickness).center(thickness))

# Bottom Pillars
for i in range(thickness - 3):
    print((c * (thickness - 2)).center(thickness + 2) + (c * (thickness - 2)).center(thickness * 10 - (thickness - 2)))
# BottomCones
for i in range(thickness + 1):
    print((c * (thickness - 2 * i)).center(thickness + 2) + (c * (thickness - 2 * i)).center(
        thickness * 10 - (thickness - 2)))