# try to reconstruct the optimal program?
# wait.... there is no need for the count of the repeating sequences


def find_repeating_sequences(lst):
    result = []
    i = 0
    n = len(lst)
    
    while i < n:
        best = None 
        for k in range(1, (n - i) // 2 + 1):
            pattern = lst[i:i+k]
            count = 1
            while i + (count+1) * k <= n and lst[i + count * k : i + (count+1) * k] == pattern:
                count += 1
            if count > 1:
                total_length = count * k
                if best is None or total_length > best[2]:
                    best = (pattern, count, total_length)
        if best is not None:
            result.append((tuple(best[0]), best[1]))
            i += best[2]  
        else:
            result.append(((lst[i],), 1))
            i += 1
    return result


def solve():
    N, K = map(int, input().split())

    A = list(map(int, input().split()))

    seqs = find_repeating_sequences(A)
    cnt = 0



    for sqr in seqs:
        newSqr = sqr[0]
        cnt += len(set(newSqr))


    
    print("YES" if cnt <= K else "NO")


for _ in range(int(input())):


    solve()