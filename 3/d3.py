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
    combined_pattern = (
        r'(?P<mul>mul\((\d{1,3}),(\d{1,3})\))|'
        r'(?P<do>do\(\))|'
        r'(?P<dont>don\'t\(\))'
    )    
    mul = True
    res = 0
    for line in instructions:
      matches = re.finditer(combined_pattern, line)
      for match in matches:
        print(match.group(2))
        if match.group('mul'):
          if mul:
            a = int(match.group(2))
            b = int(match.group(3))
            res += a * b
          else:
            print("yurr")
        elif match.group('do'):
          print('do')
          mul = True
        elif match.group('dont'):
          print('dont')
          mul = False
        
    print(res)


p1()
p2()
