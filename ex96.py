def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        content = file.read()
    with open(new_file_name, "w") as new_file:
        new_file.write(content[::-1])


copy_and_reverse("story.txt", "new_story.txt")
