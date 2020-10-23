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
    start1 = l1[0]
    end1 = l1[1]   
    
    start2 = l2[0]
    end2 = l2[1]
        
    if (start1 >= start2 and start1 <= end2) or (end1 >= start2 and end1 <= end2) or (start1 <= start2 and end1 >= end2):
        return True
    else:
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
    from itertools import combinations 
    line_keys = list(combinations(lines, 2))
    res = [] 
    for ky in line_keys:        
        l1 = lines[ky[0]]
        l2 = lines[ky[1]]
        if overlap(l1, l2):
            res.append(ky)
    return res

a = { 
        'A': (3, 6),
        'B': (1, 8),
        'C': (15, 11),
        'D': (6, 9),
        #'E': (16, 9),
        #'F': (11, 9),
        #'G': (12, 20),
        #'H': (2, 10),
        #'I': (21, 22),
    }

print ("Res", find_overlaps(a))
