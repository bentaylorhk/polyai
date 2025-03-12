#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Benjamin Michael Taylor (bentaylorhk)
2025
"""

import time

# Format string for the monkey animation
# 0 - eye
# 1 - mouth
# 2 - tail top (2 chars)
# 3 - tail bottom
# 4 - thoughts
# 5 - inline prompt
MONKEY_FORMAT = """
  -      {4}
c{0}{1}{0}o  .-{2}    {5}
(| |)_/   {3}
"""

TAIL_1 = "-'"
TAIL_2 = "-."
TAIL_3 = ". "

TAIL_BOTTOM_1 = TAIL_BOTTOM_2 = " "
TAIL_BOTTOM_3 = "`"

CLOSED_MOUTH = "_"
OPEN_MOUTH = "O"

CLOSED_EYE = "-"
OPEN_EYE = "'"


def clear_lines(num: int):
    """
    Function which clears *num* previous rows of stdout
    """
    # Move up row, then clear row, num times
    print("\033[F\033[K" * num, end="")


def print_monkey(
    eye: str,
    mouth: str = CLOSED_MOUTH,
    tail_top: str = TAIL_1,
    tail_bottom: str = TAIL_BOTTOM_1,
    thoughts: str = "",
    prompt: str = "",
):
    print(MONKEY_FORMAT.format(eye, mouth, tail_top, tail_bottom, thoughts, prompt))


def main():
    # Prevent clearing prompt line
    print()
    count = 0
    while True:
        count += 1

        output = ""

        output += (" " * 10) + ("? " * count) + "\n"

        output += """
          -
        c-_-o  .--'
        (| |)_/
        """

        num_lines = len(output.splitlines())
        clear_lines(num_lines)

        print(output)

        time.sleep(0.3)

        if count == 3:
            count = 0


if __name__ == "__main__":
    main()
