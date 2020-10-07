#!/user/bin/python3
def write_file(filename="", text=""):
    """
    open a write a new file
    """
    with open(filename, mode='w+', encoding="utf-8") as newtext:
        return newtext.write(text)

