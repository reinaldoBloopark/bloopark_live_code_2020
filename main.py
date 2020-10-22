from itertools import combinations

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
    # Check if l2 lies within l1
    if min(l1) <= min(l2) and max(l1) >= max(l2):
      return True
    # return if l1 lies within or itersects with l2
    return (l1[0] >= min(l2) and l1[0] <= max(l2)) or (l1[1] >= min(l2) and l1[1] <= max(l2))
       
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
    output = list()
    keys = list(lines)
    # sort the keys as dict is unordered
    keys.sort()
    comb = combinations(keys, 2)
    for i in list(comb):
      if overlap(lines[i[0]], lines[i[1]]):
        output.append(i)
    # for i in range(len(keys)):
    #   # Need to check first with only rest of the items
    #   # and so on...
    #   for j in range(i+1, len(keys)):
    #     if overlap(lines[keys[i]], lines[keys[j]]):
    #       output.append(tuple((keys[i], keys[j])))
    return output
