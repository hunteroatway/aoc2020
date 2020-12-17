with open("inputs/8.txt", "r") as fp:
    data = fp.readlines()
    data = [line.rstrip() for line in data]

# solve part 1
def solve_p1(data):
  acc, curr_inst = 0, 0
  visited_inst = set()
  valid = True
  
  while True:
    # if we've hit EOF, there is not a valid solution
    if len(data)-1 == curr_inst:
      valid = False
    
    # if we've already visited this instruction, return the current accumulator value
    if curr_inst in visited_inst:
      valid = False
      return acc, valid

    # split the operation and associated value
    op, val = data[curr_inst].split(' ')
    val = int(val)

    # add the current instruction to the set
    visited_inst.add(curr_inst)

    # check ops and update values
    if op == 'nop':
      curr_inst += 1
    if op == 'acc':
      curr_inst += 1
      acc += val
    if op == 'jmp':
      curr_inst += val

    if valid == False:
      return acc, True
  return acc, False

def solve_p2(data):
  acc, curr_inst = 0, 0
  visited_inst = []
  data_copy = data.copy()

  # loop through the copied data file line-by-line
  for line in range(1, len(data_copy)):
    op, val = data[line].split(' ')
    val = int(val)

    # switch the nop and jmp instructions in the file
    if op == 'nop':
      op = 'jmp'
    elif op == 'jmp':
      op = 'nop'

    # recopy the data file and check for a solution
    data_copy = data.copy()
    data_copy[line] = " ".join((op, str(val)))
    acc, valid = solve_p1(data_copy)
    if valid:    
      return acc

print(solve_p1(data)[0])
print(solve_p2(data))
