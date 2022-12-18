def distance(string1, string2):
    if len(string1) > len(string2) or len(string2) > len(string1) \
            or string1 is None or string2 is None:
        raise ValueError(".+")
    else:
        return sum(c1 != c2 for c1, c2 in zip(string1, string2))