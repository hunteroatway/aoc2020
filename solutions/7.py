import re
from collections import defaultdict

data = [i.strip() for i in open("inputs/7.txt").readlines()]

def parse(data):
  bags = defaultdict(dict)
  for line in data:
    bag = re.match(r'(.*) bags contain', line).groups()[0]
    for c, b in re.findall(r'(\d+) (\w+ \w+) bag', line):
      bags[bag][b] = int(c)
  return bags  

def solve_p1(bags):
  ret = set()
  def search(colour):
    for i in bags:
      if colour in bags[i]:
        ret.add(i)
        search(i)
  search('shiny gold')
  return len(ret)

def solve_p2(bags):
  def search(bag):
    count = 1
    for x in bags[bag]:
      m = bags[bag][x]
      count += m * search(x)
    return count
  return search('shiny gold') - 1

print(solve_p1(parse(data)))
print(solve_p2(parse(data)))
