"""This program allows the user to display one Julia set at a time.
It is recommended to have at least an 80 column display.
"""
# import math
import imag

# (x-range), (y-range), (resolution=(4, 4)), (divergent (depth), convergent, (0,0)) ("□", "■", "▣")
PARAMETERS = ((-2, 0.5), (-1.12, 1.12), (4, 4), (" ", "*", "@"))  # Mandelbrot
# PARAMETERS = ((-2, 2), (-2, 2), (4, 4), ((" ", ",", ".", "'", ":"), "*", "@"))  # Julia sets


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
    z = (z * z) + c
    return z


def main():
    """This function implements the above in order to actually graph onto a CLI."""
    print()

    # Generate line-wrap length
    line_wrap = len(
        [
            ""
            for _ in range(
                int(PARAMETERS[0][0] * 100),
                int(PARAMETERS[0][1] * 100),
                PARAMETERS[2][1],
            )
        ]
    )

    # Generate points
    points = []
    for b in range(
        int(PARAMETERS[1][1] * 100), int(PARAMETERS[1][0] * 100), -PARAMETERS[2][0]
    ):
        for a in range(
            int(PARAMETERS[0][0] * 100), int(PARAMETERS[0][1] * 100), PARAMETERS[2][1]
        ):
            points.append(imag.imag(a / 100, b / 100))

    count = 0
    print(" ", "_" * line_wrap, sep="", end="\n|")
    for point in points:
        count += 1

        # Print (0, 0)
        if point.a == 0 and point.b == 0:
            print(PARAMETERS[3][2], end="")
            continue

        # Run algorithm
        z = imag.imag(0, 0)
        for run in range(100):
            z = algorithm(z, point)
            if z.a > 2 or z.a < -2 or z.b > 2 or z.b < -2:
                if not isinstance(PARAMETERS[3][0], tuple):
                    print(PARAMETERS[3][0], end="")
                    break
                else:

                    num_sep = 100 // len(PARAMETERS[3][0])
                    for index, char in enumerate(PARAMETERS[3][0]):
                        if run < int(num_sep) * (int(index) + 1):
                            print(char, end="")
                            break
                    break

        else:
            print(PARAMETERS[3][1], end="")

        # Line wrap
        if count % line_wrap == 0:
            print("|\n", end="")

        if count % line_wrap == 0:
            if point != points[-1]:
                print("|", sep="", end="")

    print(" ", "‾" * line_wrap, sep="")


if __name__ == "__main__":
    main()
