def main(s,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return s[:-n] if n <=len(s) else ""


print (main("Hello,World!",4))
print (main("Kompyuter",2))