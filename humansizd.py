SUFFIXES = [ 'KB', 'MB', 'TB', 'PB', 'EB', 'ZB', 'YB' ]

def approximate_size(size):
    """ Conver a file size to a human-readable form.
    Keyword arguments:
    size -- file size in bytes

    Returns: string
    """
    if size < 0:
        raise ValueError('number must be non-positive')
    multiple = 1024
    for suffix in SUFFIXES:
        size /= SUFFIXES[multiple]
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('number too long')
            