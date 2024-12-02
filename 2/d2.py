def p1():
  with open('input.txt', 'r') as file:
    levels = [list(map(int, line.strip().split())) for line in file]
    ans = sum(is_valid_sequence(level) for level in levels)
  print(ans)


def is_valid_sequence(level):
  increasing = level[0] < level[1]
  for a, b in zip(level, level[1:]):
    if a == b:
      return False

    if increasing and (b - a < 1 or b - a > 3 or b <= a):
      return False

    if not increasing and (a - b < 1 or a - b > 3 or b >= a):
      return False

  return True


def problem_dampener(level):
  if is_valid_sequence(level):
    return True

  for i in range(len(level)):
    test_level = level[:i] + level[i+1:]
    if is_valid_sequence(test_level):
      return True

  return False


def p2():
  with open('input.txt', 'r') as file:
    levels = [list(map(int, line.strip().split())) for line in file]
    ans = sum(problem_dampener(level) for level in levels)
  print(ans)


p1()
p2()
