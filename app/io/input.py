import pandas

def input_from_console():
    """
    Read text from the console input.

    Returns
        str (Text entered by the user)
    """
    return input("Enter text: ")

def read_file(filename):
    """
    Read text from a file using Python built-in functions.

    Parameters
        filename : str (Path to the file.)

    Returns
        str (Contents of the file)
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def read_file_with_pandas(filename):
    """
    Read text from a file using the pandas library.

    Parameters
    ----------
    filename : str
        Path to the file.

    Returns
        str (Contents of the file as text)
    """
    df = pandas.read_csv(filename, header=None)
    return df.to_string(index=False)