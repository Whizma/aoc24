with open('input.txt', 'r') as file:
  grid = [line.strip() for line in file]


def p1(grid):
  rows, cols = len(grid), len(grid[0])
  total = 0

  directions = [
      (0, 1),    # right
      (0, -1),   # left
      (1, 0),    # down
      (-1, 0),   # up
      (-1, 1),   # up-right
      (-1, -1),  # up-left
      (1, 1),    # down-right
      (1, -1)    # down-left
  ]

  def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols

  def check_xmas(r, c, dr, dc):
    if (is_valid(r, c) and is_valid(r+dr*3, c+dc*3)):
      string = ''.join(grid[r+j*dr][c+j*dc] for j in range(4))
      return string == "XMAS"
    return False

  for r in range(rows):
    for c in range(cols):
      for dr, dc in directions:
        if check_xmas(r, c, dr, dc):
          total += check_xmas(r, c, dr, dc)

  print(total)


def p2(grid):
  rows, cols = len(grid), len(grid[0])
  total = 0
  for r in range(1, rows-1):
    for c in range(1, cols-1):
      if grid[r][c] == 'A':

        if grid[r+1][c-1] == 'M' and grid[r+1][c+1] == 'M':       # M-M
          if grid[r-1][c-1] == 'S' and grid[r-1][c+1] == 'S':     # A
            total += 1                                            # S-S

        if grid[r-1][c-1] == 'M' and grid[r-1][c+1] == 'M':       # S-S
          if grid[r+1][c-1] == 'S' and grid[r+1][c+1] == 'S':     # A
            total += 1                                            # M-M

        if grid[r+1][c-1] == 'M' and grid[r-1][c-1] == 'M':       # M-S
          if grid[r+1][c+1] == 'S' and grid[r-1][c+1] == 'S':     # A
            total += 1                                            # M-S

        if grid[r+1][c+1] == 'M' and grid[r-1][c+1] == 'M':       # S-M
          if grid[r+1][c-1] == 'S' and grid[r-1][c-1] == 'S':     # A
            total += 1                                            # S-M

  print(total)


p1(grid)
p2(grid)
