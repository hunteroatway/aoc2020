from string import ascii_letters

#input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
input = [i.rstrip() for i in open("inputs/2.txt")]

def solve_p1():
  num_invalid = 0
  for i in range(len(input)):
    total = len(input)
    x = input[i].split(' ')
    min, max = x[0].split('-')[0], x[0].split('-')[1]
    val = x[1].replace(':', '')
    pwd = x[2]

    if (pwd.count(val) < int(min) or pwd.count(val) > int(max)):
      num_invalid += 1
  return total - num_invalid

def solve_p2():
  num_invalid = 0
  for i in range(len(input)):
    total = len(input)
    x = input[i].split(' ')
    min, max = x[0].split('-')[0], x[0].split('-')[1]
    val = x[1].replace(':', '')
    pwd = x[2]

    if(pwd[int(min)-1] == val and pwd[int(max)-1] == val):
      num_invalid += 1
    elif (pwd[int(min)-1] != val and pwd[int(max)-1] != val):
      num_invalid += 1
  return total - num_invalid

print(solve_p1(), solve_p2())