# No Gemini imports needed for this function

def pretty_print(text, indent_level=0, color='red'):
    """This function takes a string as input and prints it to the console
    with enhanced formatting and styling. It could include features like
    syntax highlighting, indentation, or other visual enhancements.
    For instance, pretty_print("Hello, world!") would display 'Hello, world!'
    with some specific formatting.

    Args:
        text (str): The string to be printed.
        indent_level (int, optional):  The level of indentation (number of tabs). Defaults to 0.
        color (str, optional):  The color of the text.  Options include 'white', 'red', 'green', 'blue'. Defaults to 'white'.
    """
    indent = "    " * indent_level  # Use 4 spaces per indent level

    color_code = {
        'white': '\033[0m',  # Reset
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
    }.get(color.lower(), '\033[0m')  # Default to white if color is invalid

    print(f"{color_code}{indent}{text}{'\033[0m'}") # Prints the formatted text

