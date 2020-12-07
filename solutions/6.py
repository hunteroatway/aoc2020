from collections import Counter

# import data
data = [i.strip() for i in open('inputs/6.txt', 'r').readlines()]

# solve part 1
def solve_p1(data):
  current_count = 0
  total_count = 0
  complete_group = ""

  # loop through each line in the dataset
  for line in data:
    # empty lines start a new group, reset values and update total
    if line == '':
      total_count += current_count
      current_count = 0
      complete_group = ""
      continue
    
    # continue adding lines to a complete group set until a line break
    for group in line.split():
      complete_group += group
    
    # set the current question count to the length to the unique values in the set
    current_count = len(set(complete_group))
  return total_count + current_count

# solve part 2
def solve_p2(data):
  group = []
  groups = []
  total = 0

  # loop through each line in the dataset
  for line in data:
    # append to line to current group if not empty, otherwise start a new group
    if line != '':
      group.append(line)
    else:
      groups.append(group)
      group = []

  # loop through each group in the list of groups
  for group in groups:
    # get the current size of the group (# of elements in list)
    size = len(group)
    # create a counter object which counts the number of times an element occurs in the list
    counts = Counter(''.join(group))
    # counts the number of items in which that element appears in all elements
    counts = Counter(list(counts.values()))[size]
    total += counts
  return total + counts

print(solve_p1(data))
print(solve_p2(data))