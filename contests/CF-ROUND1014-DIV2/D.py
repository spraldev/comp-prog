def is_balanced(s):
    return s.count('L') == s.count('I') == s.count('T')


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    

    if is_balanced(s):
        print(0)
        continue

    if len(s) == 1:
        print(-1)
        continue

    op_log = []
    max_ops = 2 * n
    for _ in range(max_ops):
        if is_balanced(s):
            break

        current_counts = (s.count('L'), s.count('I'), s.count('T'))
        current_imbalance = max(current_counts) - min(current_counts)
        
        best_move = None
        best_imbalance = current_imbalance
        fallback = None
        

        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                continue

            missing = (set("LIT") - {s[i], s[i+1]}).pop()
            new_s = s[:i+1] + missing + s[i+1:]
            new_counts = (new_s.count('L'), new_s.count('I'), new_s.count('T'))
            new_imbalance = max(new_counts) - min(new_counts)
            if fallback is None:
                fallback = (i, missing, new_imbalance)
            if new_imbalance < best_imbalance:
                best_imbalance = new_imbalance
                best_move = (i, missing, new_imbalance)
                if best_imbalance == 0:
                    break

        if best_move is None:
            if fallback is not None:
                best_move = fallback
            else:
                break 
        i, letter, _ = best_move
        s = s[:i+1] + letter + s[i+1:]
        op_log.append(i + 1) 

    if is_balanced(s):
        print(len(op_log))
        for op in op_log:
            print(op)
    else:
        print(-1)
