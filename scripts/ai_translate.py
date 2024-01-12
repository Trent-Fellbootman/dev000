#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path

from openai import OpenAI

client = OpenAI()

def stream_translation(file_path: Path, language_code: str, silent: bool = True) -> str:
    # Read the markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Preparing the prompt for translation
    prompt = f"""I have a markdown file:

<markdown>
{content}
</markdown>

Please translate this markdown to {language_code} (that's an ISO language code).
Notice that the label text contained in `mermaid` blocks also needs to be translated
(but don't translate labels like A, B, C).
Output the translated markdown ONLY and NOTHING ELSE.
DO NOT INCLUDE <markdown> and </markdown>.

Notice that, if there are special "developer" terms
(like "abstractions", or "compiler", sometimes but not always in bold face),
you should not only translate but also provide the original English properly,
e.g., "compiler" --> "编译器（compiler）".

Note, "ja" is not the code for Chinese!
"""

    # Stream parameter set to True for incremental output
    stream = client.chat.completions.create(
      model="gpt-3.5-turbo-16k",
      messages=[
          {"role": "system", "content": "You are a multilingual expert developer."},
          {"role": "user", "content": prompt}
        ],
      stream=True
    )
    
    translated_text = ''

    # Iterating over the stream and printing each part of the response
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            text = chunk.choices[0].delta.content
            if not silent:
                print(text, end='', flush=True)
            translated_text += text

    return translated_text

parser = argparse.ArgumentParser()
parser.add_argument('language_code', type=str, help='Code of the language to translate to')
parser.add_argument('input_path', type=Path, help='Path to the input markdown file')
parser.add_argument('output_path', type=Path, help='Path to save the translated markdown file')

if __name__ == '__main__':
    args = parser.parse_args()
    language, input_path, output_path = args.language_code, args.input_path, args.output_path
    
    translated_text = stream_translation(input_path, language, silent=False)
    
    output_path.touch()
    
    with open(output_path, 'w') as f:
        f.write(translated_text)
