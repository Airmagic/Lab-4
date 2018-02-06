def area(base, height):
    '''computing the area of a triangle'''
    if base < 0 or height < 0:
        raise ValueError('numbers have to be postive. \n was given base: {}, height {}'.format(base, height))
    area = base * height /2
    return area
