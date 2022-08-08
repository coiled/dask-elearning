@delayed
def inc(x):
    """Increments x by one"""
    sleep(1)
    return x + 1

@delayed
def add(x, y):
    """Adds x and y"""
    sleep(1)
    return x + y