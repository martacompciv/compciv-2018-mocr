from datastubs import PEOPLE_LIST

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():

    def foo(x):
        return x['age']

    return sorted(PEOPLE_LIST, key=foo)
   
   
    """
    sort by age in ascending order
    """
    # fill it out

def oldest():

    def foo(x):
        return x['age']
    
    return sorted(PEOPLE_LIST, key=foo, reverse=True)
   
   
    """
    sort by age in descending order
    """
    # fill it out


def name_reverse_alpha():

    def foo(x):
        return x['name']

    return sorted(PEOPLE_LIST, key=foo, reverse=True)

def country_then_age():
    
    def foo(x):
        return x['country']
    def bob(y):
        return y['age']
    s = sorted(PEOPLE_LIST, key=bob)

    return sorted(s, key=foo)
