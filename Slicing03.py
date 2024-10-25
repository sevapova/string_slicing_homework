def main(s):
    """The s string variable is given. Return all characters except the one at the beginning and end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    x=s[1:len(s)]
    return x
a = main('Salom hjvkgjhvkjb!')
print(a)
