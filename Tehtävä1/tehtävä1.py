import numpy as np

# Tehtävä 1.1
print("Tehtävä 1.1")
A = np.array([2.493, 0.911])
for i in A:
    print(f"{np.array(i)} = {np.degrees(i):.2f}°")

# Tehtävä 1.2
print("\nTehtävä 1.2")
B = np.array([137.7, 62.3])
for i in B:
    print(f"{np.array(i)}° = {np.radians(i):.2f} rad")
# Tehtävä 1.3
print("\nTehtävä 1.3")
C = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
k = 0
for i in C:
    print(f"{np.array(i)}° = {np.radians(i):.2f} rad | ", end="")
    k += 1
    if k == 3:
        print()
        k = 0
