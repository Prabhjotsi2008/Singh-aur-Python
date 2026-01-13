# FUNCTION RETURNING MULTIPLE VALUES
import math

def circle_stats(radius):
    area = math.pi*(radius**2)
    circum = 2 * math.pi * radius
    return area,circum # a tuple is returned
    print("hi") # will never run # nothing after return is executed


# using tuple indexing
result = circle_stats(3)
print(type(result)) # tuple

# used round(value,precision)
print(f"Area : {round(result[0],2)}, Circumference : {round(result[1],2)}")


# using tuple-unwrapping
area,circum = circle_stats(5)
print(f"Area : {round(area,2)}, Circumference : {round(circum,2)}")