import re


def p1():
  with open('input.txt', 'r') as file:
    instructions = [line.strip() for line in file]
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    res = 0
    for line in instructions:
      matches = re.finditer(pattern, line)
      for match in matches:
        a = int(match.group(1))
        b = int(match.group(2))
        res += a * b
    print(res)


def p2():
  mul = True
  
  with open('input.txt', 'r') as file:
    instructions = [line.strip() for line in file]
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    mul = True
    
    res = 0
    for line in instructions:
      matches = re.finditer(pattern, line)
      for match in matches:
        a = int(match.group(1))
        b = int(match.group(2))
        res += a * b
      
    print(res)


p1()
p2()
