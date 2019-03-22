SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']


def approximate_size(size=100_000):
    """Convert a file size to human-readable form.
    Keyword arguments:
    size -- file size in bytes
    Returns: string
    """
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024
    for suffix in SUFFIXES:
        size /= SUFFIXES[multiple]
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('number too large')


if __name__ == '__main__':
    print(approximate_size(1000))
    print(approximate_size(100))
    print(approximate_size(999000))
    print(approximate_size(1000))
    print(approximate_size())
