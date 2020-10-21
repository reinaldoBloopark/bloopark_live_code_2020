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

    # get x1 and x2
    x1, x2 = l1
    x3, x4 = l2

    # algorithm
    # we are going to test if x1 is in [x3,x4], if it is correct we return True
    # same thing with x2 if x2 is in [x3, x4] we return True
    # otherwise we return False

    if x1 >= x3 and x1 <= x4:
      return True

    if x2 >= x3 and x2 <= x4:
      return True

    if x3 >= x1 and x3 <= x2:
      return True

    if x4 >= x1 and x4 <= x2:
      return True

    return False

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

    """
      output: the variable to be return
      keys_already_used: the variable we use to keep track of already used key
    """
    output = []
    keys_already_used = []

    # loop all the element in dictionnary
    for key_to_loop in lines.keys():

      # get the first tuple
      l1 = lines[key_to_loop]

      for key_line in lines:

        # if key have already been used we continue
        # or if it is the same key we continue
        if key_line in keys_already_used or key_line == key_to_loop:
          continue

        # get the second tuple
        l2 = lines[key_line]

        # if the l1 and l2 overlap, we add it inside the output list
        if overlap(l1, l2):
          output.append((key_to_loop, key_line))

      # we add this key in key already looped
      keys_already_used.append(key_to_loop)

    return output
