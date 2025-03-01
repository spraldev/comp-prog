



def solve(s):
    if s == "MOO":
        return 0
    if len(s) < 3:
        return -1
    else:
        count = 0
        last_MO = s.rfind("MO")
        if last_MO == len(s) - 2:
            last_MO = s[:last_MO].rfind("MO")
        
        if last_MO == -1 and s == "M" * len(s):
            return -1
        elif last_MO == -1 and s == "O" * len(s):
            return len(s) - 3 + 1
        elif last_MO == -1:
            return -1

        if s[last_MO +2] == "M":
            count += 1


        count += len(s[last_MO + 2:]) + len(s[:last_MO]) - 1

        

        return count

        

Q = int(input())

for _ in range(Q):
    s = input()
    print(solve(s))