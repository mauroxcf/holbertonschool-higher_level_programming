#!/user/bin/python3
""" write in a file """


def write_file(filename="", text=""):
    """
    open a write a new file
    """
    with open(filename, mode='w+', encoding="utf-8") as newtext:
        return newtext.write(text)

