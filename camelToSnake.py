import os

def is_camel_case(word):
    return word != word.lower() and word != word.upper() and "_" not in word

def to_snake_case(word):
    fragments = [word[0].lower()]
    for c in word[1:]:
        if c.isupper():
            fragments.append("_")
            fragments.append(c.lower())
        else:
            fragments.append(c)
    return "".join(fragments)

def iterateFiles():
    directory = input("Type the root directory: ")

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r+") as f_in:
                for line in f_in:
                    words = line.split()
                    for i, word in enumerate(words):
                        if is_camel_case(word):
                            words[i] = to_snake_case(word)
                        f_in.write(words + "\n")

    print("Files changed")


iterateFiles()
