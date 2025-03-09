#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Benjamin Michael Taylor (bentaylorhk)
2025
"""

import time

MOVE_UP_ROW = "\033[F"
CLEAR_ROW = "\033[K"

def clear_lines(num: int):
    """
    Function which clears *num* previous rows of stdout
    """
    print((MOVE_UP_ROW + CLEAR_ROW) * num, end="")

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

