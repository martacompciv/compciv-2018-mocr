
ez_list = [0, 1, 2, 3, 4, ['a', 'b', 'c'], 5, ['apples', 'oranges'], 42]

def foo_hello():

    return type(ez_list)

def foo_a():

    return ez_list[0]

def foo_b():
   
   return ez_list[1] + ez_list[3]

def foo_c():

    return ez_list[8]

def foo_cx():

    return type(ez_list[7])

def foo_d():

    return ez_list[7][1]

def foo_e():

    return len(ez_list)

def foo_f():

    string1 = str(ez_list[5][0])
    string2 = str(ez_list[5][1])
    string3 = str(ez_list[5][2])

    return (string1 + ';' + string2 + ';' + string3)

def foo_g():

    myList = [ez_list[1], ez_list[2], ez_list[3], ez_list[4]]
    return myList

def foo_h():

    myList = [ez_list[8], ez_list[7], ez_list[6]]
    return myList