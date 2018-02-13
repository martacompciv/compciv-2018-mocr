from datastubs import NUMBER_LIST


def reverse_numerical_order():

    return sorted(NUMBER_LIST, reverse=True)


def numerical_order():
   
    return sorted(NUMBER_LIST)


def as_absolute_value():
   
   return sorted(NUMBER_LIST, key=abs)


def as_inverse_number():
    
    def foo(x):
        return 1/x
    
    return sorted(NUMBER_LIST, key=foo)
