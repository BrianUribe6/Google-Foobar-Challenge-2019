from math import sqrt, floor


def solution(area):
  ans = []
  while area >0:
    nearest_square = int(sqrt(area))**2
    ans.append(nearest_square)
    area -= nearest_square
  return ans


