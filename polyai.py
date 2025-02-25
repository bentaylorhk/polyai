#!/usr/bin/env python

# Benjamin Michael Taylor (bentaylorhk)
# 2025

# Script which produces the suitable bash commands
# from its command line args, which can then be executed.

from openai import OpenAI
from pydantic import BaseModel
import subprocess
import sys


class BashCommands(BaseModel):
    commands: list[str]


system_prompt = """
Generate one or more Bash commands that best accomplish the task described by the user.  

Output Requirements:
- Output *only* the Bash command(s), with no explanations or additional text.  
- Ensure strict adherence to valid Bash syntax.  
- Format the output for human-readability.

Execution Context:
- Commands will run on *Arch Linux*, so prefer Arch-specific tools if applicable.  

Usability Considerations:
- If multiple commands are required, separate them with `&&` where appropriate.  
- Favor safe, efficient, and commonly available tools.  
"""


def main():
    user_prompt = " ".join(sys.argv[1:])

    client = OpenAI()
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        response_format=BashCommands,
    )

    commands = completion.choices[0].message.parsed.commands

    for i, cmd in enumerate(commands, start=1):
        print(f"{i}. {cmd}")

    choice = int(input("Select command: ")) - 1

    if 0 <= choice and choice < len(commands):
        print(commands[choice])
        subprocess.run(commands[choice], shell=True)


if __name__ == "__main__":
    main()
