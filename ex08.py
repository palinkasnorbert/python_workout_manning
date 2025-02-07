def strsort(word: str) -> str:
    """
    strsort, that takes a single string as its input and returns a string. 
    The returned string should contain the same characters as the input, 
    except that its characters should be sorted in order, 
    from the lowest Unicode value to the highest Unicode value.
    """

    return "".join(sorted(word))

print(strsort("cba"))