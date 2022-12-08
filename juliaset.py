"""This program allows the user to display one Julia set at a time.
It is recommended to have at least an 80 column display.
"""
# import math
import imag

# (x-range), (y-range), (res=(80, 40)), (divergent (depth), convergent, (0,0)) ("□", "■", "▣")
PARAMETERS = ((-2, 0.5), (-1.12, 1.12), (80, 40), (" ", "*", "@"), 1000)
# PARAMETERS = ((-2, 2),(-2, 2), (80, 40), ((" ", ",", ".", "'", ":"), "*", "@"), 10000,)


def algorithm(z: imag.imag, c: imag.imag) -> imag.imag:
    """This function represents the actual function being graphed as a Julia set

    Parameters:
        z: imag.imag = The complex number used to check stability
        c: imag.imag = The point being checked for stability

    Returns:
        imag.imag -> A new point to use for checking stability
    """
    if z.a == 0 and z.b == 0:
        return c
    z = (z * z) + imag.imag(c.a, c.b)
    return z


def test_point(point: imag.imag) -> int:
    """This function returns the number of iterations it takes for the point to diverge

    Parameters:
        point: imag.imag = The point to check

    Returns:
        int -> The number of iterations needed to diverge, or the maximum interation
    """
    if len(PARAMETERS[3]) == 3 and point.a == 0 and point.b == 0:
        return -1
    z = imag.imag(0, 0)
    for run in range(PARAMETERS[4]):
        z = algorithm(z, point)
        if z.a < -2 or z.a > 2 or z.b < -2 or z.b > 2:
            return run
    return PARAMETERS[4]


def point_char_to_draw(runs: int) -> str:
    """This function returns the correct depth character to print for a particular point

    Parameters:
        runs: int = The number of iterations needed for the point to diverge

    Returns:
        str -> The string to print for this particular point
    """
    if runs == -1:
        return PARAMETERS[3][2]

    if runs == PARAMETERS[4]:
        return PARAMETERS[3][1]

    count = 0
    while (PARAMETERS[4] / len(PARAMETERS[3][0])) * (count + 1) < runs:
        count += 1
    return PARAMETERS[3][0][count]


def main():
    """This function implements the above in order to actually graph onto a CLI."""
    print()

    print(" ", "_" * PARAMETERS[2][0], sep="", end="\n")
    for y in range(PARAMETERS[2][1]):
        print("|", end="")
        for x in range(PARAMETERS[2][0]):
            print(
                point_char_to_draw(
                    test_point(
                        imag.imag(
                            PARAMETERS[0][0]
                            + x
                            * (
                                (PARAMETERS[0][1] - PARAMETERS[0][0]) / PARAMETERS[2][0]
                            ),
                            PARAMETERS[1][1]
                            - y
                            * (
                                (PARAMETERS[1][1] - PARAMETERS[1][0]) / PARAMETERS[2][1]
                            ),
                        )
                    )
                ),
                end="",
            )

        if y != PARAMETERS[2][1] - 1:
            print("|")
        else:
            print("|\n ", "‾" * PARAMETERS[2][0], sep="", end="")
    print(" ")


if __name__ == "__main__":
    main()
