input = [i.rstrip() for i in open("inputs/3.txt")]

def solve(right, down):
  i, t = 0, 0
  for line_index, line_val in enumerate(input):
    if line_index % down == 0:
      char = list(line_val)
      if i >= len(char):
        i -= len(char)
      if char[i] == '#':
        t += 1
      i += right
  return t
      
print(solve(3, 1))
print(solve(1, 1)*solve(3, 1)*solve(5, 1)*solve(7, 1)*solve(1, 2))