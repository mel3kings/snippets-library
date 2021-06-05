#!/usr/bin/python

import sys

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

input = sys.argv[1:]
if not input:
    input = """convert_me_to_camel"""
    print("no input provided defaulting to " + input)
print("DONE:" + to_camel_case(input))

