# Student ID : 1201201025
# Student Name : Tai Jun Ping

import math

radius = int(input("Enter the radius : "))

v = 1.33333333333 * (math.pi) * pow(radius,3)
sa = 4 * (math.pi) * pow(radius,2)

print("The sphere of radius ",radius," is the volume of {:.2f} and the surface area of {:.2f}".format(v,sa))