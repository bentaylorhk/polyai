#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
monkey

Benjamin Michael Taylor (bentaylorhk)
2025
"""

import random
import time
import os
import sys


# Format string for the monkey animation
# 0 - eye
# 1 - mouth
# 2 - tail top (2 chars)
# 3 - tail bottom
# 4 - thoughts
# 5 - inline prompt
MONKEY_FORMAT = """      {4}
   -
 c{0}{1}{0}o  .-{2}    {5}
 (| |)_/   {3}
"""

TAIL_1 = "-'"
TAIL_2 = "-."
TAIL_3 = ". "

TAIL_BOTTOM_1 = " "
TAIL_BOTTOM_2 = "`"

CLOSED_MOUTH = "_"
OPEN_MOUTH = "O"

CLOSED_EYE = "-"
OPEN_EYE = "'"

# Sequences of characters for the monkey animation
TAIL_ANIMATION = [TAIL_1, TAIL_2, TAIL_3, TAIL_2]
TAIL_BOTTOM_ANIMATION = [TAIL_BOTTOM_1, TAIL_BOTTOM_1, TAIL_BOTTOM_2, TAIL_BOTTOM_1]

SAVE_CURSOR = "\033[s"
RESTORE_CURSOR = "\033[u"
CLEAR_UNDER_CURSOR = "\033[J"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"
MOVE_UP_ROW = "\033[F"
CLEAR_ROW = "\033[K"


def clear_lines(num: int):
    """
    Function which clears *num* previous rows of stdout
    """
    sys.stdout.write((MOVE_UP_ROW + CLEAR_ROW) * num)


def loop():
    # Prevent clearing prompt line
    # print()

    sys.stdout.write(SAVE_CURSOR)

    eye = OPEN_EYE
    mouth = CLOSED_MOUTH

    tail_state = 0
    thoughts_state = 0
    blinking_state = False

    while True:
        output = ""

        if not blinking_state and random.random() < 0.1:
            blinking_state = True
            eye = CLOSED_EYE
        else:
            blinking_state = False
            eye = OPEN_EYE

        thoughts = "? " * thoughts_state
        thoughts_state += 1
        if thoughts_state > 3:
            thoughts_state = 1

        prompt = ""

        output += MONKEY_FORMAT.format(
            eye,
            mouth,
            TAIL_ANIMATION[tail_state],
            TAIL_BOTTOM_ANIMATION[tail_state],
            thoughts,
            prompt,
        )

        tail_state += 1
        if tail_state == len(TAIL_ANIMATION):
            tail_state = 0

        # num_lines = len(output.splitlines())
        # clear_lines(num_lines)

        sys.stdout.write(output)
        sys.stdout.flush()

        time.sleep(0.2)

        # Reset animation below bash prompt
        sys.stdout.write(RESTORE_CURSOR)
        sys.stdout.write(SAVE_CURSOR)
        sys.stdout.write(CLEAR_UNDER_CURSOR)
        # TODO: Move back to clear lines, relative movements are better.


def main():
    """
    Main function
    """
    try:
        # Disable terminal auto-wrap
        os.system("tput rmam")

        sys.stdout.write(HIDE_CURSOR)

        # TODO: buffer a few lines first.

        loop()

    finally:
        # Restore terminal condition, can be left messed up
        # by a 'KeyboardInterrupt'

        sys.stdout.write(SHOW_CURSOR + "\n")
        sys.stdout.flush()

        # Enable termial wrap
        os.system("tput smam")


if __name__ == "__main__":
    main()
