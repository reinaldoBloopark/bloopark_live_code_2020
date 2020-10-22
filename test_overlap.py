import main

"""
Overlapping Test cases:
Case 1: (1,5), (2,8)
Case 2: (5,1), (2,8)
Case 3: (5,1), (8,2)
Case 4: (1,5), (8,2)
Case 5: (2,8), (1,5)
Case 6: (2,8), (5,1)
Case 7: (8,2), (1,5)
Case 8: (8,2), (5,1)

Non-overlapping test cases:
Case 9: (1,4), (5,8)
Case 10: (1,4), (8,5)
Case 11: (4,1), (5,8)
Case 12: (4,1), (8,5)
Case 13: (8,5), (1,4)
Case 14: (8,5), (4,1)
Case 15: (5,8), (4,1)
Case 16: (5,8), (1,4)
"""
test_cases = {
  '1': [(1,5), (2,8)],
  '2': [(5,1), (2,8)],
  '3': [(5,1), (8,2)],
  '4': [(1,5), (8,2)],
  '5': [(2,8), (1,5)],
  '6': [(2,8), (5,1)],
  '7': [(8,2), (1,5)],
  '8': [(8,2), (5,1)],
  '9': [(1,4), (5,8)],
  '10': [(1,4), (8,5)],
  '11': [(4,1), (5,8)],
  '12': [(4,1), (8,5)],
  '13': [(8,5), (1,4)],
  '14': [(8,5), (4,1)],
  '15': [(5,8), (4,1)],
  '16': [(5,8), (1,4)],
  '17': [(-5,-8), (1,-6)],
  '18': [(-5,8), (1,-4)],
  '19': [(-5,-1), (-6,-9)],
}


# While adding keys to test_case only use consecutive
# integers
for i in range(1, 1 + len(test_cases.keys())):
  j = str(i)
  output = "Test case {} with (l1,l2): {}: ".format(i, test_cases[j])
  if main.overlap(test_cases[j][0], test_cases[j][1]):
    output += "OVERLAPS"
  else:
    output += "NO OVERLAPS"
  print(output)