from datastubs import STRING_LIST


def reverse_alpha():
    
    return sorted(STRING_LIST, reverse=True)


def alpha_case_insensitive():
    
    return sorted(STRING_LIST, key=str.lower)


def by_longest_length():
    
    def foo(STRING_LIST):
        return len(STRING_LIST)
    return sorted(STRING_LIST, key=foo, reverse=True)
    
def filter_and_sort_number_strings():
    """
    Filter the original list for strings that
    contain numbers. Then sort that list of number
    strings but as strings (i.e. alphaebtical order)

    Hint: string objects have a method named .isnumeric()
    https://www.geeksforgeeks.org/python-string-isnumeric-application/

    """
    # fill it out


def filter_and_sort_number_strings_as_numbers():
    """
    Filter the list for strings that contain numbers
    and then sort that list of strings in *numerical* order

    Hint: string objects have a method named .isnumeric()
    https://www.geeksforgeeks.org/python-string-isnumeric-application/

    Hint: Use the int() or float() method to convert a numeric string
       into an actual number
    """
    # fill it out


