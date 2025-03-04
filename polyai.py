#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script which produces a bash command described by a given prompt.
The command is produced with the OpenAI API, which can then be executed.

Benjamin Michael Taylor (bentaylorhk)
2025
"""

__version__ = "1.0.0"
__author__ = "Benjamin Taylor"

import os
from openai import OpenAI
from pydantic import BaseModel
import subprocess
import sys


class BashCommand(BaseModel):
    command: str


system_prompt = """
Generates a Bash command that best accomplish the task described by the user.

Output Requirements:
- Output *only* the Bash command, with no explanations or additional text.
- Ensure strict adherence to valid Bash syntax.
- Format the output for human-readability, opting to use readability flags where possible.

Execution Context:
- Command will run on *Arch Linux*, so prefer Arch-specific tools if applicable

Usability Considerations:
- If multiple commands are required, prioritise separating them with `&&` before newlines.
- Favor safe, efficient, modern and commonly available tools
"""


def main():
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        script_name = os.path.splitext(os.path.basename(__file__))[0]
        print(f"Usage: {script_name} <prompt>")
        exit(0)

    user_prompt = " ".join(sys.argv[1:])

    client = OpenAI()
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        response_format=BashCommand,
    )

    command = completion.choices[0].message.parsed.command

    print(command)

    choice = input("Execute command [Y/n]: ")

    if choice.lower() == "y":
        print(command)
        subprocess.run(command, shell=True)


if __name__ == "__main__":
    main()
