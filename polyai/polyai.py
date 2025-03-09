#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script which produces a bash command described by a given prompt.
The command is produced with the OpenAI API, which can then be executed.

Benjamin Michael Taylor (bentaylorhk)
2025
"""

import os
import subprocess
import sys

from openai import OpenAI
from pydantic import BaseModel


class BashCommand(BaseModel):
    """
    Simple format for the models response. Getting
    a response with this model much more reliably
    gets responses without markup formatting in it
    even if stated so in the system prompt >:(
    """

    command: str


SYSTEM_PROMPT = """
Generate a Bash command that best accomplish the task described by the user prompt.

Output Requirements:
- Output only plain text. Do not output markdown.
- Output *only* the Bash command, with no explanations or additional text.
- Ensure strict adherence to valid Bash syntax.

Execution Context:
- Command will run on *Arch Linux*, so prefer Arch-specific tools if applicable

Usability Considerations:
- If multiple commands are required, prioritise separating them with `&&` before newlines.
- Format the output for human-readability, opting to use readability flags where possible.
- Favor safe, efficient, modern and commonly available tools
"""

client = OpenAI()


def get_command(user_prompt: str) -> str:
    """
    Gets a bash command from a given prompt using OpenAI's ChatGPT.

    Args:
        user_prompt: Prompt describing bash command.

    Returns:
        Bash command outputted by the AI model.
    """

    response = client.beta.chat.completions.parse(
        model="gpt-4o",
        store=True,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        response_format=BashCommand,
    )

    return response.choices[0].message.parsed.command


def main():
    """
    Take args as prompt, and loop to offer alternative prompts.
    """
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        script_name = os.path.splitext(os.path.basename(__file__))[0]
        print(f"Usage: {script_name} <prompt>")
        return 0

    user_prompt = " ".join(sys.argv[1:])

    command = get_command(user_prompt)

    # Retaining all commands for model memory
    commands = [command]

    # Continue looping if asking for alternatives
    while True:
        print(command)

        choice = input("Execute command [(y)ay/(a)lt/(n)ae]: ")

        if choice.lower() == "y":
            print(command)

            # Run command, propagate error if it fails
            subprocess.run(command, shell=True, check=True)

        # Only continue looping if alrternative is requested
        if choice.lower() != "a":
            break

        command = get_command(f"""
        Could you provide an alternative command to the ones you previously outputted,
        still trying to achieve the user's initial prompt?
        User's initial prompt: {user_prompt}
        Previous responses: {commands}
        """)
        commands.append(command)

    return 0


if __name__ == "__main__":
    main()
