def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "w") as file:
        new_content = file.read().replace(old_word, new_word)
        file.write(new_content)
        file.truncate()


def find_and_replace2(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()
