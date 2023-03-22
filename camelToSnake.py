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


def write_file(file, content):
    with open(file, "w") as f_out:
        f_out.write(content)


def build_line(words):
    return ' '.join(words) + '\n'


def iterate_files():
    directory = input("Type the root directory: ")
    extension = input("Type the file extension (e.g. '.txt'): ")
    backup_files = input("Create backup files? (y/n): ").lower() == "y"

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r") as f_in:
                        replaced_content = ""
                        for line in f_in:
                            words = line.split()
                            if line == "\n":
                                replaced_content += "\n"
                            else:
                                for i, word in enumerate(words):
                                    if is_camel_case(word):
                                        words[i] = to_snake_case(word)
                                new_line = build_line(words)
                                replaced_content += new_line

                        if backup_files:
                            backup_path = file_path + ".bak"
                            write_file(backup_path, f_in.read())

                        write_file(file_path, replaced_content)

                    print(f"{file_path} processed successfully.")
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
                    continue

    print("Files changed")


iterate_files()
