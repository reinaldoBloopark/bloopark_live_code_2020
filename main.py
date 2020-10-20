def overlap(l1, l2):
    """
    Evaluate if two lines (x1,x2) and (x3,x4) on the x-axis overlaps
    Args:
      l1: tuple (int, int), the first line.
      l2: tuple (int, int), the second line.
    Returns:
      If the two lines overlaps returns True, otherwise returns False.
      If one line starts in the same point that the other ends is considered
      overlapping.
    """
    pass


def find_overlaps(lines):
    """
    From a dictionary of lines determines pairs of overlapped lines
    Args:
      lines: dict (str: tuple), dictionary where the keys are the name of the
             lines and the value is its coordinates
    Returns:
      list: [tuple1, tuple2, ...] where each element is a tuple containing
            a pair of lines that overlaps.
    Example:
        input => {
            'A': (3, 6),
            'B': (1, 8),
            'C': (15, 11),
            'D': (6, 9)
        }
        output => [('A', 'B'), ('A', 'D'), ('B', 'D')]
    """
    pass
