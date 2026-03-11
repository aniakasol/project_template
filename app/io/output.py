def output_to_console(text):
    """
    Print text to the console.

    Parameters
        text : str (Text to display)
    """
    print(text)

def write_to_file(filename, text):
    """
    Write text to a file using Python built-in functions.

    Parameters
    ----------
    filename : str (Path to the output file)
    text : str (Text to write)
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")
