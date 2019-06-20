import logging

logger = logging.getLogger(__name__)


def van_eck_sequence():
    """https://oeis.org/A181391
    """
    seen = {}
    yield 0
    current = 0
    i = 1
    while True:
        next_value = i - seen[current] if current in seen else 0
        yield next_value
        seen[current] = i
        i += 1
        current = next_value
