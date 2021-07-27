def to_pascal_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[0:])


input = """ convert_me_to_pascal """
print(to_pascal_case(input))
