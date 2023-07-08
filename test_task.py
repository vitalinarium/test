import re


def get_unique_char(raw_text):
    text = re.split('[-"+():\n/ .]+', raw_text)
    result = ''
    chars = []
    for word in text:
        for char in word:
            number = word.count(char)
            if number == 1:
                chars.append(char)
                break
            else:
                continue

    for symbol in chars:
        num = chars.count(symbol)
        if num == 1:
            result = symbol
            break
        else:
            continue

    return result


output = get_unique_char('''The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"''')
print(f'Your unique symbol is: {output}')
