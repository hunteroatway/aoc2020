import re

data = [i.strip() for i in open('inputs/4.txt', 'r').readlines()]
required_fields = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']

def solve_p1(data):
  valid_passport_count = 0
  req_field_count = 0

  for line in data:
    if line == '':
      if req_field_count == len(required_fields):
        valid_passport_count += 1
      req_field_count = 0
      continue

    for field in line.split():
      attr, val = field.split(':')
      if attr in required_fields:
        req_field_count += 1
    
  return valid_passport_count

def solve_p2(data):
  valid_passport_count = 0
  passport = {}

  for line in data:
    if line == '':
      if validate(passport):
        valid_passport_count += 1
      passport = {}
      continue
      
    for field in line.split():
      attr, val = field.split(':')
      passport[attr] = val

  return valid_passport_count

def validate(passport):
  REGEX = [
    r"(?:19[2-9]\d|200[0-2])\b", #byr
    r"20(?:1\d|20)\b", #iyr
    r"20(?:2\d|30)\b", #eyr
    r"(?:1(?:[5-8]\d|9[0-3])cm|(?:59|6\d|7[0-6])in)\b", #hgt
    r"#[0-9a-f]{6}\b", #hcl
    r"(amb|blu|brn|gry|grn|hzl|oth)\b", #ecl
    r"\d{9}\b", #pid
  ]

  for f in required_fields:
    if f not in passport:
      return False

  if re.match(REGEX[0], passport['byr']) is None:
    return False
  if re.match(REGEX[1], passport['iyr']) is None:
    return False
  if re.match(REGEX[2], passport['eyr']) is None:
    return False
  if re.match(REGEX[3], passport['hgt']) is None:
    return False
  if re.match(REGEX[4], passport['hcl']) is None:
    return False
  if re.match(REGEX[5], passport['ecl']) is None:
    return False
  if re.match(REGEX[6], passport['pid']) is None:
    return False
  return True

print(solve_p1(data)) # off by 1
print(solve_p2(data)) # off by 1