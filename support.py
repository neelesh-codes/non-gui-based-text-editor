
def read_the_file(filename):
    """
    This method reads the content of a file.

    :param filename: The name of the file to read.
    :return: The content of the file as a string.
    """
    with open(filename, 'r') as f:
        text = f.read()
        print(text)
    return text


def write_in_file(filename, what_to_write):
    """
    This method writes a string to a file.

    :param filename: The name of the file to write to.
    :param what_to_write: The string to write.
    :return: None.
    """
    with open(filename, 'w') as f:
        f.write(what_to_write)
    return None


def append_in_file(filename, what_to_append):
    """
    This method appends a string to a file.

    :param filename: The name of the file to append to.
    :param what_to_append: The string to append.
    :return: None.
    """
    with open(filename, 'a') as f:
        f.write(what_to_append)
    return None


if __name__ == "__main__":
    # Checking The fclass TextEditor here
    read_the_file("main.py")
    write_in_file("main.py", "print('hello world')")
    append_in_file("main.py", "\nimport support as spp")

