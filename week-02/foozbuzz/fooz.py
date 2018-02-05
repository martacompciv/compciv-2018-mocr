<<<<<<< HEAD
def fob(x):
    for i in range(1,x + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "Foozbuzz")
            continue
        elif i % 3 == 0:
            print(i, "Fooz")
            continue
        elif i % 5 == 0:
            print(i, "Buzz")
            continue
=======
def fob(x):
    for i in range(1,x + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "foozbuzz")
            continue
        elif i % 3 == 0:
            print(i, "fooz")
            continue
        elif i % 5 == 0:
            print(i, "buzz")
            continue
>>>>>>> 8ca8f4c5a16b1245613c8cd625edf7d70d9d2c60
        print(i)