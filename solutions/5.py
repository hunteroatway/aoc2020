data = [i.strip() for i in open("inputs/5.txt").readlines()]

def find_seat_ids(data):
  seat_ids = []
  binary_map = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
  for i in range(len(data)):
    seat = ''.join([binary_map[x] for x in data[i]])
    seat_ids.append(int(seat, 2))
  return sorted(seat_ids)

def find_missing(seat_ids):
  for i in range(len(seat_ids)):
    if seat_ids[i+1] - seat_ids[i] != 1:
      return seat_ids[i]+1
    else:
      continue

def solve_p1(data):
  return max(find_seat_ids(data))

def solve_p2(data):
  return find_missing(find_seat_ids(data))

print(solve_p1(data))
print(solve_p2(data))