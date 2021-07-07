# Implement a method that accepts 3 integer values a, b, c. 
# The method should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    """Checks if a triangle can be built from 3 given values.

    Args:
        a ( ): assumed side
        b ( ): assumed side
        c ( ): assumed side

    Returns:
        either False or True: returns based on whether triangle can be made or not from the given values.
    """
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

first_test_line = is_triangle(2,2,2)
print(first_test_line)

second_test_line = is_triangle(-1,2,3)
print(second_test_line)