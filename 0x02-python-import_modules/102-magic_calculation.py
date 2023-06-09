#!/usr/bin/python3

def magic_calculation(a, b):
    add = __import__('add_0').add
    sub = __import__('sub_0').sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

# import dis
# print(dis.dis(magic_calculation))
