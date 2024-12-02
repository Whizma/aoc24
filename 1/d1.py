def p1():
    with open('input.txt', 'r') as file:
        lines = [line.strip().split() for line in file]
        l1 = sorted(int(line[0]) for line in lines)
        l2 = sorted(int(line[1]) for line in lines)
        res = sum(abs(id1 - id2) for id1, id2 in zip(l1, l2))
    print(res)

def p2():
    with open('input.txt', 'r') as file:
        lines = [line.strip().split() for line in file]
        l1 = sorted(int(line[0]) for line in lines)
        l2 = {}
        for line in lines:
            key = int(line[1])
            l2[key] = l2.get(key, 0) + key
        
        res = sum(l2.get(id, 0) for id in l1)
    print(res)

p1()
p2()