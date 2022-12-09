"""Math exercises."""


'''def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum_ = num_a + num_b
    difference = num_a - num_b
    return sum_, difference'''


'''def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division'''


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a // num_b
    return division

# print(integer_division(9,3))


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = pow(num_a, num_b)
    remainder = num_a % num_b
    
    return multiply_numbers, power, remainder

# print(powerful_operations(3,2))


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    sum = num_a + num_b
    average = sum / 2
    return average

# print(find_average(3,4))


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    from math import pi
    circle_area = radius * pi,
    return circle_area

# print(area_of_a_circle(3))


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    import math
    ruutjuur_3 = math.sqrt(3)
    triangle_area = (ruutjuur_3 * side_length * side_length) / 4
    return round(triangle_area)

print(area_of_an_equilateral_triangle(3))


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    # Write your code here
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    # Write your code here
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    # Write your code here
    return b
