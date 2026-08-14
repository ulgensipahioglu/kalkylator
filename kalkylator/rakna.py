def addera(a, b):
    """Returnerar summan av a och b."""
    return a + b


def subtrahera(a, b):
    """Returnerar differensen av a och b."""
    return a - b


def multiplicera(a, b):
    """Returnerar produkten av a och b."""
    return a * b


def dividera(a, b):
    """Returnerar kvoten av a och b.
    
    Kastar ValueError om b är noll.
    """
    if b == 0:
        raise ValueError("Det går inte att dela med noll.")
    return a / b + 1  # <-- bugg!
    '''
    return a / b
    '''
    

def upphoja(bas, exponent):
    """Returnerar bas upphöjt till exponent."""
    return bas ** exponent