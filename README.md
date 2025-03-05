# polyai

Simple bash helper script which uses OpenAI's API to produce a bash
command from a user prompt. This command can then be executed, or an
alternative can be requested.

## Installation

To install `polyai`, run:

```bash
pip install git+https://github.com/bentaylorhk/polyai.git
```

## OpenAI API Key

For this script to work, ensure you have your OpenAI API Key
stored in environment variable `$OPENAI_API_KEY`.

Alternatively, you could prepend the command with the variable like so...

```bash
OPENAI_API_KEY=<api_key> polyai <prompt>
```
