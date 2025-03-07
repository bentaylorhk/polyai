<p align="center">
<pre>
                     ,,                      ,,  
                   `7MM                      db  
                     MM                          
`7MMpdMAo.  ,pW"Wq.  MM `7M'   `MF',6"Yb.  `7MM  
  MM   `Wb 6W'   `Wb MM   VA   ,V 8)   MM    MM  
  MM    M8 8M     M8 MM    VA ,V   ,pm9MM    MM  
  MM   ,AP YA.   ,A9 MM     VVV   8M   MM    MM  
  MMbmmd'   `Ybmd9'.JMML.   ,V    `Moo9^Yo..JMML.
  MM                       ,V                    
.JMML.                  OOb" 
</pre>
</p>


Simple bash helper script which uses OpenAI's API to produce a bash
command from a user prompt. This command can then be executed, or an
alternative can be requested.

## Installation

To install `polyai`, run:

```bash
pip install git+https://github.com/bentaylorhk/polyai.git
```

## OpenAI API Key

After installation, you can run the script with...

```bash
polyai [--help] <prompt>
```

For this script to work, ensure you have your OpenAI API Key
stored in environment variable `$OPENAI_API_KEY`.

Alternatively, you could prepend the command with the variable like so...

```bash
OPENAI_API_KEY=<api_key> polyai <prompt>
```
