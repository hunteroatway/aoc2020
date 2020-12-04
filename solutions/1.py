from itertools import combinations_with_replacement

#input = [1721, 979, 366, 299, 675, 1456]
input = [int(i.rstrip()) for i in open("inputs/1.txt")]

def target(input):
  return sum(input) == 2020

two_sum = list(filter(target, list(combinations_with_replacement(input, 2))))
three_sum = list(filter(target, list(combinations_with_replacement(input, 3))))

two_sum_res = two_sum[0][0] * two_sum[0][1]
three_sum_res = three_sum[0][0] * three_sum[0][1] * three_sum[0][2]

print(two_sum_res, three_sum_res)