import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    print("\nEn dan nu line=", line, end=' ')
    try:    
        next_lang = line.strip()
#       print("next_lang=", next_lang)

        raw_bytes = next_lang.encode(encoding, errors=errors)
        cooked_string = raw_bytes.decode(encoding, errors=errors)

        print(raw_bytes, "<===>", cooked_string)
    except:
        print("mislukt")


languages = open("languages.txt", mode="r", encoding="utf-8")

main(languages, input_encoding, error)

